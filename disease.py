from flask import Flask, render_template, request , redirect, url_for, session, jsonify
import mysql.connector
import hashlib
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import mpld3
import numpy as np
matplotlib.use('Agg') #needed for graph to work
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' 


mydb = mysql.connector.connect(
            host="sql5.freesqldatabase.com",
            port="3306",
            user="sql5736933",
            password="njn8cESVbV",
            database="sql5736933"
        )
