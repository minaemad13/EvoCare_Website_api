from django.urls import path,include
from rest_framework import routers
from .views import *
app_name = "images and packages"

# router = routers.DefaultRouter()
# router.register('images', ImageView)
urlpatterns = [
    path('images/<id>', ImageAPIViewSingel.as_view()),
    path('images/', ImageView.as_view()),
    path('packages/<sv_id>', PackagesView.as_view()),
]