# implements Kafka topic consumer functionality

import threading
from confluent_kafka import Consumer, OFFSET_BEGINNING
import json
import os
from werkzeug.utils import secure_filename
from producer import proceed_to_deliver

CWD: str = None

def save_file(update: bytes, name):
    update_path = os.path.join(CWD, 'data', secure_filename(name))
    with open(update_path, 'wb') as update_file:
        update_file.write(update)

def get_update(name):
    update_path = os.path.join(CWD, 'data', secure_filename(name))
    with open(update_path, 'rb') as f:
        update = f.read()
        return json.loads(update)

def handle_event(id: str, details: dict):    
    # print(f"[debug] handling event {id}, {details}")
    print(f"[info] handling event {id}, {details['source']}->{details['deliver_to']}: {details['operation']}")
    try:
        # TODO: implement handlers
        if details['operation'] == 'save_file':
            update = details['blob']
            name = details['module_name']
            save_file(json.dumps(update).encode(), name)
            
        elif details['operation'] == 'get_software_update':
            details['blob'] = get_update(details['module_name'])
            details['operation'] = 'send_software_update'
            details['deliver_to'] = 'plc_updater'
            proceed_to_deliver(id, details)

    except Exception as e:
        print(f"[error] failed to handle request: {e}")

def consumer_job(args, config):
    # Create Consumer instance
    storage_consumer = Consumer(config)

    # Set up a callback to handle the '--reset' flag.
    def reset_offset(storage_consumer, partitions):
        if args.reset:
            for p in partitions:
                p.offset = OFFSET_BEGINNING
            storage_consumer.assign(partitions)

    # Subscribe to topic
    topic = "storage"
    storage_consumer.subscribe([topic], on_assign=reset_offset)

    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = storage_consumer.poll(1.0)
            if msg is None:
                pass
            elif msg.error():
                print(f"[error] {msg.error()}")
            else:
                try:
                    id = msg.key().decode('utf-8')
                    details_str = msg.value().decode('utf-8')
                    # TODO: decrypt msg
                    # print("[debug] consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                        # topic=msg.topic(), key=id, value=details_str))
                    handle_event(id, json.loads(details_str))
                except Exception as e:
                    print(
                        f"Malformed event received from topic {topic}: {msg.value()}. {e}")
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        storage_consumer.close()


def start_consumer(args, config):
    global CWD
    CWD = os.path.dirname(__file__)
    threading.Thread(target=lambda: consumer_job(args, config)).start()


if __name__ == '__main__':
    start_consumer(None)