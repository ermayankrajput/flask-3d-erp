from flask_sqlalchemy import SQLAlchemy
from flask import Flask, abort, jsonify, request
import psycopg2
# from app import app
# db = SQLAlchemy()

hostname = "localhost"
database = "three_erp"
username = "postgres"
pwd = "password"
port_id = "5432"
con  = None
cur = None

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
    

    cur = conn.cursor()

    create_script = '''CREATE TABLE IF NOT EXISTS  quote (

                        id           int PRIMARY KEY,
                        file_name    text NOT NULL,
                        status       INTEGER DEFAULT 1 NOT NULL,
                        created_at   date NOT NULL,
                        updated_at   date NOT NULL)'''
    

    cur.execute(create_script)


    conn.commit()
except Exception as error:
    print(error)



finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


# class three_erp(db.Model):
#     __tablename__ = 'quote'
#     id = db.Column(db.Integer, primary_key = True)
#     file_name = db.Column(db.Text(), nullable = False)
#     status = db.Column(db.Integer(), nullable = False)
#     created_at = db.Column(db.Integer(), nullable = False)
#     updated_at = db.Column(db.Integer(), nullable = False)
