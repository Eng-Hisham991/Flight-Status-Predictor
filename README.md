# Will your flight be delayed? 
<br> 

<img src = "https://www.smartertravel.com/uploads/2013/10/stm52582875d01ca20131011.jpg" width = 600 height= 400>

## Background 

How many flights are delayed/cancelled each year? We built a classifier using machine learning techniques that predicts whether your flight will be delayed or normal based on the 
airline, the destination city, the delay, the month, and the year leaving IAH in houston. 

## Model Details 

The process started, after getting cleaned data, to choose the best model to use. The train, test and tuning done on the following models:

 - Logistic Regression.
 - K Nearest Neighbors.
 - Random Forest.
 - Support Vector Machine.

All the models were tested for accuracy which is follow for each:

 - Logistic Regression : ~ 91.5%
 - K Nearest Neighbors: 92.3%
 - Random Forest: 92.5%
 - Support Vector Machine: 70.8%

Based on accuracy, the Random Forest model was selected for this work.
  
## Visualizations 

The visualizations were done on tableau, posted on tableau public, and incorporated into the HTML. 
There were four visualizations in total. The visuals compared the different kinds of delays experienced specifically here in the United States, the airports with the most delays, and the airlines that are mostly affected by the delays.

## Flask App 

The Flask app is in direct communication with the model & the JavaScript file and the HTML file to predict the outcome based on the user input into the website. 



