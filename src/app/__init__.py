from flask import Flask

app = Flask('stargazers')

from src.app import views