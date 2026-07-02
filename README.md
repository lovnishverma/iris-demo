# 🌸 Iris Flower Species Prediction using Flask

A simple Machine Learning web application built with **Python**, **Flask**, and **Scikit-learn** that predicts the species of an Iris flower based on its measurements.

---

## 📌 Live Demo: 

https://iris-demo-gjle.onrender.com/

---

## 📌 Screenshot

<img width="590" height="886" alt="image" src="https://github.com/user-attachments/assets/c4d0cfa6-b60d-45df-94bd-5690c5f2b9ad" />


## 📌 Project Overview

This project demonstrates how to deploy a Machine Learning model using the Flask web framework.

The user enters four flower measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The trained Machine Learning model predicts the flower species:

- 🌼 Iris Setosa
- 🌸 Iris Versicolor
- 🌺 Iris Virginica

---

## 🛠 Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- Joblib
- HTML
- CSS

---

## 📁 Project Structure

```
Iris-Flask-App/
│
├── app.py
├── model.joblib
├── scaler.joblib
├── README.md
│
├── templates/
│   ├── index.html
│   └── about.html
│
└── static/
```

---

## 📦 Install Required Libraries

Open the terminal inside the project folder and run:

```bash
pip install flask pandas scikit-learn joblib
```

or


```bash
pip install -r requirements.txt
```


---

## ▶️ Run the Application

Run the Flask application:

```bash
python app.py
```

You should see output similar to:

```
* Running on http://127.0.0.1:5000/
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 💻 How to Use

1. Open the application in your browser.
2. Enter the four flower measurements.
3. Click the **Predict** button.
4. The predicted Iris species will be displayed.

---

## 📷 Sample Input

| Feature | Value |
|----------|------:|
| Sepal Length | 5.1 |
| Sepal Width | 3.5 |
| Petal Length | 1.4 |
| Petal Width | 0.2 |

### Output

```
Predicted Species:
setosa
```

---

## 🧠 Machine Learning Model

The application uses a **Logistic Regression** classifier trained on the famous Iris Dataset.

The input data is first scaled using **StandardScaler**, and then the trained model predicts the flower species.

---

## 📂 Files Description

### app.py

Main Flask application.

Responsible for:

- Loading the model
- Loading the scaler
- Creating Flask routes
- Receiving user input
- Predicting the species
- Displaying the result

---

### model.joblib

Saved Machine Learning model.

---

### scaler.joblib

Saved StandardScaler used during model training.

---

### templates/index.html

Home page containing:

- Input form
- Prediction result
- Current date and time

---

### templates/about.html

Developer information page.

---

## 🌼 Iris Dataset Features

| Feature | Description |
|----------|-------------|
| Sepal Length | Length of sepal (cm) |
| Sepal Width | Width of sepal (cm) |
| Petal Length | Length of petal (cm) |
| Petal Width | Width of petal (cm) |

---

## 📸 Application Workflow

```
User Input
      │
      ▼
Flask Application
      │
      ▼
StandardScaler
      │
      ▼
Machine Learning Model
      │
      ▼
Predicted Species
      │
      ▼
Displayed on Web Page
```

---

## 🚀 Future Improvements

- Add Bootstrap UI
- Display flower image based on prediction
- Show prediction confidence
- Deploy on Render or PythonAnywhere
- Add input validation
- Responsive mobile-friendly design

---

## 👨‍💻 Author

**Lovnish Verma**

Project Engineer

NIELIT Ropar

---

## ⭐ If you found this project helpful

Give this repository a ⭐ on GitHub and feel free to contribute!
