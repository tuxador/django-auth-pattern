from django.urls import path
from . import views
#from . import views

app_name = 'correspondence'
urlpatterns = [
    path('<slug:slug>_courrier<int:pk>',
         views.courrier_pdf, name='courrier_pdf'),
    path('<slug:slug>_certificat<int:pk>',
         views.certificat_pdf, name='certificat_pdf'),
    path('<slug:slug>_stomato<int:pk>',
         views.stomato_pdf, name='stomato_pdf'),
    path('<slug:slug>_arret<int:pk>',
         views.arret_pdf, name='arret_pdf'),
        ]
#    path('articles/<int:year>/', views.year_archive),
#    path('articles/<int:year>/<int:month>/', views.month_archive),
