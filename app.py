from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the model
#model = tf.keras.models.load_model("./skin_type_model.keras")
model = tf.keras.models.load_model("./skin_model_mobilenetv2_finetuned.h5")

# Define class names
CLASS_NAMES = {
    0: "dry",
    1: "normal",
    2: "oily"
}

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
    # Get the image file from the request
        file = request.files['file']
        image = Image.open(file).convert('RGB')
        image = image.resize((224, 224))  # Resize to model input size
        image = np.array(image) / 255.0  # Normalize
        image = np.expand_dims(image, axis=0)  # Add batch dimension

    # Make prediction
        predictions = model.predict(image)
        predicted_class = np.argmax(predictions[0])  # Get the class with the highest probability

    # Get the class name
        class_name = CLASS_NAMES[predicted_class]

    # Return the response with class name
        response = {
            'predicted_class': class_name,
            'confidence': float(np.max(predictions[0]))
        }
        return jsonify(response)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': 'An error occurred while making the prediction'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
