from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load data from JSON file
def load_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "data.json file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}

@app.route('/')
def home():
    return jsonify({
        "message": "Car Makes and Models API",
        "endpoints": {
            "/api/brands": "Get all car brands and models",
            "/api/brands/<brand_name>": "Get models for a specific brand",
            "/api/count": "Get statistics about brands and models"
        }
    })

@app.route('/api/brands', methods=['GET'])
def get_all_brands():
    """Get all car brands and their models"""
    data = load_data()
    return jsonify(data)

@app.route('/api/brands/<string:brand_name>', methods=['GET'])
def get_brand_models(brand_name):
    """Get models for a specific brand"""
    data = load_data()
    
    if "error" in data:
        return jsonify(data), 500
    
    # Search for the brand (case-insensitive)
    for brand in data.get('brands', []):
        if brand['name'].lower() == brand_name.lower():
            return jsonify(brand)
    
    return jsonify({"error": f"Brand '{brand_name}' not found"}), 404

@app.route('/api/count', methods=['GET'])
def get_statistics():
    """Get statistics about the data"""
    data = load_data()
    
    if "error" in data:
        return jsonify(data), 500
    
    brands = data.get('brands', [])
    total_brands = len(brands)
    total_models = sum(len(brand.get('models', [])) for brand in brands)
    
    return jsonify({
        "total_brands": total_brands,
        "total_models": total_models,
        "brands": [brand['name'] for brand in brands]
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
