from django.urls import path

from administrador.views import *

administrador_patterns =([
    path('', HomePageView.as_view(), name="home"),
    path('film/', FilmListView.as_view(), name='VerPeliculas'),
    path('create/', FilmCreateView.as_view(), name='create'),    
    path('<int:pk>/', FilmDetailView.as_view(), name='pelicula'),
    path('borrar/<int:pk>/', FilmDeleteView.as_view(), name='borrar'),    
    path('update/<int:pk>/', FilmUpdate.as_view(), name='update'),  
    path('buscar/', FilmCounterRedirectView.as_view(url='{% url administrador:pelicula %}'), name='buscar'),        

],'administrador')