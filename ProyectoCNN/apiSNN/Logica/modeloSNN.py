from django.db import models
from django.urls import reverse
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer, ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.python.keras.models import load_model, model_from_json
from keras import backend as K
from apiSNN import models
import os
import matplotlib.pyplot as plt
from keras.models import Sequential
import pathlib
#import keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from keras.preprocessing.image import load_img
from keras.preprocessing import image
from skimage.transform import resize
class modeloSNN():
    """Clase modelo SNN"""
    Selectedmodel=Sequential()
    def suma(num1=0,num2=0):
        resultado=num1+num2
        return resultado
    def cargarRNN(nombreArchivoModelo,nombreArchivoPesos):
        K.reset_uids()
        # Cargar la Arquitectura desde el archivo JSON
        with open(nombreArchivoModelo+'.json', 'r') as f:
            model = model_from_json(f.read())
        # Cargar Pesos (weights) en el nuevo modelo
        model.load_weights(nombreArchivoPesos+'.h5py')
        print("Red Neuronal Cargada desde Archivo")
        return model
    def predecirImagen(self,imagen):#Pclass=1, Sex='female', Age=60 ,Fare=0, Embarked='C'
        #Modelo optimizado
        #img = image.load_img(self.img, target_size=(21,28))
        images=[]
        print('MODELO OPTIMIZADO')
        nombreArchivoModelo=r'apiSNN/Logica/model_architecture'
        nombreArchivoPesos=r'apiSNN/Logica/sports_mnist'
        #return (str(pathlib.Path().absolute())+'\Modelos')
        self.Selectedmodel=self.cargarRNN(nombreArchivoModelo,nombreArchivoPesos)
        print(self.Selectedmodel)
        print(self.Selectedmodel.summary())

            #METODOD DE PRDICCION

            # AQUI ESPECIFICAMOS UNAS IMAGENES
        filenames = [imagen]
        for filepath in filenames:
            image = plt.imread(filepath,0)
            image_resized = resize(image, (21, 28),anti_aliasing=True,clip=False,preserve_range=True)
            images.append(image_resized)

        print(filenames)
        print(images)
        X = np.array(images, dtype=np.uint8) #convierto de lista a numpy
        test_X = X.astype('float32')
        test_X = test_X / 255.
        print(test_X)

        predicted_classes = self.Selectedmodel.predict(test_X)


        directories=['tenis', 'natacion','boxeo', 'beisball', 'ciclismo', 'golf', 'americano', 'futbol', 'f1', 'basket']



        deportes=[]
        indice=0
        for directorio in directories:
            name = directorio.split(os.sep)
            print(indice , name[len(name)-1])
            deportes.append(name[len(name)-1])
            indice=indice+1
        print(deportes)

        for i, img_tagged in enumerate(predicted_classes):
            print(filenames[i], deportes[img_tagged.tolist().index(max(img_tagged))])
            resu= deportes[img_tagged.tolist().index(max(img_tagged))]
           
      #'tenis', 'natacion','boxeo', 'beisball', 'ciclismo', 'golf', 'americano', 'futbol', 'f1', 'basket'

        ynew = self.Selectedmodel.predict_proba(test_X)
        probaa=self.Selectedmodel.predict_proba(test_X)

        if resu=="tenis":
            proba=self.Selectedmodel.predict_proba(test_X)[:,0]
            total=proba*100

        if resu=="natacion":
            proba=self.Selectedmodel.predict_proba(test_X)[:,1]
            total=proba*100

        if resu=="boxeo":
            proba=self.Selectedmodel.predict_proba(test_X)[:,2]
            total=proba*100
        
        if resu=="beisball":
            proba=self.Selectedmodel.predict_proba(test_X)[:,3]
            total=proba*100
        
        if resu=="ciclismo":
            proba=self.Selectedmodel.predict_proba(test_X)[:,4]
            total=proba*100
        
        if resu=="golf":
            proba=self.Selectedmodel.predict_proba(test_X)[:,5]
            total=proba*100

        if resu=="americano":
            proba=self.Selectedmodel.predict_proba(test_X)[:,6]
            total=proba*100

        if resu=="futbol":
            proba=self.Selectedmodel.predict_proba(test_X)[:,7]
            total=proba*100

        if resu=="f1":
            proba=self.Selectedmodel.predict_proba(test_X)[:,8]
            total=proba*100

        if resu=="basket":
            proba=self.Selectedmodel.predict_proba(test_X)[:,9]
            total=proba*100

        # show the inputs and predicted probabilities
        print(probaa)
        print(proba)


        id=4
        dbReg=models.Image(id,imagen, label=resu, probability=total)
        dbReg.save()
      
        mensaje=resu
        men=total
        return mensaje,total
       
