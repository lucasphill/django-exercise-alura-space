from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia



def index(request):
    fotograifa = Fotografia.objects.order_by('datetime_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards':fotograifa})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia':fotografia})