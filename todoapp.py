from flask import Flask, render_template,request,redirect
import re
import pickle
from os import path

app = Flask(__name__)

if(path.exists('save.p')):
        todo_list=pickle.load(open("save.p","rb"))
else:
    todo_list = {}

@app.route('/')
def table():
    return render_template('table.html',todo_list=todo_list)

@app.route('/submit',methods=['POST'])
def submit():
    
    try:
        task=request.form['task']
        email=request.form['email']
        priority=request.form['priority']
        pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        if(re.search(pattern,email)):
            if(priority=='Low' or priority=="Medium" or priority=="High"):
                todo_list.update({task:(email,priority)})
            else:
                print("Priority is unclear")
        else:
            print('Email invalid')
            
    
        return redirect('/')
            
    except Exception as e:
        print(e)
        return redirect('/')

@app.route('/clear',methods=['POST'])
def clear():
    todo_list.clear()
    pickle.dump(todo_list,open("save.p","wb"))
    return redirect('/')

@app.route('/save',methods=['POST'])
def save():
    pickle.dump(todo_list,open("save.p","wb"))
    
    #print(pickle.load(open("save.p","rb")))
    return redirect('/')
    
@app.route('/delete',methods=['POST'])
def delete():
    
    del todo_list[request.form['del']]
    return redirect('/')

if __name__ == '__main__':
    app.run()
    print(pickle.load(open("save.p","rb")))