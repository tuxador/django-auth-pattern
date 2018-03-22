from django.urls import path
from . import views
#from . import views

app_name = 'correspondence'
urlpatterns = [
    path('<slug:slug>_courrier<int:pk>',
         views.courrier_pdf, name='courrier_pdf'),
    ]
#    path('articles/<int:year>/', views.year_archive),
#    path('articles/<int:year>/<int:month>/', views.month_archive),
