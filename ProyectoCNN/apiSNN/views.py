#CONTROLADOR

from rest_framework import generics #para microservicio
from apiSNN import models
from apiSNN import serializers
from django.shortcuts import render
#simport pyrebase #para consumo servicio base de datos de firebase
from apiSNN.Logica import modeloSNN #para utilizar modelo SNN
import pyrebase
from django.http import HttpResponse
# Create your views here.
class Prueba():
    def home(request):
        return HttpResponse('Hello mundo')

class Image(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
class ListImage(generics.ListCreateAPIView):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer

class DetailImage(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer


config = {

    'apiKey': "AIzaSyDBYpL2tb3yh3SIPo2BFhlS7slKruVGOic",
    'authDomain': "proyectotiendajpri.firebaseapp.com",
    'databaseURL': "https://proyectotiendajpri.firebaseio.com",
    'projectId': "proyectotiendajpri",
    'storageBucket': "proyectotiendajpri.appspot.com",
    'messagingSenderId': "1046831721926",
    'appId': "1:1046831721926:web:7402a636a8cd165f4b16c7",
    'measurementId': "G-MKSCN84RDE"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

class Autenticacion():

    def singIn(request):

        return render(request, "signIn.html")

    def postsign(request):
        email=request.POST.get('email')
        passw = request.POST.get("pass")
        try:
            user = auth.sign_in_with_email_and_password(email,passw)
        except:
            message = "invalid cerediantials"
            return render(request,"signIn.html",{"msg":message})
        print(user)
        return render(request, "welcome.html",{"e":email})

class Clasificacion():
    
    def determinarImagen(request):

        return render(request, "predecirImagen.html")

    def predecir(request):
        try:
            #pclass = int(request.POST.get('pclass'))
            #sex = request.POST.get('sex')
            imagen= request.FILES['foto']
            print(imagen)
            #imagen='/imagenes/1.jpg'
            #fare = float(request.POST.get('fare'))
            #embarked = request.POST.get('embarked')
        except:
            imagen='/imagenes/1.jpg'

        #print(type(imagen))
        #resul=modeloSNN.modeloSNN.suma(num1,num2)
        resul=modeloSNN.modeloSNN.predecirImagen(modeloSNN.modeloSNN,imagen)
        return render(request, "welcome.html",{"e":resul})

     




