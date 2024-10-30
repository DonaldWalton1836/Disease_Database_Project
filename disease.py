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

#Part 1:
#Implementations for the the login in page: including username, password,
#Should be able to add to the data base once a new user is created
#Also you can implement features that deletes a user account from the data base based on username input.

#PART2:
#Creating the funtionalities of the webpage
#being able to click on a certain disease and should display each country info

#Part 3:
#Creating aggreate fruntions that can compare and contrast some statistsics(line or bar graph)
#Implementations are up to you. can select what attributes you want to compare and what countries you want to compare.






