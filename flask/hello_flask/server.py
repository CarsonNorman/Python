from flask import Flask, render_template
app = Flask(__name__)   
@app.route('/')         
def render_play():
    for i in range(int(3)):
        return render_template('box.html', x=3)
@app.route('/<x>')         
def render_box(x):
        return render_template('box.html', x=int(x), color='blue')
@app.route('/<x>/<color>')         
def render_box_color(x, color):
        return render_template('box.html', x=int(x), color=color)

if __name__=="__main__":    
    app.run(debug=True)    

