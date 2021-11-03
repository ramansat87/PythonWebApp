from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World Welcome to Azure Python World, Welcome to the Azure DevOps and this is a sample Python Web App running on Flask Framework!"

