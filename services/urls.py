from django.urls import path,include
from rest_framework import routers
from .views import *
app_name = "images"

# router = routers.DefaultRouter()
# router.register('images', ImageView)
urlpatterns = [
    path('images/<id>', ImageAPIViewSingel.as_view()),
    path('images/', ImageView.as_view()),
]