from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from administrador.models import *
from django.urls import reverse, reverse_lazy
# Create your views here.

from administrador.models import Film

class FilmListView(ListView):

    template_name = "administrador/film_list.html"

    model = Film
    queryset = Film.objects.all()
    paginate_by = 100  # if pagination is desired
    fields= "__all__"
    # Funcion
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q: 
             object_list = self.model.objects.filter(name__incontains=q)
        else:
             object_list = self.model.objects.all()
        return object_list
    
class FilmCreateView(CreateView):
    model = Film
    template_name = "administrador/film_form.html"
    fields = "__all__"    
    success_url = reverse_lazy('administrador:VerPeliculas')    


    
class HomePageView(TemplateView):
    
        template_name = "administrador/home.html"    
    
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
        
        
class FilmDetailView(DetailView):

    model = Film
    template_name = "administrador/film_detail.html"   
    fields= "__all__"
    
    
class FilmUpdate(UpdateView):
    model = Film
    fields = "__all__"
    template_name_suffix= "_update_form"   
    
    def get_success_url(self) -> str:
         return reverse_lazy('administrador:update', args=[self.object.id])+'?ok'       
     
class FilmDeleteView(DeleteView):
    model = Film
    success_url = reverse_lazy('administrador:VerPeliculas')   
 

class FilmCounterRedirectView(RedirectView):

    model = Film
    permanent = False
    query_string = True
    pattern_name = 'film_detail'

    def get_redirect_url(self, *args, **kwargs):
        film = get_object_or_404(Film, pk=kwargs['pk'])
        
        return super().get_redirect_url(*args, **kwargs)+'?'+film.id
    