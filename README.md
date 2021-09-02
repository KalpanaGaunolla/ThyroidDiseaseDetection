# Thyroid Disease Detection

Thyroid disease a very common problem in India, more than one crore people are suffering with the disease every year. Thyroid disorder can speed up or slow down the metabolism of the body.

The main objective of this project is to predict if a person is having compensated hypothyroid, primary hypothyroid, secondary hypothyroid or negative (no thyroid) with the help of Machine Learning. Classification algorithms such as Logistic regression, Random Forest, Decision Tree, Naïve Bayes, Support Vector Machine have been trained on the thyroid dataset, UCI Machine Learning repository. Random Forest performed well with better accuracy (98%), precision and recall. After hyper parameter tuning, application has deployed on Heroku with the help of flask.

## Website link
https://thyroid-disease-detection132.herokuapp.com/

## Demo
![Screenshot (339)](https://user-images.githubusercontent.com/81810275/131874488-10be3b94-6f3c-481b-a0f7-332f17efdf92.png)
![Screenshot (336)](https://user-images.githubusercontent.com/81810275/131875701-2f68ddcf-82fc-4550-b9cc-d14c13228e71.png)

## Technical aspect
* Python 3.9
*	Front-end: HTML, CSS
*	Back-end: Flask
*	IDE: Jupyter Notebook, PyCharm
*	Database: MongoDB Atlas
*	Deployment: Heroku

## How to run this app
Code is written in Python 3.9. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.
* Create virtual environment - *conda create -n myenv python=3.8*
*	Activate the environment - *conda activate myenv*
*	Install the packages - *pip install -r requirements.txt*
*	Run the app - *python app.py*

## Workflow

### Data Collection
Thyroid Disease Data Set from UCI Machine Learning Repository

### Data Pre-processing
* Missing values handling by Simple imputation (median strategy)
*	Outliers detection and removal by boxplot and percentile methods
*	Categorical features handling by ordinal encoding and label encoding
*	Feature scaling done by Standard Scalar method
*	Imbalanced dataset handled by SMOTE
*	Feature selection done by forward feature selection

### Model Creation and Evaluation
*	Various classification algorithms like Logistic Regression, Random Forest, Decision Tree, Naïve Bayes, Support Vector Machine tested.
*	Random Forest, Decision Tree and Logistic regression were given better results. Random Forest was chosen for the final model training and testing.
*	Hyper parameter tuning was performed.
*	Model performance evaluated based on accuracy, confusion matrix, classification report.

### Database Connection
MongoDB Atlas database used for this project

### Model Deployment
The final model is deployed using on Heroku using Flask framework

## Authors
**Kalpana Gaunolla**
**Ojjaswi Nirmal**

### If you like this project, please do give the star. We are open to your suggestions. 



