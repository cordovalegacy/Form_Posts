from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'supah safe, nothing to see here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template = session['username'], email_on_template = session['email_address'])

@app.route('/users', methods=['POST'])
def create_users():
    print("Post Information")
    print(request.form)
    session['username'] = request.form['name']
    session['email_address'] = request.form['email']
    return redirect('/show')

if __name__ == "__main__":
    app.run(debug=True)