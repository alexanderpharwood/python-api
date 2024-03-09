from flask import Flask
from Router import Router

class Server:
  def __init__(self):
    self.app = Flask(__name__)
    self.router = Router(self.app)

  def boot(self):
    self.router.boot()
    self.app.run(host="localhost", port=8000, debug=True)