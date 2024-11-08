from fastapi import FastAPI
import asyncio

app = FastAPI()
# Создайте приложение(объект) FastAPI предварительно импортировав класс для него.
# 2.Создайте маршрут к главной странице - "/". По нему должно выводиться сообщение "Главная страница".
@app.get('/')
async def welcome() -> dict:
    return {'message': "Главная страница"}

# 3.Создайте маршрут к странице
# администратора - "/user/admin". По нему должно выводиться сообщение "Вы вошли как администратор".

@app.get('/user/admin')
async def admine() -> str:
    return "Вы вошли как администратор"

# 4.Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".
#
@app.get('/user/{user_id}')
async def useer(user_id) -> str:
    return f"Вы вошли как пользователь № {user_id}"

# 5.Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user".
# По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".

@app.get('/user')
async def us_name_age(username: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

# async def id_paginator(username: str = 'Alex', age: int = 24) -> dict: ставим значения по умолчанию
