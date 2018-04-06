from django.urls import path
from . import views
#from . import views

app_name = 'correspondence'
urlpatterns = [
    path('courrier_new/',
         views.CreateCourrier.as_view(), name='courrier_new'),
    path('certificat_new/',
         views.CreateCertificat.as_view(), name='certificat_new'),
    path('arret_new/',
         views.CreateArret.as_view(), name='arret_new'),
    path('stomato_new/',
         views.CreateStomato.as_view(), name='stomato_new'),
    path('<slug:slug>_courrier<int:pk>.pdf',
         views.courrier_pdf, name='courrier_pdf'),
    path('<slug:slug>_certificat<int:pk>.pdf',
         views.certificat_pdf, name='certificat_pdf'),
    path('<slug:slug>_stomato<int:pk>.pdf',
         views.stomato_pdf, name='stomato_pdf'),
    path('<slug:slug>_arret<int:pk>.pdf',
         views.arret_pdf, name='arret_pdf'),
        ]
#    path('articles/<int:year>/', views.year_archive),
#    path('articles/<int:year>/<int:month>/', views.month_archive),
