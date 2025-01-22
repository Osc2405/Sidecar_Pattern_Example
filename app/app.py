from flask import Flask
import logging

app = Flask(__name__)

# Configurar logs
logging.basicConfig(filename='/logs/app.log', level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Acceso a la ruta principal.")
    return "Hola, mundo! Revisa los logs para más detalles."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
