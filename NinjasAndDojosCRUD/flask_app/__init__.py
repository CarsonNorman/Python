from flask import Flask, redirect, request, render_template as render
app= Flask(__name__, template_folder='static/templates')

from flask_app.controllers.dojos_controller import Dojo
from flask_app.controllers.ninjas_controller import Ninja