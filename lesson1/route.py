from flask import Flask
from faker import Faker
from essential_generators import DocumentGenerator
import requests

app = Flask('app')

@app.route("/pull-request")
def pull_request():
    f = open('requirements.txt')
    return f.read()


@app.route("/fake-data")
def fake_data():
    gen = DocumentGenerator()
    fake = Faker()
    return ''.join(f"{fake.name()}  {gen.email()} <br>" for _ in range(100))


@app.route("/hw")
def hw():
    f = open('hw.csv')
    content = f.read()
    content = content.split('\n')[1:]

    height = []
    weight = []

    for row in content:

        try:

            row_split = row.split(',')
            row1 = float(row_split[1])  # height
            row2 = float(row_split[2])  # weight

            height.append(row1)
            weight.append(row2)

        except Exception as e:
            continue

    avg_height = sum(height) / len(height)
    avg_weight = sum(weight) / len(weight)
    return f"Средний рост составил: {avg_height},см. А средний вес: {avg_weight}, кг"


@app.route("/cosmonaut")
def cosmonaut():
    r = requests.get('http://api.open-notify.org/astros.json')
    arr = r.json()
    array_people = arr['people']
    return f"Количество космонавтов: {len(array_people)}"


if __name__ == '__main__':
    app.run()
