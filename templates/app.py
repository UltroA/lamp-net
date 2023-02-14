from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    content = {
        'pic': '1-1.png',
        'hello': 'Ultronet',
        'hi': 'Привет, друг!',
        'me': 'Ultronet - социальная сеть нового поколения',
    }
    return render_template('index.html', **content)


#@app.route('/blog/')
def blog():
    story = [
        {
            'head': 'Как я решил стать програмистом',
            'text': """
    <p>Как-то раз я задумался: "Кем-бы я хотел стать, когда выросту?"</p>
    <p>Я люблю работать за компьютером и "программировать" своего робот LEGO MINDSTORMS EV3.</p>
    <p>В итоге я понял, что лучше мне стать программистом.</p>
    """,
            'pic': 'html.png',
        },
        {
            'head': 'Я и мой канал на YouTube',
            'image': 'youtube.webp'
            ,
            'text': """
    <p>Однажды я решил сделать себе канал на YouTube.</p>
    <p>Скачав приложение в AppStore, я зарегестрировал gmail и создал канал.</p>
    <p>Первым делом я начал снимать ролики-обзоры на LEGO наборы, потом у меня появилась рубрика Let's Play, а теперь я двигаюсь в сторону позновательного контента.</p>
    <p>Мой канал существует и по сей день и называется Ultro.</p>
    """,
        },
        {
            'head': 'Как я занился веб-разроботкой',
            'image': 'wix.png',
            'text': """
    <p>Как-то раз я создавая свою игру задумался: "А как люди смогут скачать мою игру?".</p>
    <p>Я принял решение создать сайт для своей игры. </p>
    <p>Я начал искать в интернете разные ресурсы по созданию сайтов.</p>
    <p>После 30 минут поисков я наткнулся на сайт wix.com и уже в их конструкторе я и создал официальный портал своей игры.</p>
    """
        }
    ]
    dict = {'story': story}

    return render_template('blog.html' ** dict)


#@app.route('/about/')
def about():
    content = {
        '1': """
        <li>E-mail: GGStudio.un@yandex.ru</li>
        """,
        '2': """
        <li>Телефон: +1424950</li>
            """,
        '3': """
        <li>Москва, Тверская улица, дом 13</li>
            """,
        '4': """
        <li><a href="https://www.youtube.com/channel/UC4NqauqoJyupaA_CICGe3AA?view_as=subscriber" target="_blank">Мой YouTube канал</a></li>
            """
    }
    return render_template('about.html' ** content)


names = {
    'matvey': 'Матвей',

}


#@app.route('/secret/')
#@app.route('/secret/<name>')
def hello(name='незнакомец'):
    html = """
        <a href = "/">Привет, незнакомец! Тебе сюда</a>
    """
    return html


def mat(name='artem'):
    mhtml = """
        <p>Привет, Артём!!!!!!!</p>
        <a href = "/">Главная страница </a>
        <a href = "/blog">Блог </a>
        <a href = "/about">Контакты</a>
    """
    return mhtml


def pol(name='polina'):
    phtml = """
    <p>Привет, Полина!</p>
    <a href = "/">Главная страница </a>
    <a href = "/blog">Блог </a>
    <a href = "/about">Контакты</a>
    """
    return phtml

if __name__ == '__main__':
    app.run()