# Iris Species Prediction API with FastAPI

This project provides a machine learning-powered API to predict the species of an Iris flower based on its sepal and petal measurements. It is built using FastAPI for high performance and containerized with Docker for easy, cross-platform deployment. This project was created to fulfill the AI Engineering Internship Assignment.

---

## 🚀 Features

* **Accurate Predictions**: Utilizes a Logistic Regression model trained on the standard Iris dataset.
* **High-Performance API**: Built with FastAPI, ensuring fast response times and asynchronous capabilities.
* **Robust Data Validation**: Employs Pydantic to validate incoming data, preventing errors and ensuring data integrity.
* **Dockerized for Portability**: Comes with a `Dockerfile` for building a self-contained application that runs anywhere.
* **Interactive Documentation**: Automatically generates user-friendly API documentation with Swagger UI and ReDoc.

---

## 📂 Project Structure

```bash
/iris-api
├── Dockerfile          # Docker configuration for containerization
├── main.py             # FastAPI application source code
├── train.py            # Script to train and save the ML model
├── iris_model.joblib   # The serialized, pre-trained model file
├── requirements.txt    # Python package dependencies
└── README.md           # This file
```


## ⚙️ Setup and Usage

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

* Python 3.8+
* Docker

### 1. Installation

First, clone the repository and navigate into the project directory. Then, install the required Python packages.

```bash
# Clone the repository
git clone [https://github.com/aaditya-01-28/iris-api.git](https://github.com/aaditya-01-28/iris-api.git)

```bash
# Navigate into the project directory
cd iris-api

# Install dependencies
pip install -r requirements.txt
```
2. Train the Model
Before starting the API, you must first train the model by running the train.py script. This will generate the iris_model.joblib file.

```bash
python train.py
```

3. Running the Application
You can run the API either directly with a Uvicorn server or as a Docker container.

Method A: Run with Uvicorn (for Development)
This method is ideal for development as it supports features like hot-reloading.

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Method B: Run with Docker (for Production)
This method showcases the containerized deployment of the application.

```bash

# 1. Build the Docker image
docker build -t iris-api .

# 2. Run the Docker container
docker run -p 8000:8000 iris-api
```

4. Accessing the API
Once the server is running (using either method), the API will be available:

API URL: http://localhost:8000

Interactive Docs (Swagger UI): http://localhost:8000/docs

🧪 API Demonstration
You can test the prediction endpoint by sending a POST request.

Example Request with curl:

```bash

curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 5.9,
  "sepal_width": 3.0,
  "petal_length": 5.1,
  "petal_width": 1.8
}'
```

Expected Successful Response (for a Virginica flower):
```bash

JSON

{
  "prediction": 2,
  "species_name": "Virginica"
}
