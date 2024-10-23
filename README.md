# Breast Cancer Classifier

This project is a web-based app for breast cancer classification, allowing users (such as physicians) to input various tumor features and receive predictions on whether a tumor is benign or malignant. The app is built using **Streamlit** and leverages a pre-trained machine learning model from **PyCaret** to make predictions.

## Features

- Predict whether a breast tumor is benign or malignant based on input features.
- User-friendly interface for inputting tumor characteristics.
- Provides both the classification (Benign/Malignant) and a confidence score for the prediction.

## Technologies Used

- **Python**
- **Streamlit**: For creating the web app interface.
- **PyCaret**: For machine learning model deployment.
- **Pandas**: For data manipulation.
- **scikit-learn**: For creating the confusion matrix and other metrics (part of PyCaret).
- **matplotlib**: For data visualization
- **seaborn** : For data visualization

## Model Information

The app uses a logistic regression model trained on breast cancer data. The model pipeline is created and stored using PyCaret, and is loaded in the app for real-time predictions.

## Getting Started

To run this app locally, follow these steps:

### Prerequisites

Make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sthoran/breastcancerclassifier.git
    cd breastcancerclassifier
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv env
    source env/bin/activate    # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

Once the app is running, you will see a local URL in your terminal. Open this URL in your browser to access the app.

### App Features

Once the app is running, you will be able to:

1. Input the following tumor features:
   - Worst Texture
   - Worst Concavity
   - Standard Error Radius
   - Worst Smoothness
   - Worst Symmetry
   - Mean Concavity
   - Standard Error Fractal Dimension
   - Standard Error Area

2. Click the **Classify** button to get the prediction and confidence score.


