from django.urls import path

from . import views

app_name = 'clinic'
urlpatterns = [
    path('patients/', views.ListPatients.as_view(), name='patients'),
    path('patients/new_patient', views.CreatePatient.as_view(),
         name='create_patient'),
    path('admissions/new/', views.CreateAdmission.as_view(),
         name='create_admission'),
    path('admissions/<int:pk>/edit/', views.UpdateAdmission.as_view(),
         name='update_admission'),
    path('patients/new_consultation', views.CreateConsultation.as_view(),
         name='create_consultation'),
    path('patients/new_fiche', views.CreateFicheTechnique.as_view(),
         name='create_fiche_technique'),
    path('patients/new_stress', views.CreateStress.as_view(),
         name='create_stress'),
    path('patients/<slug:slug>/', views.DetailPatient.as_view(),
         name='patient_detail'),
    path('admissions/', views.ListAdmissions.as_view(),
         name='list_admissions'),
    path('admissions/current/', views.CurrentAdmissions.as_view(),
         name='admission_current'),
    path('patients/<slug:slug>_consultation<int:pk>.pdf',
         views.consultation_pdf, name='consultation_pdf'),
    path('patients/<slug:slug>_admission<int:pk>.pdf',
         views.admission_pdf, name='admission_pdf'),
    path('patients/<slug:slug>_stress<int:pk>.pdf',
         views.stress_pdf, name='stress_pdf'),
    path('patients/<slug:slug>_fiche<int:pk>.pdf',
         views.fiche_pdf, name='fiche_pdf'),
    path('results/', views.PatientSearchListView.as_view(), name='search'),
              ]
