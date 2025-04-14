from flask import Flask, request, jsonify, render_template
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
dataset = fetch_california_housing()
AveRooms = dataset.data[:, 1].reshape(-1, 1)
model = LinearRegression()
model.fit(AveRooms, dataset.target)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.post('/predict')
def predict():
    try:
        data = request.get_json()
        feature = data['feature']
        prediction = model.predict([[feature]])
        pre_price = round(prediction[0] * 100000, 2)
        return jsonify({'prediction': pre_price})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)