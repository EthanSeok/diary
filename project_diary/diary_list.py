from flask import Flask,render_template,request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1> 나의 일기장</h1>'

@app.route('/')
def read_file():
    document_path = os.getcwd()+'diary_text.txt'
    document = open(document_path, 'r')
    return '<h2>' document '</h1>'

host_addr = '0.0.0.0'
port_num = '8080'

if __name__=='__main__':
    app.run(host=host_addr,port=port_num)