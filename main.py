from flask import Flask,request,render_template,redirect,url_for
import pickle,gzip
import joblib
import numpy as np
from pymongo import MongoClient
from flask_pymongo import PyMongo


model = joblib.load('Thyroid_model.pkl')

app=Flask(__name__)

app.config['MONGO_DBNAME']='mydb'
app.config["MONGO_URI"]='mongodb+srv://kalpuG:12345@mydb.ydqwp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

mongo=PyMongo(app)

@app.route('/')

def home():
    online_uses=mongo.db.users.find({"online":True})
    return render_template('index.html',online_uses=online_uses)

@app.route('/predict',methods=['POST'])

def predict():
    db = mongo.db.Results_app

    Age=float(request.form.get('age',False))
    Sex= float(request.form.get('sex',False))
    Level_thyroid_stimulating_hormone= float(request.form.get('TSH',False))
    Total_thyroxine_TT4= float(request.form.get('TT4',False))
    Free_thyroxine_index=float(request.form.get('FTI',False))
    On_thyroxine= float(request.form.get('on_thyroxine',False))
    On_antithyroid_medication= float(request.form.get('on_antithyroid_medication',False))
    Goitre= float(request.form.get('goitre',False))
    Hypopituitary = float(request.form.get('hypopituitary', False))
    Psychological_symptoms = float(request.form.get('psych', False))
    T3_measured= float(request.form.get('T3_measured',False))

    values=({"age":Age,"sex":Sex,"TSH":Level_thyroid_stimulating_hormone,
            "FTI":Free_thyroxine_index,"on_thyroxine":On_thyroxine,
            "on_antithyroid_medication":On_antithyroid_medication,
            "goitre":Goitre,"hypopituitary":Hypopituitary,
            "psych":Psychological_symptoms,"T3_measured":T3_measured})
    my_data=db.insert_one(values)

    arr=np.array([[Age,Sex,Level_thyroid_stimulating_hormone,Total_thyroxine_TT4,Free_thyroxine_index,
    On_thyroxine,On_antithyroid_medication,Goitre,Hypopituitary,Psychological_symptoms,T3_measured]])
    pred=model.predict(arr)


    if pred==0:
        res_Val="Compensated hypothyroid"
    elif pred==1:
        res_Val="No thyroid"
    elif pred==2:
        res_Val='Primary hypothyroid'
    elif pred==3:
        res_Val='Secondary hypothyroid'


    return render_template('index.html',prediction_text='Patient has {}'.format(res_Val),my_data=my_data)


if __name__=='__main__':
    app.run(debug=True)
