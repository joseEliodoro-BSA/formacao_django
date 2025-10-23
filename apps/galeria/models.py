from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Fotografia(models.Model):
    OPCAO_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
        ("ESTRELA", "Estrela"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False, default="")
    categoria = models.CharField(max_length=100, choices=OPCAO_CATEGORIA)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey( 
        to=User, 
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self):
        return "{" + f'"nome": {self.nome}, "legenda": {self.legenda}' + "}"
