from django.urls import path

from message.views import main_page

urlpatterns = [
    path("", main_page, name='main-page')
]