#!/bin/bash

# Запуск тестов с генерацией Allure-отчетов
pytest -v --alluredir=allure-results

# Генерация Allure-отчета
allure generate --clean allure-results -o allure-report
rm -rf allure-results/history
cp -r allure-report/history allure-results/
allure open allure-report