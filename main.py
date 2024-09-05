from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import json
app = Flask(__name__)
