from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "bc8f00971e40640add44ac54e5d342f7"


@app.route('/', methods=["GET", "POST"])
def index():
    clima = None
    erro = None
    if request.method =="POST":
        cidade = request.form.get("cidade")
        if cidade:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
            try:
                res = requests.get(url)
                if res.status_code == 200:
                    clima = res.json()
                else:
                    erro = "cidade não encontrada!"
            
            except requests.exceptions.RequestException:
                erro = "Erro ao conectar ao serviço."
    return render_template("index.html", clima=clima, erro=erro)
    

if __name__ == "__main__":
    app.run(debug=True)
