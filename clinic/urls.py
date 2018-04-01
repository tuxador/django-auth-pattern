from django.urls import path

from . import views

app_name = 'clinic'
urlpatterns = [
    path('patients/', views.ListPatients.as_view(), name='patients'),
    path('patients/<slug:slug>/', views.DetailPatient.as_view(),
         name='patient_detail'),
    path('patients/<slug:slug>_consultation<int:pk>.pdf',
         views.consultation_pdf, name='consultation_pdf'),
    path('patients/<slug:slug>_admission<int:pk>.pdf',
         views.admission_pdf, name='admission_pdf'),
    path('results/', views.PatientSearchListView.as_view(), name='search'),
#    path('articles/<int:year>/<int:month>/', views.month_archive),
#    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
              ] 
