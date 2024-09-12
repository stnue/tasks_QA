
## Задание 1

Для просмотра решения задания 1 откройте файл task_1.pdf в папке .avito_task_1.

## Задание 2

## Инструкция по запуску тестов и созданию отчетов Allure

**1. Клонируйте репозиторий проекта выполнив команду:**

git clone https://github.com/stnue/tasks_QA.git

Или скачайте ZIP-архив по ссылке (https://github.com/stnue/tasks_QA/archive/refs/heads/main.zip) и распакуйте его.

**2. Убедитесь, что на вашем компьютере установлен Python, с помощью команды:**

python --version

Если Python не установлен, скачайте его с официального сайта Python и установите, выбрав подходящую версию для вашей операционной системы. В процессе установки обязательно отметьте галочку в чекбоксе "Add python.exe to PATH".

**3. Установите зависимости проекта**

- Перейдите в корневую директорию проекта:


cd /путь/до/директории/с/проектом

- Установите необходимые зависимости из файла requirements.txt, с помощью команды:


pip install -r requirements.txt

Если команда не работает, попробуйте:

pip3 install -r requirements.txt

**4. Установите драйвер ChromeDriver для Selenium:**

Скачайте  драйвер (https://googlechromelabs.github.io/chrome-for-testing) и добавьте его корневую папку.

**5. Установите Allure Commandline:**

Чтобы создать отчеты Allure, нужно установить инструмент Allure Commandline. Для этого выполните следующие шаги:

- Перейдите на страницу релизов Allure (https://github.com/allure-framework/allure2/releases) и скачайте ZIP-архив последней версии.

- Распакуйте скачанный архив в удобное место на вашем компьютере.

- Добавьте путь к бинарным файлам в PATH:

Это нужно сделать через "Системные свойства" -> "Дополнительные параметры системы" -> "Переменные среды" -> "PATH".

- Проверьте установку Allure, с помощью команды:

allure --version

Если команда возвращает версию Allure, установка прошла успешно.

Если не находит путь, то попробуйте запуск команды с полным путем до allure:

C:\Program Files\Allure\bin\allure --version

**6. Запустите тесты, с помощью команды:**

pytest 

**7. сохраните результаты тестов в папку allure-results, с помощью команды:**

 allure generate allure-results --clean -o allure-report

**8. Создайте отчет Allure командой:**

allure serve allure-results

Эта команда запускает локальный сервер и открывает отчет Allure в вашем веб-браузере.
Здесь перейдите в вкладку Suites, где отображаются отчеты по тестам.


**9. Очистите старые отчеты (опционально)**

Если вам нужно очистить старые отчеты перед созданием нового, вы можете удалить папку allure-results, с помощью команды:


rm -rf allure-results

## Примечания
Убедитесь, что у вас установлены все необходимые инструменты и библиотеки для работы с Selenium и Allure.

