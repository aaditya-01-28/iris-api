# Iris Species Prediction API with FastAPI

[cite_start]This project is a solution for the AI Engineering Internship Assignment[cite: 1]. [cite_start]It involves building and deploying a machine learning model to predict the species of an Iris flower based on its sepal and petal measurements[cite: 91, 92]. The model is served via a REST API built with FastAPI and is containerized using Docker for easy deployment.

---

## Features

* [cite_start]**ML Model**: A Logistic Regression model trained on the classic Iris dataset[cite: 95].
* **FastAPI Backend**: A high-performance, asynchronous API to serve predictions.
* **Data Validation**: Utilizes Pydantic for robust, type-hinted validation of incoming request data.
* [cite_start]**Dockerized**: Includes a `Dockerfile` for building a portable container, simplifying deployment[cite: 52].
* **Interactive Docs**: Provides automatically generated and interactive API documentation (via Swagger UI and ReDoc).

---

## Project Structure