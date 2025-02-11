from flask import Flask

app= Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Soy team Ubuntu'

if __name__ == '__main__':
    app.run(debug=True)