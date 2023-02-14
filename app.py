# import flask-needed from flask library
from flask import Flask, render_template, g
# import db library
import sqlite3
# App's API (additional script for using less code in main file)
import API

app = Flask(__name__)

# Routes on website
@app.route('/')
def comments():
    # main page with posts
    # we need to make more mobile optimization
    comments = [['Shitpost.', 'name', '/static/ТГ.png'],
                ['Some text', 'more text', '/static/Картина.png'],
                ['Kill your family - dekma', 'Лучший исполнитель', '/static/Дед.png'],
                ['I love Minecraft', 'О игре']]
    return render_template('comments.html', comments=comments)


# TODO: work with database

# main site working cycle
if __name__ == '__main__':
    app.run(port=9000)
