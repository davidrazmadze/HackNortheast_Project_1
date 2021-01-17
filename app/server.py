from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/square/', methods=['POST'])
def square():
    stockName = request.form['text']
    isLive = request.form['isLive']

    # num = float(request.form.get('number', 0))
    # square = num ** 2
    # data = {'square': square}
    # data = jsonify(data)
    return "Ok"


if __name__ == '__main__':
    app.run(debug=True)
