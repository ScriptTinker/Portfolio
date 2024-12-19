from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "136aba0cd611a36e9fbcfe5a2c695a88d4e89c33be32a6a0de2f8c2c7beb914e"

from portfolio import routes
