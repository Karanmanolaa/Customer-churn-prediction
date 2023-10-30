# Project 3 - Customer-churn-prediction

![Customer-churn-rate-1024x683](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/86508d72-08b4-4d3b-995d-1898f629d992)


# Table of Content
- Overview
- Problem Statement and Motivation
- Technical Aspects
- Visualizations
- Challenges and Solutions

# 1- Overview :
The aim of this project is to perform customer churn prediction on a bank dataset. Using machine learning classification techniques, I analyzed a dataset comprising approximately 10,000 records. The dataset was sourced from Kaggle and serves as the foundation for training our customer churn classification model.

# 2- Problem Statement and Motivation :
In this project, I aimed to tackle a significant issue in the banking industry – customers leaving. This is a crucial problem because it can seriously affect a bank's revenue and financial stability. By utilizing data-driven techniques, our objective was to predict and prevent customer churn. I also recognized that churn patterns can vary based on geographical and demographic factors. Our approach was to predict churn before it occurred, enabling us to allocate resources effectively. Ultimately, our goal was to enhance customer satisfaction and retain their loyalty to the bank.


# 3- Technical Aspects :
In this project i have used python programming language and its libraries - scikit-learn,pandas, numpy,matplotlib,seaborn,xgboost for different purpose like
- Performed Explolatory data analysis using matplotlib and seaborn.
- Created new features (feature engineering) like exited,stayed for further analysis.
- Converted categorical columns to numerical using Labelencoder.
- Applied standard scalar to ensure that all the features in a dataset are on a similar scale,making it easier for machine learning models to learn and make accurate predictions,especially when features have different units or ranges.
- I tried several models like LogisticRegression , decision tree.
- Performed hyperparameter tuning and Random Forest model did the best with and accuracy of 0.86.

# 4 - Challenges and Solutions:
Challenges:
- Class Imbalance: In customer churn prediction, it's common to have an imbalanced dataset, where the number of customers who stayed far exceeds those who left.
This imbalance can lead to model bias,where the model may have difficulty in correctly identifying the minority class (churned customers).

Solutions :
-Utilized models like Random Forest (with tuned hyperparameters) that are robust and less prone to overfitting, making the model more reliable when dealing with imbalanced datasets.

  

  # 5 - Visualizations:


![download corr](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/7d81b86f-b82d-4bf0-b1eb-cda87cae338a)

  ![download 1](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/3473d1d8-7ee8-4ee5-a1dd-ea7cc575c740)

![download 2](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/4042efc0-8a88-43d5-9a2e-93cf63fb44a7)


![download 4](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/0da4bf98-5119-44bd-a383-38ac80f07ef8)


![download 5](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/efe7a44e-9eab-4f99-a1b4-368ccdeeafea)


![download 6](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/7a1a0da7-aaa9-4180-9534-a75ecdd5bbc5)


![download 7](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/e70d41fd-01ab-436e-8f56-efdd8de9b6b5)


![download 8](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/5a8c0219-346f-4cea-8ce5-98f944c4277a)


![download 9](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/6df2114f-764b-410a-a129-73549053b746)


![download 10](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/9203dd40-c0ab-46b0-b61a-d0fd3e48e6c3)


![download 11](https://github.com/Karanmanolaa/Customer-churn-prediction/assets/144649975/f838dd7d-31a0-4d67-b5fe-c841957e650d)











  
