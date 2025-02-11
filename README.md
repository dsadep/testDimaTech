Требования

  - Python
  - PostgreSQL
  - Docker Desktop

### Клонирование репозитория

```
git clone https://github.com/dsadep/testDimaTech.git
cd testDimaTech
```

## Запуск приложения

### С использованием Docker Compose

1. Создайте файл .env и .env-non-dev в корне проекта и добавьте ваши переменные окружения и заполните их в соответствии с .env.example и .env-non-dev.example

2. Запустите приложение с помощью Docker Compose:

   ```docker-compose up --build```
   
3. Документация к API будет доступна по адресу http://localhost:7777/docs.

### Без Docker

1. Убедитесь, что у вас установлен Python и PostgreSQL.
2. Создайте виртуальное окружение и активируйте его:

   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Установите зависимости:

    ```pip install -r requirements.txt```
   

4. Создайте файл .env и .env-non-dev в корне проекта и добавьте ваши переменные окружения и заполните их в соответствии с .env.example и .env-non-dev.example
   

5. Запустите миграции (если используете Alembic):

   ```alembic upgrade head```
   

6. Запустите приложение:

   ```uvicorn app.main:app --reload```
   

7. Документация к API будет доступна по адресу http://localhost:8000/docs.
