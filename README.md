# Honey Purity & Price Prediction

An end-to-end Machine Learning project that predicts:

- **Honey Purity**
- **Honey Price**

using chemical properties and pollen analysis.

This project includes:

- Data preprocessing
- Model comparison (Linear Regression, Random Forest, Gradient Boosting)
- Best model selection
- Streamlit interactive dashboard
- Data analysis visualizations

---

## Project Overview

This project builds regression models to estimate:
1. Honey Purity  
2. Honey Price  

based on the following input parameters:

- CS
- Density
- WC (Water Content)
- pH
- EC (Electrical Conductivity)
- F
- G
- Viscosity
- Pollen Analysis

The system automatically selects the best-performing model based on **R² Score**.

---

## Machine Learning Models Used

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Model evaluation metrics:

- R² Score
- RMSE (Root Mean Squared Error)

The best model is selected based on highest R² performance.

---

## Exploratory Data Analysis

- Correlation Matrix
- Feature Distribution
- Price Distribution
- Price vs Purity
- Model Comparison Graphs
- Actual vs Predicted plots

---

## Project Structure

```
Honey_Price_Prediction/
│
├── models/                    
│   ├── honey_purity_model.pkl
│   ├── honey_price_model.pkl
│   ├── feature_columns_purity.pkl
│   └── feature_columns_price.pkl
│
├── plots/                   

├── Honey_Price_Prediction.ipynb            
├── honey_dataset.csv          
├── app.py                    
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### 1️. Clone the Repository

```bash
git clone https://github.com/TheVedantPatil/Honey_Price_Prediction.git
cd Honey_Price_Prediction
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 4️. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️. Run the Streamlit Application

```bash
streamlit run app.py
```

---

## Model Evaluation

Models were evaluated using:

- R² Score
- RMSE

The best-performing model was selected separately for:

- Purity Prediction
- Price Prediction

---

## Tech Stack Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## Future Improvements

- SHAP Explainability
- Confidence Intervals
- REST API (Flask/FastAPI)
- Cloud Deployment
- Real-time data integration

---

## Author

**Vedant Patil**

---

## License

This project is developed for academic and educational purposes.
