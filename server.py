from flask import Flask, request, jsonify, Response
import util

app= Flask(__name__)
#expose http endpoint-->
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods = [ 'POST'])
def predict_home_price():
    #all inputs in request.form format - http requests
    total_sqft= float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response: = jsonify({
        'estimated_price' : util.get_estimated_price(location,total_sqft,bhk,bath)
    })
#2 routines - 1st - return the locations in blr --- in UI dropdown for all the locations

if __name__=="__main__":
    print("Starting Python Flask Server For Real Estate Price Prediction....")
    app.run()