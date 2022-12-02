from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'Carson'

@app.route('/', methods=['GET'])
def render():        
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['Name'] = request.form.get('name')
    session['Location'] = request.form.get('locations')
    session['Language'] = request.form.get('language')
    session['About'] = request.form.get('about')
    return render_template('end.html', data=session.items())

if __name__=="__main__":    
    app.run(debug=True)    