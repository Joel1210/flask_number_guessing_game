from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)
app.secret_key = 'This is a secret'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    print(session['number'])

    return render_template('index.html')

@app.route('/myguess', methods= ['POST'])
def guess():
    session['userguess'] =int(request.form['guess'])
    if 'counter' in session: 
        session['counter'] += 1
    else:
       session['counter'] = 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)