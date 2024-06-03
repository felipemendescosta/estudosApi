
from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI, Router


api = NinjaAPI()

deletar = Router()

api.add_router("/events/")



urlpatterns = [
    path("admin/", admin.site.urls),
    path('cadastro/',include('cadastro.urls'))
]
