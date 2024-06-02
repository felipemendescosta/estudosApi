from ninja import NinjaAPI
from .models import Livro
import json

api = NinjaAPI()

@api.get('livro/')
def listar(request):
    livro=Livro.objects.all()
    response = [{'id': i.id,'titulo': i.titulo,'descricao': i.descricao,'autor': i.autor} for i in livro]
    print(response)
    return response