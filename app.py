from flask import Flask , request , redirect , url_for , render_template
from sqlConnector import show,ins,showByPriority
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/page1', methods=['GET','POST'])
def page1():

    res = showByPriority(8)
    
    
    return render_template('ui.html',tasks=res)

@app.route('/page2', methods=['GET','POST'])
def page2():

    res = showByPriority(6)
    
    
    return render_template('ui.html',tasks=res)

@app.route('/page3', methods=['GET','POST'])
def page3():

    res = showByPriority(4)
    
    
    return render_template('ui.html',tasks=res)

@app.route('/page4', methods=['GET','POST'])
def page4():

    res = showByPriority(0)
    
    
    return render_template('ui.html',tasks=res)

@app.route('/page5', methods=['GET','POST'])
def page5():
    return {}



@app.route('/input')
def input():
    return render_template('input.html')


@app.route('/plan',methods=['POST'])
def plan():

    task = request.form['task']
    priority = request.form['priority']
    ins(task,int(priority))
    
    
    res = show()
    
    
    return render_template('planner.html',tasks=res)

if __name__ == '__main__':
    app.run(debug=True)