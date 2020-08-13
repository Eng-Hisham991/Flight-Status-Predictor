# Will your flight be delayed? 
<br> 

<img src = "https://www.smartertravel.com/uploads/2013/10/stm52582875d01ca20131011.jpg" width = 600 height= 400>

## Background 

How many flights are delayed/cancelled or be on time each year? We built a classifier model using machine learning techniques that predicts whether your flight will be delayed or normal based on the 
airline, the destination city, the delay, the month, and the year leaving IAH airport in Houston, TX. 

## Steps 

A web app used to predict flight status at IAH airport in Houston, TX.

  -	Data was downloaded from: https://www.transtats.bts.gov/DL_SelectFields.asp
  
  -	We used Python (in Jupyter Notebook) to implement Data cleansing, Random Forest Classifier within Scikit-Learn package.
  
  -	We used TABLEAU to create visualizations.
  
  -	We successfully got cleaned data consists of more than 80 000 rows using to feed our training model.
  
  -	Random Forest Classifier Model scores more than 92 % on the testing data.
  
  -	Data and model were transported using Flask to a font end prepared with html, bootstrap, css and JavaScript.

## Tools/Packages Used

  -	Scikit Learn (for models LinearSVC, Random Forest, etc..).

  - Tensorflow.keras  (for transforming data).

  -	Pandas.

  -	Numpy.

  -	Tableau (For Visualization).

  -	Flask (For creation web application)


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
There was one story visualizations in total. The visuals compared the different kinds of delays experienced specifically here in the United States, the airports with the most delays, cancellation, on time and the airlines that are mostly affected by the delays.

## Flask App 

The Flask app is in direct communication with the model & the JavaScript file and the HTML file to predict the outcome based on the user input into the website. 

## How to use:
  -	Insert numbers on the boxes, choose Destination airport and destination city then click submit, the model will predict the most likely flight status at IAH airport in Houston, TX. 
App is available on AWS: https:// Enjoy!

 Hisham (@Eng-Hisham991), Abdullah (@Abdullah101298) and Mercy (@mercymuigai)





