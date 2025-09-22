from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello, World!'
    return render_template("Lesson_05_TemplatesRendering/home.html")

if __name__ == '__main__':
    app.run(debug=True, port="5050")