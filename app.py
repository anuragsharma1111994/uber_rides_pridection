import numpy as np
from flask import Flask,request,jsonify,render_template 
import pickle
import math


app = Flask(__name__)
model = pickle.load(open('taxi.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features= [int(x) for x in request.form.values()]
    final_featurs=[np.array(int_features)]
    pridection = model.predict(final_featurs)
    

    output = round(pridection[0],2)

    return render_template('index.html',pridection_text="Number of weekly rides should be{}".format(math.floor(output)))

    

if __name__ == "__main__":
    app.run(debug=True)

