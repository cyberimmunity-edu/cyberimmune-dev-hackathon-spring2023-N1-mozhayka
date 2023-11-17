# Условия использования 

Этот проект представляет собой заготовку, MVP, для задачи "ПЛК" и предназначен для получения представления о интерфейсе взаимодействия компонентов, возможных способах реализации их минимального функционала, его объеме и т.д. Таким образом, пример является отправной точкой работы, но не обязательно является образцом "хорошо" или "правильно" и может быть изменен и расширен участниками в своих реализациях.

Применять только в учебных целях. Данных код может содержать ошибки, авторы не несут никакой ответственности за любые последствия использования этого кода.
Условия использования и распространения - MIT лицензия (см. файл LICENSE).

## Настройка и запуск

### Системные требования

Данный пример разработан и проверен на ОС Ubuntu 20.04.5, авторы предполагают, что без каких-либо изменений этот код может работать на любых Debian-подобных OS, для других Linux систем, а также для MAC OS необходимо использовать другой менеджер пакетов. В Windows необходимо самостоятельно установить необходимое ПО или воспользоваться виртуальной машиной с Ubuntu (также можно использовать WSL версии не ниже 2).

### Используемое ПО

Стандартный способ запуска демо предполагает наличие установленного пакета *docker*, а также *docker-compose*. Для автоматизации типовых операций используется утилита *make*, хотя можно обойтись и без неё, вручную выполняя соответствующие команды из файла Makefile в командной строке.

Другое используемое ПО (в Ubuntu будет установлено автоматически, см. следующий раздел):
- python (желательно версия не ниже 3.8)
- pipenv (для виртуальных окружений python)

Для работы с кодом примера рекомендуется использовать VS Code или PyCharm.

В случае использования VS Code следует установить расширения
- REST client
- Docker
- Python

### Настройка окружения и запуск примера

см. [Отчет о выполнении](report.md)