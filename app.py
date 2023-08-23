# Valentine’s Day
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        boy_birthday = datetime.strptime(request.form['boy_birthday'], '%Y-%m-%d')
        girl_birthday = datetime.strptime(request.form['girl_birthday'], '%Y-%m-%d')
        anniversary = datetime.strptime(request.form['anniversary'], '%Y-%m-%d')
        boy_area = request.form['boy_area']
        girl_area = request.form['girl_area']
        today = datetime.today()
        anniversary_days = (today - anniversary).days
        return render_template('message.html',
                               boy_birthday=boy_birthday,
                               girl_birthday=girl_birthday,
                               anniversary=anniversary,
                               anniversary_days=anniversary_days,
                               boy_area=boy_area,
                               girl_area=girl_area)
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
