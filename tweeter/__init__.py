from flask import Flask
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)
app.debug = True
import views