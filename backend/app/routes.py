from app import app

@app.route('/')
def index():
    return "Welcome to the NBA Game Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    return "Prediction endpoint"