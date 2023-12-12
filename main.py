from flask import Flask, render_template, request
import datetime
import database_access

#from dotenv import load_dotenv
#load_dotenv()

hoje = str(datetime.datetime.today())[:10]
db = database_access.DataBase()


app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/isabela')
def isabela():
	return render_template("isabela.html")


@app.route('/miguel')
def miguel():
	return render_template("miguel.html")


@app.route('/isabela_dados', methods=['POST'])
def isabela_dados():
	peso = request.form['isabela_peso']
	peso = peso if peso != "" else peso == 0
	altura = request.form['isabela_altura']
	altura = altura if altura != "" else altura == 0
	mensagem = request.form['isabela_mensagem']
	registro = (0, hoje, peso, altura, mensagem)
	db.create("ferias_isabela", registro)
	return render_template("anotado.html")


@app.route('/miguel_dados', methods=['POST'])
def miguel_dados():
	peso = request.form['isabela_peso']
	peso = peso if peso != "" else peso == 0
	altura = request.form['isabela_altura']
	altura = altura if altura != "" else altura == 0
	mensagem = request.form['miguel_mensagem']
	registro = (0, hoje, peso, altura, mensagem)
	db.create("ferias_miguel", registro)
	return render_template("anotado.html")



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=1024, debug=True)
