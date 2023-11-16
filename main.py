from flask import Flask,render_template,redirect,url_for
from forms import ProfileForm,EntryForm
from game import Game


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ezpz'

g = Game()

@app.route("/", methods=['get', 'post'])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        name = form.name.data
        return redirect(url_for('game',name=name))

    return render_template("index.html", form=form)

@app.route("/game/<string:name>",methods = ["get","post"])
def game(name):
    if g.times==0:
        g.times+=1
        message = g.to_display
        form = ProfileForm()
        return render_template("game.html", form=form,message=message)
    form = ProfileForm()
    if form.validate_on_submit():
        direction = form.data["direction"]
        steps = form.data["steps"]
        message = g.move_multiple(direction,steps)
        return render_template("game.html", form=form, message = message)

    return render_template("game.html", form=form)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)