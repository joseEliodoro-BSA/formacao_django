from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from apps.galeria.forms import FotografiaForms

from apps.galeria.models import Fotografia
from django.contrib import messages
from django.shortcuts import render, redirect


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")
    # fotografias = Fotografia.objects.all()
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, "galeria/index.html", {"cards": fotografias})


def imagem(request, foto_id: int):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galeria/imagem.html", {"fotografia": fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")

    fotografia = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_buscar = request.GET["buscar"]
        if nome_buscar:
            fotografia = fotografia.filter(nome__icontains=nome_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografia})


def nova_imagem(request):

    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect("login")

    form = FotografiaForms
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Nova fotografia cadastrada!")
            return redirect("index")

    return render(request, "galeria/nova_imagem.html", {"form": form})


def editar_imagem(request, foto_id: int):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)

        if form.is_valid():
            form.save()
            messages.success(request, "Imagem editada!")
            return redirect("index")

    return render(request, "galeria/editar_imagem.html", {"form": form, "foto_id": foto_id})


def deletar_imagem(request):
    return render(request, "galeria/deletar_imagem.html")
