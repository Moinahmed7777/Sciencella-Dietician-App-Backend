# Sciencella-Dietician-App-Backend

## Overview
Sciencella Dietitian App is a food journaling photo recognition app designed to assist dieticians to monitor their patient’s dietary habits to reduce the risk of cancer,diabetes,heart disease and improve the condition of patients.
The app utilizes computer vision technology to help clients track their nutritional intake.
The app allows clients to upload images of their meals through their camera and receive information of what the food is and the macronutrients of the recognized food. 
After creating the client's account, clients are prompted to record their biometrics and set nutritional goals or diets with the help of their dietitian.
The app then helps clients to stay on track with their nutritional goals by calculating a daily meal score based on the client's dietary needs and food intake.
 
## Features
- Recognize what food is in the image from 101 food classes.
- Provide macronutrients of the food pulled from the USDA database.
- the ability to track daily meal consumption.
- the ability to track your own diet.
- the ability to get a nutrition score based on meals consumed throughout your day.

## Technologies Used
- Flask
- SQlite
- AWS RDS 
- Tensorflow

## Diagrams
![image](https://user-images.githubusercontent.com/33766593/222344947-66060ed6-0488-4ea6-aadd-f32f60050da7.png)



## Demo

## How to run
- Clone the repo 
- Create a virtual environment with python 3.6.13 
- Install all the required dependencies by running the command "pip install -r requirements.txt"
- Navigate to code and run command "python app.py" to start the Flask application.


## Conclusion
The project was a learning experience that allowed me to gain knowledge on both transfer learning, creating RESTful APIs and designing the database.
Despite the initial difficulties, we were able to overcome them and successfully develop a large CNN model that can recognize and predict food from food images,
track clients diet and provide a score from their food intake.

## Reference
Tflite model maker - https://www.tensorflow.org/lite/models/modify/model_maker/image_classification
