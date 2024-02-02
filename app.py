from flask import Flask, render_template

elitefc = Flask(__name__)

@elitefc.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    elitefc.run(debug=True)