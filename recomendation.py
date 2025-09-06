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

# Example usage for testing purpose
if __name__ == "__main__":
    # You can replace this with dynamic input later if needed
    skin_type = "oily"  # Example skin type
    concern = "acne" 
    skin_type2 = "dry"  # Example skin type
    concern2 = "wrinkles"    # Example concern
    recommendations = recommend_products(skin_type, concern)
    products = {}
    products_list = []
    print("Recommended Products:")
    for idx, prod in enumerate(recommendations, 1):
        products_list.append(f"{idx}. {prod}")
    
    products['predicted_products'] = products_list
    
    print(products)

