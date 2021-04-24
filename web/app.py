import json

from flask import Flask, render_template

app = Flask(__name__)


def get_speed_data():
    speed_file = open("./shared/data.json", "r")
    speed_data = speed_file.read()
    speed_file.close()
    return json.loads(speed_data)['data']


@app.route('/')
def get_chart():
    data = get_speed_data()
    labels = [row['time'] for row in data]
    values = [row['speed'] for row in data]
    return render_template("index.html", labels=labels, values=values)


if __name__ == '__main__':
    app.run()
