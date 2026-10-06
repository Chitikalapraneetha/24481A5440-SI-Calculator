from flask import Flask,redirect, request,url_for,render_template,Request


app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to flaskapp<==>routing"

@app.route('/greet/<username>')
def greet(username):
    return f"Hello World,{username}!"
'''
@app.route('/delete/<int:roll>')
def delete_user(roll):
    return redirect(url_for('greet'))
'''
@app.route('/calculate',methods=['GET','POST'])
def si():
    if request.method == 'POST':
        p = float(request.form['p'])
        r = float(request.form['r'])
        t = float(request.form['t'])
        result= (p * r * t) / 100
        total =p+result
        return render_template('index.html', result=result, total=total)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=3500)