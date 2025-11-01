# Car Makes and Models API

A simple Flask REST API that provides access to car makes and models data. This API is designed to be deployed on Render using Gunicorn.

## Features

- Get all car brands and their models
- Search for specific car brands
- Get statistics about the dataset
- CORS enabled for cross-origin requests
- Production-ready with Gunicorn

## API Endpoints

### 1. Home / API Info
```
GET /
```
Returns information about available endpoints.

**Response:**
```json
{
  "message": "Car Makes and Models API",
  "version": "2.0",
  "endpoints": {
    "/api/brands": "Get all car brands and models with years",
    "/api/brands/<brand_name>": "Get models for a specific brand",
    "/api/brands/search?model=<name>&year=<year>": "Search for models by name or year",
    "/api/count": "Get statistics about brands and models"
  }
}
```

### 2. Get All Brands
```
GET /api/brands
```
Returns all car brands and their models with year information.

**Response:**
```json
{
  "brands": [
    {
      "name": "Toyota",
      "models": [
        {
          "model_name": "Camry",
          "year": 1997
        },
        {
          "model_name": "Corolla",
          "year": 1995
        }
      ]
    }
  ]
}
```

### 3. Get Specific Brand
```
GET /api/brands/<brand_name>
```
Returns models for a specific brand (case-insensitive).

**Example:**
```
GET /api/brands/toyota
```

**Response:**
```json
{
  "name": "Toyota",
  "models": [
    {
      "model_name": "Camry",
      "year": 1997
    },
    {
      "model_name": "Corolla",
      "year": 1995
    }
  ]
}
```

### 4. Search Models
```
GET /api/brands/search?model=<name>&year=<year>
```
Search for models by name or year. Both parameters are optional.

**Examples:**
```
GET /api/brands/search?model=camry
GET /api/brands/search?year=2020
GET /api/brands/search?model=corolla&year=1995
```

**Response:**
```json
{
  "count": 2,
  "results": [
    {
      "brand": "Toyota",
      "model_name": "Camry",
      "year": 1997
    },
    {
      "brand": "Lexus",
      "model_name": "Camry",
      "year": 2002
    }
  ]
}
```

### 5. Get Statistics
```
GET /api/count
```
Returns statistics about the dataset including year range.

**Response:**
```json
{
  "total_brands": 95,
  "total_models": 2450,
  "year_range": {
    "min": 1980,
    "max": 2025
  },
  "brands": ["Abarth", "Aito", "Alfa Romeo", ...]
}
```

## Local Development

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Using Gunicorn (Production)
```bash
gunicorn app:app
```

## Deployment to Render

### Method 1: Using Render Dashboard

1. Create a new account on [Render](https://render.com)

2. Click "New +" and select "Web Service"

3. Connect your repository or upload your code

4. Configure the service:
   - **Name:** car-makes-models-api (or your preferred name)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free (or your preference)

5. Click "Create Web Service"

### Method 2: Using render.yaml

Create a `render.yaml` file in your repository root:

```yaml
services:
  - type: web
    name: car-makes-models-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

Then connect your repository to Render.

## Environment Variables

- `PORT`: The port number the app will run on (automatically set by Render)

## Project Structure

```
car makes and models/
│
├── app.py                 # Main Flask application
├── data.json             # Car brands and models data
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Technologies Used

- **Flask**: Web framework
- **Gunicorn**: WSGI HTTP Server
- **Flask-CORS**: Cross-Origin Resource Sharing support

## Data Structure

The API serves data from `data.json` which contains 95+ car brands with their respective models and year information. Each model entry includes:
- `model_name`: The name of the car model
- `year`: The year the model was introduced or available

## Error Handling

The API includes proper error handling for:
- 404: Endpoint or brand not found
- 500: Internal server errors
- Invalid JSON data

## License

This project is open source and available for personal and commercial use.

## Support

For issues or questions, please create an issue in the repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Made with ❤️ using Flask and Python**
