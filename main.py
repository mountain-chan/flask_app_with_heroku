from flask import Flask, Config

app = Flask(__name__)


class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    DEBUG_TB_ENABLED = False
    HOST = '0.0.0.0'
    TEMPLATES_AUTO_RELOAD = False


app.config.from_object(ProdConfig)


@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run(host='0.0.0.0', port=5012)
