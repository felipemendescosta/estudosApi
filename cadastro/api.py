from django.http import HttpRequest
from ninja import NinjaAPI, Schema
from ninja.types import DictStrAny
from .models import Livro
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

import json
import orjson
from ninja.parser import Parser

class ORJSONParser(Parser):
    def parse_body(self, request: HttpRequest):
        return orjson.loads(request.body)

api = NinjaAPI(parser=ORJSONParser())

@api.get('livro/')
def listar(request):
    livro=Livro.objects.all()
    response = [{'id': i.id,'titulo': i.titulo,'descricao': i.descricao,'autor': i.autor} for i in livro]
    print(response)
    return response

@api.get('livro/{id}') #route
def listar_livro(request, id: int): # no swagger e obrigatorio colocar o numero do id
    livro = get_object_or_404(Livro, id=id)
    return model_to_dict(livro)

@api.get('lista_consulta/') 
def lista_consulta(request, id: int=1): # no swagger já vem como padrão o primeiro id
    livro = get_object_or_404(Livro, id=id)
    return model_to_dict(livro)

class livroShema(Schema): #Shema que vem da lib api-Ninja
    titulo: str
    descricao: str
    autor: str = None

@api.post('livro') #requisicao do Tipo POST não tem /
def livro_criar(request, livro: livroShema):
    l1 = livro.dict()
    livro = Livro(**l1) # o livro já e um dicionario, podemos usar no parametro **kwargs que trabalha com funções (dicionarios) 
    livro.save()
    return 1
    
