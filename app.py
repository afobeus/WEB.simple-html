from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def root():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br>
Человечеству мала одна планета.<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
И начнем с Марса!<br>
Присоединяйся!"""


@app.route("/image_mars")
def image_mars():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1> Жди нас, Марс! </h1>
    <img src="{url_for('static', filename="images/mars.jpg")}">
    <p> Вот она какая, красная планета </p>
</body>
</html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <link rel="stylesheet", href="{url_for('static', filename="css/style.css")}">
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1> Жди нас, Марс! </h1>
            <img src="{url_for('static', filename="images/mars.jpg")}">
            <div class="alert alert-dark" role="alert">
            Человечество вырастает из детства.
            </div>
            <div class="alert alert-success" role="alert">
            Человечеству мала одна планета.
            </div>
            <div class="alert alert-secondary" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
            </div>
            <div class="alert alert-warning" role="alert">
            И начнем с Марса!
            </div>
            <div class="alert alert-danger" role="alert">
             Присоединяйся!
            </div>
        </body>
        </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet"
                      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                      integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                      crossorigin="anonymous">
                <link rel="stylesheet" href="{url_for('static', filename="css/style.css")}">
                <title>Отбор астронавтов</title>
            </head>
            <body>
                <h1>Анкета претендента</h1>
                <p>на участие в миссии</p>
                <div>
                    <form class="login_form" method="post">
                        <input type="text" class="form-control" placeholder="Введите фамилию" name="surname">
                        <input type="text" class="form-control" placeholder="Введите имя" name="name">
                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                        <label for="classSelect">Какое у вас образование?</label>
                        <select class="form-control" id="classSelect" name="graduation">
                            <option>Начальное</option>
                            <option>Среднее</option>
                            <option>Высшее</option>
                        </select>
                        <label for="form-group">Какие у вас есть профессии?</label>
                        <div id="form-group">
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="engineer1" name="profession">
                                <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                            </div>
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="pilot" name="profession">
                                <label class="form-check-label" for="acceptRules">Пилот</label>
                            </div>
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="engineer2" name="profession">
                                <label class="form-check-label" for="acceptRules">Инженер жизнеобеспечения</label>
                            </div>
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="climate" name="profession">
                                <label class="form-check-label" for="acceptRules">Климатолог</label>
                            </div>
                            <div class="form-group form-check">
                                <input type="checkbox" class="form-check-input" id="biologist" name="profession">
                                <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="form-check">Укажите пол</label>
                            <div class="form-check" id="form-check">
                                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                <label class="form-check-label" for="male">
                                    Мужской
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                <label class="form-check-label" for="female">
                                    Женский
                                </label>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                        </div>
                        <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="ready" name="accept">
                            <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                        </div>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </div>
            </body>
            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['graduation'])
        print(request.form['about'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route("/choice/<planet_name>")
def choice(planet_name):
    texts = {"марс": ["Эта планета близка к Земле", "На ней много ресурсов", "На ней есть атмосфера"],
             "земля": ["Это наша планета", "На ней есть крутые ресурсы", "И ещё на ней есть я"]}
    if planet_name.lower() in texts:
        text = texts[planet_name]
    else:
        text = ["Если вы это видите,", "то это значит, что", "мне было лень"]
    return f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1> Моё предложение: {planet_name} </h1>
            <h2> {text[0]} </h2>
            <div class="alert alert-success" role="alert">
            {text[1]}
            </div>
            <div class="alert alert-secondary" role="alert">
            {text[2]}
            </div>
        </body>
        </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <title>Результаты</title>
        </head>
        <body>
            <h1> Результаты отбора </h1>
            <h2> Претендента на участие в миссии {nickname}: </h2>
            <div class="alert alert-success" role="alert">
            Поздравляем! Ваш рейтинг после {level} этапа отбора
            </div>
            <h3> составляет {rating} </h3>
            <div class="alert alert-secondary" role="alert">
            Желаем удачи!
            </div>
        </body>
        </html>"""


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
