# existing imports
from django.urls import path
from django.conf.urls import url
from apiSNN import views

urlpatterns = [
    path('imagenes/', views.ListImage.as_view()),
     path('imagenes/<int:pk>/', views.DetailImage.as_view()),
    url(r'^predecird/$',views.Clasificacion.determinarImagen),
    url(r'^predecir/',views.Clasificacion.predecir),
    url(r'^$',views.Autenticacion.singIn),
    url(r'^postsign/',views.Autenticacion.postsign),
]