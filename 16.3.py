# Создайте новое приложение FastAPI и сделайте CRUD запросы.
from fastapi import FastAPI, Path
from typing import Annotated
import asyncio

app = FastAPI()
# Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
users = {'1': 'Имя: Example, возраст: 18'}

# Реализуйте 4 CRUD запроса:
# get запрос по маршруту '/users', который возвращает словарь users.
@app.get('/users')
async def return_dict_users() -> dict:
    return users
# post запрос по маршруту '/user/{username}/{age}',
# который добавляет в словарь по максимальному по значению ключом значение строки "Имя: {username},
# возраст: {age}". И возвращает строку "User <user_id> is registered".

@app.post('/user/{username}/{age}')
async def put_data(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registered'

# put запрос по маршруту '/user/{user_id}/{username}/{age}',
# который обновляет значение из словаря users под ключом user_id на строку "Имя: {username},
# возраст: {age}". И возвращает строку "The user <user_id> is updated"
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(description="Enter your ID")],
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return "The user <user_id> is updated"

# delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
@app.delete('/user/{user_id}')
async def delete_message(user_id: Annotated[str, Path(description="Enter your ID")]) -> str:
    users.pop(user_id)
    return f"User {user_id} is deleted "

# Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
# 1. GET '/users'
# {
# "1": "Имя: Example, возраст: 18"
# }
# 2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
# "User 2 is registered"
# 3. POST '/user/{username}/{age}' # username - NewUser, age - 22
# "User 3 is registered"
# 4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
# "User 1 has been updated"
# 5. DELETE '/user/{user_id}' # user_id - 2
# "User 2 has been deleted"
# 6. GET '/users'
# {
# "1": "Имя: UrbanProfi, возраст: 28",
# "3": "Имя: NewUser, возраст: 22"
# }