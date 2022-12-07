from flask import Flask, redirect,request, render_template as render
app = Flask(__name__)  

from  flask_app.controllers.user_controller import User

