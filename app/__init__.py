from flask import Flask

app = Flask(__name__)
app.secret_key = 'church@2025$secure'

app.secret_key = "yoursecretkey"  # Use a secure random key for production

from app import routes
