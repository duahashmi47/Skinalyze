import sys
import tensorflow as tf
import numpy as np
from PIL import Image
from ultralytics import YOLO

# Load MobileNetV2 model
skin_type_model = tf.keras.models.load_model("./skin_model_mobilenetv2_finetuned.h5")

# Load YOLOv8 model
skin_issue_model = YOLO("./skin_issue_model.pt")

# Class mappings
SKIN_TYPE_CLASSES = {
    0: "dry",
    1: "normal",
    2: "oily"
}

SKIN_ISSUE_CLASSES = {
    0: "wrinkles",
    1: "redness",
    2: "dryness",
    3: "acne_Level_0",
    4: "acne_Level_1",
    5: "acne_Level_2"
}

# Sample product database
PRODUCT_DATABASE = [
    {"name": "Hydrating Moisturizer", "skin_types": ["dry", "normal"], "concerns": ["dryness", "wrinkles"]},
    {"name": "Oil-Free Cleanser", "skin_types": ["oily"], "concerns": ["acne", "redness"]},
    {"name": "Anti-Redness Serum", "skin_types": ["oily", "normal"], "concerns": ["redness"]},
    {"name": "Wrinkle Repair Cream", "skin_types": ["dry", "normal"], "concerns": ["wrinkles"]},
    {"name": "Lightweight Sunscreen", "skin_types": ["oily", "normal", "dry"], "concerns": ["redness", "dryness", "wrinkles", "acne"]},
    {"name": "Acne Spot Treatment", "skin_types": ["oily"], "concerns": ["acne"]},
    {"name": "Soothing Gel", "skin_types": ["oily", "normal"], "concerns": ["redness", "acne"]},
]

def recommend_products(skin_type, concern, top_n=3):
    """
    Recommend products based on skin type and concern.
    
    Args:
        skin_type (str): 'dry', 'oily', or 'normal'
        concern (str): 'dryness', 'wrinkles', 'redness', or 'acne'
        top_n (int): How many products to return
    
    Returns:
        list of recommended product names
    """
    matches = []

    for product in PRODUCT_DATABASE:
        if skin_type in product["skin_types"] and concern in product["concerns"]:
            matches.append(product["name"])
    
    if not matches:
        return ["No specific product found, try a dermatologist-approved general skincare product!"]

    return matches[:top_n]

# Prediction function
def predict_image(image_path, confidence_threshold=0.25):
    # Load and preprocess image for MobileNetV2
    image = Image.open(image_path).convert('RGB')
    image_resized = image.resize((224, 224))
    image_array = np.array(image_resized) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    # Predict skin type
    skin_type_predictions = skin_type_model.predict(image_array, verbose=0)
    skin_type_idx = int(np.argmax(skin_type_predictions[0]))
    skin_type_confidence = float(np.max(skin_type_predictions[0]))

    skin_type_result = {
        'predicted_class': SKIN_TYPE_CLASSES[skin_type_idx],
        'confidence': skin_type_confidence
    }

    # Predict skin issues using YOLOv8
    yolo_results = skin_issue_model.predict(image_path, conf=confidence_threshold, verbose=False)
    detections = yolo_results[0].boxes  # Get detection boxes

    if detections is not None and detections.shape[0] > 0:
        # Get the box with the highest confidence
        confidences = detections.conf
        best_idx = np.argmax(confidences)
        best_detection = detections[best_idx]

        issue_class_idx = int(best_detection.cls)
        issue_confidence = float(best_detection.conf)

        skin_issue_result = {
            'predicted_class': SKIN_ISSUE_CLASSES[issue_class_idx],
            'confidence': issue_confidence
        }
    else:
        raise ValueError("No face or skin issue detected. Image upload is not allowed.")

    # skin_type = prediction['skin_type']['predicted_class']
    # skin_issue = prediction['skin_issue']['predicted_class']
    # recommended_products = recommend_products(skin_type, skin_issue)
    
    # products_list = []
    # for idx, product in enumerate(recommended_products, 1):
    #     products_list.append(f"{idx}. {product}")
        # print(f"{idx}. {product}")
    # Combine results
    result = {
        'skin_type': skin_type_result,
        'skin_issue': skin_issue_result
        # 'hello': {'some': 'something','hello':"how are you?"}
        # 'recomended_products': products_list
    }
    return result

# Main logic
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No image path provided.")
        sys.exit(1)

    image_path = sys.argv[1]
    prediction = predict_image(image_path)
    skin_type = prediction['skin_type']['predicted_class']
    skin_issue = prediction['skin_issue']['predicted_class']
    prediction['recomended_products'] = recommend_products(skin_type, skin_issue)
    print(prediction)
    # print(type(prediction))
    # print(prediction)
    # try:
    #     # Predict skin type and issue
    #     prediction = predict_image(image_path)
    #     print(prediction)
    #     # Extract skin type and issue
    #     # skin_type = prediction['skin_type']['predicted_class']
    #     # skin_issue = prediction['skin_issue']['predicted_class']

    #     # # Get product recommendations based on skin type and issue
    #     # recommended_products = recommend_products(skin_type, skin_issue)
        
    #     # # Print recommended products
    #     # print("Recommended Products:")
    #     # for idx, product in enumerate(recommended_products, 1):
    #     #     print(f"{idx}. {product}")

    # except ValueError as ve:
    #     print(f"Error: {ve}")
    #     sys.exit(2)  # Custom exit code to tell Node.js it was face issue
    # except Exception as e:
    #     print(f"Error: {e}")
    #     sys.exit(1)  # Other unexpected errors
