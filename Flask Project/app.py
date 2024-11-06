from urllib import request
from flask import *
from flask import jsonify
import pickle
import numpy as np
#load_model_DT=pickle.load(open('static/Sav_Models/DT_model.sav','rb'))
#load_model_KNN=pickle.load(open('static/Sav_Models/KNN_model.sav','rb'))
load_model_XGB=pickle.load(open('Flask Project/static/Sav_Models/gb_model086.sav','rb'))

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data')
def pd():
    return render_template("pd.html")

@app.route('/predict',methods=['POST'])
def predict():
        MDVP_Fo = float(request.form['MDVP_Fo'])
        MDVP_Fhi = float(request.form['MDVP_Fhi'])
        MDVP_Flo = float(request.form['MDVP_Flo'])
        mdvp_jitter_percent = float(request.form['mdvp_jitter_percent'])
        mdvp_jitter_abs = float(request.form['mdvp_jitter_abs'])
        mdvp_rap = float(request.form['mdvp_rap'])
        mdvp_ppq = float(request.form['mdvp_ppq'])
        jitter_ddp = float(request.form['jitter_ddp'])
        jitter_ddp = float(request.form['mdvp_shimmer'])
        mdvp_shimmer_db = float(request.form['mdvp_shimmer_db'])
        shimmer_apq3 = float(request.form['shimmer_apq3'])
        shimmer_apq5 = float(request.form['shimmer_apq5'])
        mdvp_apq = float(request.form['mdvp_apq'])
        shimmer_dda = float(request.form['shimmer_dda'])
        nhr = float(request.form['nhr'])
        hnr = float(request.form['hnr'])
        rped=float(request.form['rped'])
        dfa=float(request.form['dfa'])
        spread1=float(request.form['spread1'])
        spread2=float(request.form['spread2'])
        df=float(request.form['df'])
        ppe=float(request.form['ppe'])

        input_data = (MDVP_Fo,MDVP_Fhi,MDVP_Flo,mdvp_jitter_percent,mdvp_jitter_abs,mdvp_rap,mdvp_ppq,jitter_ddp,jitter_ddp,mdvp_shimmer_db,shimmer_apq3,shimmer_apq5,mdvp_apq,shimmer_dda,nhr,hnr,rped,dfa,spread1,spread2,df,ppe)

        # changing input data to a numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the numpy array
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        # standardize the data
        #std_data = scaler.transform(input_data_reshaped)

        #prediction_DT = load_model_DT.predict(input_data_reshaped)
        #print(prediction_DT)
        #prediction_KNN = load_model_KNN.predict(input_data_reshaped)
        #print(prediction_KNN)
        prediction_XGB = load_model_XGB.predict(input_data_reshaped)
        print(prediction_XGB)
        #if prediction_DT[0] == 0 and prediction_KNN[0]==0:
            #return'KNN: This person does not have parkinson disease \n DT: This person does not have parkinson disease'
        #elif prediction_DT[0] == 0 and prediction_KNN[0]==1:
            #return'KNN: This person does not have parkinson disease \n DT: This person has parkinson disease'
        #elif prediction_DT[0] == 1 and prediction_KNN[0]==0:
            #return'KNN: This person has parkinson disease \n DT: This person does not have parkinson disease'
        #elif prediction_DT[0] == 1 and prediction_KNN[0]==1:
             #return'KNN: This person has parkinson disease \n DT: This person has parkinson disease'
        if prediction_XGB[0]==0:
             return 'XGB: This person does not have parkinson disease'
        elif  prediction_XGB[0]==1:
             return 'XGB: This person have parkinson disease'




if __name__ =='__main__':
    app.run(port=3000,debug=True)