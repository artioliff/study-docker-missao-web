from flask import Flask, render_template
import random

# Aqui criamos o nosso aplicativo Flask (o cérebro da nave)
app = Flask(__name__)

# Esta função gera o status atual da nave
def obter_status_nave():
    destinos = ["Marte", "Lua", "Estação Espacial", "Nebulosa de Órion"]
    return {
        "combustivel": random.randint(50, 100),
        "temperatura": random.randint(20, 30),
        "destino": random.choice(destinos)
    }

# Rota Principal: É como a porta de entrada da nave.
# Quando alguém acessar o site, esta função será chamada.
@app.route('/')
def painel_controle():
    status = obter_status_nave()
    # Enviamos as informações para o arquivo HTML desenhar a tela
    return render_template('index.html', status=status)

# Iniciando os motores!
if __name__ == '__main__':
    # host='0.0.0.0' significa que a nave aceita conexões de qualquer lugar (necessário para o Docker)
    app.run(host='0.0.0.0', port=5000)
