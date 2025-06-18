from flask import Flask

app = Flask(__name__)
app.secret_key = 'church@2025$secure'

from app import routes
