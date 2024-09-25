import sqlite3
from faker import Faker
import random

# Підключення до бази даних
conn = sqlite3.connect('hw2.db')
cursor = conn.cursor()

# Ініціалізація Faker
faker = Faker('uk')

# Заповнення таблиці status
statuses = [('new',), ('in progress',), ('completed',)]
cursor.executemany("INSERT INTO status (name) VALUES (?)", statuses)

# Заповнення таблиці users
for _ in range(50):
    fullname = faker.name()
    email = faker.unique.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (fullname, email))

# Отримання всіх користувачів і статусів для використання в задачах
cursor.execute("SELECT id FROM users")
user_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM status")
status_ids = [row[0] for row in cursor.fetchall()]

# Заповнення таблиці tasks
for _ in range(100):
    title = faker.sentence(nb_words=6)
    description = faker.text()
    status_id = random.choice(status_ids)
    user_id = random.choice(user_ids)
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", 
                   (title, description, status_id, user_id))

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()
