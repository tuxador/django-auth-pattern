from django.urls import path

from . import views

app_name = 'clinic'
urlpatterns = [
    path('patients/', views.ListPatients.as_view(), name='patients'),
#    path('articles/<int:year>/', views.year_archive),
#    path('articles/<int:year>/<int:month>/', views.month_archive),
#    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
] 
