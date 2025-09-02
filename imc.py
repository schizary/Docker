from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('imc_calc.html')


@app.route('/calcular_imc', methods=['POST'])
def calcIMC():
    altura = float(request.form['txt_altura'])
    peso = float(request.form['txt_peso'])
    imc = peso / (altura * altura)
    return render_template('imc_calc.html', res_imc = imc)



@app.route('/calcular_imc_post', methods=['POST'])
def calcular_imc_post():
    altura = float( request.form['txt_altura'])
    peso   = float( request.form['txt_peso'] )
    calculo = peso / altura ** 2
    if (calculo < 18.5):
        classificacao = 'MAGREZA'
    if (calculo >= 18.5 and calculo <= 24.9):
        classificacao = 'NORMAL'
    if (calculo >= 25 and calculo <= 29.9):
        classificacao = 'SOBREPESO'
    if (calculo >= 30 and calculo <= 39.9):
        classificacao = 'OBESIDADE'       
    if (calculo >= 40 ):
        classificacao = 'OBESIDADE GRAVE' 
    return  render_template('imc_calc.html', IMC=f'{calculo:.2f}', classificado = classificacao)


@app.route('/calcular_imc_get', methods=['GET'])
def calcular_imc_get():
    args = request.args
    altura = float( args.get('txt_altura'))
    peso   = float( args.get('txt_peso'))
    calculo = peso / altura ** 2
    if (calculo < 18.5):
        classificacao = 'MAGREZA'
    if (calculo >= 18.5 and calculo <= 24.9):
        classificacao = 'NORMAL'
    if (calculo >= 25 and calculo <= 29.9):
        classificacao = 'SOBREPESO'
    if (calculo >= 30 and calculo <= 39.9):
        classificacao = 'OBESIDADE'       
    if (calculo >= 40 ):
        classificacao = 'OBESIDADE GRAVE' 
    return  render_template('imc_calc.html', IMC=str(f'{calculo:.2f}'), classificado=classificacao)

app.run(port=80, host='0.0.0.0')
    