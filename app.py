# import libraries
from flask import Flask, request, url_for, redirect, render_template
import joblib
import numpy as np


app = Flask(__name__)

app.config["SECRET_KEY"] = 'abd3e6fb8a9854dd92a30cfc6dab510d'
clf =  joblib.load(r'C:\Users\Niranjan\Desktop\CSE\Projects\Heart Disease Prediction\heart_log_regr.sav')

# linking of html pages
@app.route('/')
def Home():

    return render_template("Home.html")

@app.route('/Home.html')
def Homepage():
    return render_template("Home.html")


@app.route('/about.html')
def about():
        return render_template("about.html")

@app.route('/helpline.html')
def helpline():
         return render_template("helpline.html")



@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/predict.html', methods=['POST','GET'])
def prediction():
    return render_template("predict.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    
    # # int_features = [x for x in request.form.values()]
    # final = [np.array(int_features)]
    # print(int_features)
    # print(final)
    f1=request.form['age']
    f2=request.form['sex']
    f3=request.form['cp']
    f4=request.form['rbp']
    f5=request.form['cholesterol']
    f6=request.form['fbs']
    f7=request.form['rem']
    f8=request.form['mhr']
    f9=request.form['eia']
    f10=request.form['st']
    f11=request.form['slope']
    f12=request.form['novm']
    f13=request.form['tha']
    # for sex
    if f2 == 'Male':
        f2 == 0 
    else : 
        f2 == 1
    #CP
    if f3 == 'Typical Angina':
        f3 == 1
    elif f3 == 'Atypical Angina':
        f3 == 2
    elif f3 == 'Non-anginal Pain':
        f3 == 3
    else :
        f3 == 4
    #Fasting Blood Sugar
    if f6 == '> 120 mg/dl':
        f6 == 0
    elif f6 == 'true':
        f6 == 1
    else :
        f6 ==2
    #Resting Electrocardiographic Measurment
    if f7 == 'normal' :
        f7 == 0
    elif f7 == 'having ST-T wave abnormality' :
        f7 == 1
    else :
        f7 ==2
    #Exercise Induced Angina
    if f9 == 'Yes' :
       f9 == 0
    else :
        f9 == 1
    #Slope of the peak exercise ST segmnt
    if f11 == 'upsloping' :
        f11 == 0
    elif f11 == 'flat' :
        f11 == 1
    else :
        f11 == 2
    #Thalanasgemia
    if f13 == 'normal' :
        f13 == 0
    elif f13 == ' fixed defect' :
        f13 == 1
    else :
        f13 == 2




    print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13)
    list = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13]
    final=np.array([list])
    
    prediction = clf.predict_proba(final)
    print(prediction)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if output > str(0.5):
        return render_template('project.html', pred='Your Heart is in Danger.\nProbability of heart disease is {}'.format(output), res="Do consult a doctor!!")
    else:
        return render_template('project.html', pred='Your Heart is safe.\n Probability of heart disease is {}'.format(output), res="Eat safe and be healthy..")
        
    


if __name__ == '__main__':

    app.run(debug=True)
    
  