from django.shortcuts import render, get_object_or_404
from .models import Prato

# Create your views here.
def index(request):
    
    lista_pratos = Prato.objects.all()
    return render(request, 'index.html', {'lista_pratos': lista_pratos})

def churrasco(request, id):
    prato = get_object_or_404(Prato, id=id)
    return render(request, 'churrasco.html',{'prato': prato})