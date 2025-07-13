📄 Project Title:

"Predicting Credit Card Default Risk Using Machine Learning"

---

📌 Objective:

To develop a machine learning model that predicts the likelihood of a customer defaulting on a credit card payment based on demographic and financial data.

---

📊 Dataset Information:

* **Source:** UCI Machine Learning Repository
* **Name:** Default of Credit Card Clients Dataset (Taiwan)
* **Duration:** April 2005 – September 2005
* **Total Observations:** 30,000 records
* **Features:**

  * **Demographics:** Age, Gender, Education, Marital Status
  * **Credit Limit:** LIMIT\_BAL
  * **Payment History:** PAY\_0 to PAY\_6
  * **Bill Statement Amounts:** BILL\_AMT1 to BILL\_AMT6
  * **Previous Payments:** PAY\_AMT1 to PAY\_AMT6
  * **Target Variable:** `default.payment.next.month` (0 = No, 1 = Yes)

---

🛠️ Technologies Used:

* **Language:** Python
* **Libraries:** pandas, numpy, scikit-learn, matplotlib, seaborn, streamlit
* **Environment:** Jupyter Notebook, VS Code
* **App Framework:** Streamlit

---

🧹 Data Pipeline Overview:

1. **Data Collection**

* Loaded dataset and checked for nulls, duplicates.

2. **Data Cleaning**

* Renamed columns for clarity.
* Removed duplicates if any.
* Handled outliers using IQR method or capping.

3. **Preprocessing**

* Encoded categorical features (e.g., gender, education).
* Feature scaling using StandardScaler for models sensitive to scale.
* Split into **X** and **y**, then into **train-test sets** (e.g., 80/20 split).

4. **Exploratory Data Analysis (EDA)**

* Visualized distributions (e.g., age, limit balance).
* Correlation heatmap.
* Class imbalance checked.

---

🔍 Model Building:

Model Tried:

* **Logistic Regression**
* **Decision Tree**
* ✅ **Random Forest (Best performing)**

### Best Model: **Random Forest Classifier**

* **Accuracy:** 84%
* **Precision (Class 1):** 0.85
* **Recall (Class 1):** 0.82
* **F1 Score (Class 1):** 0.83

```text
              precision    recall  f1-score   support

           0       0.82      0.86      0.84      7010
           1       0.85      0.82      0.83      7009

    Accuracy:                         0.84     14019
```

---

🌐 Deployment: Streamlit App

* A user-friendly web app was built using **Streamlit**.
* Takes user input (or pre-set test case) for all 23 features.
* Predicts and displays:

  * ✅ **Low risk of default** (if predicted class is 0)
  * ⚠️ **High risk of default** (if predicted class is 1)

---

📁 Project Structure:

```
MLENDTOEND/
│
├── data/
│   ├── rawdata/
│   ├── cleaneddata/
│   └── preprocessdata/
│
├── models/
│   └── model.pkl               # Trained Random Forest model
│
├── notebooks/
│   ├── datacollection.ipynb
│   ├── datacleaning.ipynb
│   ├── preprocess.ipynb
│   ├── eda.ipynb
│   └── modelbuilding.ipynb
│
├── src/
│   ├── datacollection.py
│   ├── datacleaning.py
│   ├── preprocessing.py
│   └── modelbuilding.py
│
├── app.py                      # Streamlit app
└── requirements.txt            # Environment setup
```

---

✅ Key Learnings:

* End-to-end pipeline from raw data to deployed model.
* Feature engineering and model evaluation.
* Deploying models using Streamlit.
* Interpreting precision-recall tradeoffs.

---

📦 Future Improvements:

* Use SMOTE to handle class imbalance.
* Deploy with Docker on cloud (e.g., Heroku, AWS).
* Add SHAP for explainable AI insights.