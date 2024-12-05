import random
from datetime import datetime


def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.completed = False

    def mark_complete(self):
        self.completed = True


def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


def print_current_time():
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def countdown(start):
    for i in range(start, 0, -1):
        print(i)


tasks = [
    Task("Write code", "2024-12-06"),
    Task("Review PR", "2024-12-07"),
    Task("Deploy app", "2024-12-08")
]

numbers = [random.randint(1, 100) for _ in range(20)]
password = generate_password(12)
evens = filter_even_numbers(numbers)

for task in tasks:
    print(f"Task: {task.name}, Completed: {task.completed}")

countdown(5)
