import flask
import sqlite3
import os
from funcoes import veri_login, efetuando_cadastro 
from flask import Flask, make_response, render_template, request, redirect


app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method =='POST':
        return redirect('verificar_login')
    return render_template('index.html')     
  
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro', methods=['POST',  'GET'])
def cadastro():
    if request.method =='POST':
        nome = request.form['nome']
        email = request.form['email']
        verificaçao =  veri_login(nome, email)
        
        
        if verificaçao == True:
            mensagem = "O e-mail {} já está cadastrado no banco de dados.".format(email)
            response = make_response(render_template('login.html', mensagem=mensagem))
            return response
        return redirect('verificar_cadastro')
    return render_template('login.html')

@app.route('/verificar_cadastro', methods=['POST',  'GET'])
def verificar_cadastro():
    if request.method =='POST':
        nome = request.form['nome']
        email = request.form['email']
        efetuando_cadastro(nome,email)
    return redirect('/')


@app.route('/verificar_login', methods=['POST'])
def verificar_login():
    username = request.form['username']
    email = request.form['email']
    verificaçao = veri_login(username, email)
    if verificaçao == True:
        return redirect('/usuario')
    else:
        mensagem = "O e-mail {} não está cadastrado no banco de dados.".format(email)
        response = make_response(render_template('index.html', mensagem=mensagem))
        return  response
@app.route('/usuario')
def usuario():
    return   render_template('usuario.html')    
   

port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=port)