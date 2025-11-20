from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <div style="font-family: sans-serif; text-align: center; padding: 50px;">
        <h1>🚀 Proyecto Grupo 7</h1>
        <p>Desplegado exitosamente con Traefik y SSL Automático.</p>
        <p style="color: green;">🔒 Conexión Segura Verificada</p>
        <br>
        <small>Backend: Flask | Proxy: Traefik | Cert: Let's Encrypt</small>
    </div>
    """

if __name__ == "__main__":
    # Flask corre en el puerto 5000 internamente
    app.run(host="0.0.0.0", port=5000)