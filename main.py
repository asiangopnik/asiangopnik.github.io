from flask import Flask, render_template, url_for, redirect, session, abort, escape, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('../index.html')


@app.route('/word/<word>')
def word(word):
    return render_template('words.html', word=word)


if __name__ == '__main__':
    app.run()
