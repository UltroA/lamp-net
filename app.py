from flask import Flask, render_template, g
import sqlite3
import API

app = Flask(__name__)

text = ['adsfasdfasdfasdf\n', 'asdfasdfasdf\n', 'adfasdfasdfasdfasdfa\n']

@app.route('/')
def comments():
    comments = [['Shitpost.', 'name', '/static/ТГ.png'],
                ['Some text', 'more text', '/static/Картина.png'],
                ['Kill your family - dekma', 'Лучший исполнитель', '/static/Дед.png'],
                ['I love Minecraft', 'О игре']]
    return render_template('comments.html', comments=comments)


if __name__ == '__main__':
    app.run(port=9000)
