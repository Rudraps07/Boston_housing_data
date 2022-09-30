import pickle
from Flask import Flask,request,app,jsonify,url_for,render_templates
import numpy as np
import pandas as pd

##Load the model
app=Flask(__name__)
model=pickel.load(open('Boston_housing_data\model.pkl','rb'))

@app.route('/') 
def home():
    return render_templates('home.html')
    