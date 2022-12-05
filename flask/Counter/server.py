from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'Carson'

@app.route('/')
def render():
    if 'count' not in session:
        session['count'] = 0
    session['count']+=1
    return render_template('index.html', count=session['count'])
@app.route('/addTwo', methods=['POST'])
def addTwo():
    session['count'] +=1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session['count']=0
    return redirect('/')


if __name__=="__main__":    
    app.run(debug=True)    