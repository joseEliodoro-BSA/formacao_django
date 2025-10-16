from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia


def index(request):
    # fotografias = Fotografia.objects.all()
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id: int):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):
    fotografia = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_buscar = request.GET["buscar"]
        if nome_buscar:
            fotografia = fotografia.filter(nome__icontains=nome_buscar)

    print(fotografia)
    return render(request, "galeria/buscar.html", {"cards": fotografia})
