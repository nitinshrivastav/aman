import pandas as pd
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def fjk():
    return render_template('index.html')
    #jkdkjdkjkjd
app.run(debug=True)