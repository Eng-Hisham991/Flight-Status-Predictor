from flask import Flask, render_template, redirect, request
import pandas as pd
import numpy as np
import joblib


# Create an instance of Flask
application = app = Flask(__name__)

model = joblib.load('RFmodel.sav')
# def get_value(value): 
#     for key, value in dest.items(): 
#         if key == key: 
#             return key

# Route to render index.html template 
@app.route("/")
@app.route("/index")
def info():
    nm1 = {'YV':'Mesa Airlines', 'EV':'ExpressJet','AS':'Alaska Airlines',
                'UA':'United Airlines','YX': 'Republic Airways','AA': 'American Airlines', 
                'F9':'Fronteir Airlines','9E':'Endeavor Air','NK':'Spirit Airlines','OO':'SkyWest Airlines',
                'DL':'Delta Airlines',"B6":'JetBlue',"OH":"PSA Airlines"}
    
    lines = list(nm1.values())
    df = pd.read_csv('trial1.csv')
    cats = df['DEST_AIRPORT'].unique().tolist()
    return render_template("index.html", lines = lines, cats = cats)

@app.route("/", methods=["GET", "POST"])
def home():
    output_message = ""
    feature_names = ['AIRLINE', 'DEST_AIRPORT', 'Delays', 'YEAR', 'MONTH']
    df= pd.read_csv('trial1.csv')
    if request.method == "POST":
        AIRLINE5 = request.form["AIRLINE"]
        DEST_AIRPORT5 = request.form["Dest. Airport"]
        Delays = float(request.form["Delays"])
        YEAR = float(request.form["YEAR"])
        MONTH = float(request.form["MONTH"])

    # Convert AIRLINE5 & DEST_AIRPORT5 to numbers
    b = df['AIRLINE'].unique().tolist()
    c = df['AIRLINE_P'].unique().tolist()
    e = df['DEST_AIRPORT'].unique().tolist()
    f = df['DEST_AIRPORT_P'].unique().tolist() 
    airport = {} 
    for key in b: 
        for value in c: 
            airport[key] = value 
            c.remove(value) 
            break 
    dest = {}
    for key in e: 
        for value in f: 
            dest[key] = value 
            f.remove(value) 
            break  
    abrv = {'Mesa Airlines':'YV', 'ExpressJet':'EV','Alaska Airlines':'AS',
        'United Airlines':'UA', 'Republic Airways':'YX', 'American Airlines':'AA', 
        'Fronteir Airlines':'F9','Endeavor Air':'9E','Spirit Airlines':'NK','SkyWest Airlines':'OO',
        'Delta Airlines':'DL','JetBlue':'B6','PSA Airlines':'OH'}
    airl = abrv[f'{AIRLINE5}']
    dest2 = dest[f'{DEST_AIRPORT5}']
    AIRLINE = float(airport[f'{airl}'])
    DEST_AIRPORT = float(dest2)

    # data must be converted to df with matching feature names before predict
    data = pd.DataFrame(np.array([[AIRLINE, DEST_AIRPORT, Delays, YEAR, MONTH]]), columns=feature_names)
    result = model.predict(data)
    if result == 1:
        output_message = "Congratulation, There is no Delay. Have a safe trip."
    else:
        output_message = "Oh No, there is a delay. Consider all the options you have"
    
    return render_template("index.html", message = output_message)
@app.route("/data")
def data():
  df= pd.read_csv('trial1.csv')
  return df.to_csv(index=False)  

if __name__ == "__main__":
    application.run(debug=True)
