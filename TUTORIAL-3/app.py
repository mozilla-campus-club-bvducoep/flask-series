from flask import render_template
from flask import Flask
from forms import LoginForm


app = Flask(__name__)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

if __name__ == "__main__":
    app.run(debug=True)