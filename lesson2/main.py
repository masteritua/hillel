from flask import Flask
from flask import request
import sqlite3


def connect(query):
    conn = sqlite3.connect("chinook.db")
    cursor = conn.cursor()
    exec = cursor.execute(query)  # Выполнение запроса
    return exec.fetchall()


app = Flask('app')


@app.route("/generate")
def generate():  # Генерирование случайный чисел
    import random
    import string
    return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(10)])


@app.route("/filter")
def filter():
    city = request.args['city']
    state = request.args['state']
    result = connect(f"SELECT * FROM customers WHERE city='{city}' AND state='{state}'")
    return str(result)


@app.route("/unique-name")
def unique_name():
    result = connect("SELECT DISTINCT FirstName FROM customers")
    return str(result)


@app.route("/getdata")
def getdata():
    result = connect("SELECT SUM(UnitPrice * Quantity) as TotalProfit FROM invoice_items")
    return str(result)


if __name__ == '__main__':
    app.run()
