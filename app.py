from flask import Flask

app= Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Soy team Ubuntu'

@app.route('/alumnos')
def alumnos():
    return 'Aqui estan los datos de alumnos'


if __name__ == '__main__':
    app.run(debug=True)