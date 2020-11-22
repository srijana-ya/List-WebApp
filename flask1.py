from flask import Flask, render_template, redirect, url_for, request

a = []
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', things=a)


@app.route('/test')
def process():
    data = request.args.get("data")
    a.append(data)
    print(a)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=2222)
