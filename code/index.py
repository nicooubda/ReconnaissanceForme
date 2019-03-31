#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 23:43:18 2019

@author: nicolas
"""

#! /usr/bin/python
# -*- coding:utf-8 -*-


from imageai.Prediction import ImagePrediction
import os
from flask import Flask, render_template, request
from imageai.Detection import ObjectDetection
import shutil

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predicti')
def prediction():
    predire =[]
    execution_path = os.getcwd()
    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("resnet50_weights_tf_dim_ordering_tf_kernels.h5")
    prediction.loadModel()
    predictions, percentage_probabilities = prediction.predictImage("lion.jpg", result_count=5)
    for index in range(len(predictions)):
        a=predictions[index] , " : " , percentage_probabilities[index]
        predire.append(a)
        print(a)
    return predire


@app.route('/prediction')
def formulairePrediction():
    
    return render_template('prediction.html')

@app.route('/predictions', methods=["POST"])
def predire():
    
    b=(request.form['imgInp'])
    print(b)
    predire=""
    max=0.0
    """execution_path = os.getcwd()
    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("resnet50_weights_tf_dim_ordering_tf_kernels.h5")
    prediction.loadModel()
    predictions, percentage_probabilities = prediction.predictImage(b, result_count=5)
    for index in range(len(predictions)):
        print("======================",percentage_probabilities[index])
        if (percentage_probabilities[index])>max:
            max = percentage_probabilities[index]
            c=predictions[index] 
            print(predictions[index] , " : " , percentage_probabilities[index])
            p=percentage_probabilities[index]"""
            
            
    execution_path = os.getcwd()
    bc=""
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , b), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

    print("=====================================================================")
    for eachObject in detections:
        if eachObject["percentage_probability"]>0:
            max = eachObject["percentage_probability"]
            predire = eachObject["name"]
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        bc=(eachObject["name"] , " : " , eachObject["percentage_probability"])
        
        #predire.append(bc)
   
    return """<html>

<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">      
	<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/css/materialize.min.css">
	<script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>           
	<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/js/materialize.min.js"></script> 
	<link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	<link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>

	
</head>
<body>
	<!--NAVBAR-->
	<div class="navbar-fixed">
		<nav class="blue">
			<div class="navbar-wrapper">
				<a href="#" class="brand-logo" style="margin-left: 16px">Reconnaissance de forme</a>
				<ul id="nav-mobile" class="right hide-on-med-and-down">
					<li><a href="/">Accueil</a></li>
					<!--<li><a href="categorie">Ajouter une catégorie</a></li>-->
					<li><a href="prediction">Prédire une image</a></li>
                    <li><a href="predictionImage">Détection d'objet sur image</a></li>
				</ul>
			</div>
		</nav>
	</div>
    
    <div class="row message">
			<div class="container">
				<div class="card-panel red lighten-2 white-text">
<h4>La catégorie de l'objet est: {predire} avec un taux de {max}</h4>
				</div>
			</div>
		</div>
    
</body>
</html>  
""".format(predire=predire,max=max)

@app.route('/predictionImage')
def predictionImage():
    return render_template('predictions.html')

@app.route('/predictionss', methods=["POST"])
def predires():
    
    b=(request.form['imgInp'])
    lien=(request.form['lien'])
    print(b)
    predire=""
   
    """execution_path = os.getcwd()
    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("resnet50_weights_tf_dim_ordering_tf_kernels.h5")
    prediction.loadModel()
    predictions, percentage_probabilities = prediction.predictImage(b, result_count=5)
    for index in range(len(predictions)):
        print("======================",percentage_probabilities[index])
        if (percentage_probabilities[index])>max:
            max = percentage_probabilities[index]
            c=predictions[index] 
            print(predictions[index] , " : " , percentage_probabilities[index])
            p=percentage_probabilities[index]"""
    
    execution_path = os.getcwd()
    bc=""
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , b), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
    for eachObject in detections:
        if eachObject["percentage_probability"]>0:
            max = eachObject["percentage_probability"]
            predires = eachObject["name"]
            print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
            bc=(eachObject["name"] , " : " , eachObject["percentage_probability"])
    lien="./d"
    listImage = os.listdir(lien)  
    for image in listImage:     
        execution_path = os.getcwd()
        bc=""
        images =  lien +'/'+image
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
        detector.loadModel()
        detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , images), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
        verifie = 0
        for eachObject in detections:
            predire = eachObject["name"]
            if predire == predires:
                verifie = 1
                max = eachObject["percentage_probability"]
               
            #print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
            #bc=(eachObject["name"] , " : " , eachObject["percentage_probability"])
        if verifie == 1 :
            shutil.copy(image, './copie')
            print("=====================   TROUVER TROUVER ======================================")


    
    
    
    return """<html>

<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">      
	<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/css/materialize.min.css">
	<script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>           
	<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/js/materialize.min.js"></script> 
	<link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	<link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>

	
</head>
<body>
	<!--NAVBAR-->
	<div class="navbar-fixed">
		<nav class="blue">
			<div class="navbar-wrapper">
				<a href="#" class="brand-logo" style="margin-left: 16px">Reconnaissance de forme</a>
				<ul id="nav-mobile" class="right hide-on-med-and-down">
					<li><a href="/">Accueil</a></li>
					<!--<li><a href="categorie">Ajouter une catégorie</a></li>-->
					<li><a href="prediction">Prédire une image</a></li>
                    <li><a href="predictionImage">Détection d'objet sur image</a></li>
				</ul>
			</div>
		</nav>
	</div>
    
    <div class="row message">
			<div class="container">
				<div class="card-panel red lighten-2 white-text">
<h4>La catégorie de l'objet est: {predire} avec un taux de {max}</h4>
				</div>
			</div>
		</div>
    
</body>
</html>  
""".format(predire=predire,max=max)



if __name__ == '__main__':
    app.run(debug=True)
