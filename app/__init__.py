"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch131vgrddl13a546ckg-a.oregon-postgres.render.com",
        database="todo_tnwh",
        user="todo_tnwh_user",
        password="LgOQrjeW782zov2YJ6OCkVLRGcdr1wVD")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
