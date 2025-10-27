from django.urls import path
from apps.galeria.views import \
    index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem

# from django.http import JsonResponse

# def path_params(request, id=None):
#     if id:
#         return JsonResponse({
#             "id": id, 
#             "status": "active", 
#             "describe": "Lorem Ipsum", 
#             "name": "Bolo de Morango"
#         })
#     return JsonResponse({"status": "vivo"})

# def query_params(request):
#     tags = list(request.GET.keys())
#     response: dict = {"status": 200, "tags": tags}

#     for tag in request.GET.keys():
#         response[tag] = request.GET.get(tag)
        
#     return JsonResponse(response)

urlpatterns = [
    path("", index, name="index"),
    path("imagem/<int:foto_id>", imagem, name="imagem"),
    path("buscar", buscar, name="buscar"),
    path("nova-imagem", nova_imagem, name="nova-imagem"),
    path("editar-imagem/<int:foto_id>", editar_imagem, name="editar-imagem"),
    path("deletar-imagem/<int:foto_id>", deletar_imagem, name="deletar-imagem"),

    # path("path_params/<int:id>", path_params),
    # path("query_params", query_params),
]
