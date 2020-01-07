from flask import Flask, render_template, request
from forms import GetData

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t/harshal'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/app1", methods=['GET', 'POST'])
def app1():
    form = GetData()
    if request.method == 'POST' and form.validate_on_submit():
        print(form.username.data)
        return render_template('app1.html', form=form, result=True, confidence='95%', model="Resnet50")
    return render_template('app1.html', form=form)


@app.route("/app2", methods=['GET', 'POST'])
def app2():
    form = GetData()
    if request.method == 'POST' and form.validate_on_submit():
        print(form.username.data)
        return render_template('app2.html', form=form, result=True, confidence='95%', model="Resnet50")
    return render_template('app2.html', form=form)


@app.errorhandler(404)
def error(e):
    print(e)
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
