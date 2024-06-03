from ninja import Router
from .models import Event

deletar = Router()

@deletar.delete('events/deletar_livro/')
def list_events(request):
    pass


