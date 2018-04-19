from django.urls import path
from . import views


app_name='cathlab'
urlpatterns = [
    path('<slug:slug>_coro<int:pk>.pdf',
         views.coronarographie_pdf, name='coro_pdf'),
    path('<slug:slug>_coroscan<int:pk>.pdf',
         views.coroscan_pdf, name='coroscan_pdf'),
    ]
