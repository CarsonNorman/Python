from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'Carson'

@app.route('/', methods=['GET'])
def render():     
    session.clear()   
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['Name'] = request.form['name']
    session['Location'] = request.form['locations']
    session['Language'] = request.form['language']
    session['About'] = request.form['about']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('end.html', data=session.items())

if __name__=="__main__":    
    app.run(debug=True)    