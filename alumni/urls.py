from django.urls import path
from django.conf.urls import url
from .views import (AlumniList,
AlumniDetail,
GraduationCreateView,
GraduationProjectCreateView,
CompanyCreateView,
CompanyUpdateView,
CompanyDeleteView,
JobCreateView,
GraduationUpdateView,
GraduationDeleteView,
GraduationProjectUpdateView,
GraduationProjectDeleteView,
JobUpdateView,
JobDeleteView,
AlumniEdit)

urlpatterns = [
	path('', AlumniList.as_view(), name='AlumniList'),
	path('<int:pk>/', AlumniDetail.as_view(), name='AlumniDetail'),
	path('edit/<int:pk>/', AlumniEdit.as_view(), name='editAlumni'),
	path('<int:pk>/graduation/', GraduationCreateView.as_view(), name='newGraduation'),
	path('graduation/edit/<int:pk>/', GraduationUpdateView.as_view(), name='editGraduation'),
	path('graduation/delete/<int:pk>/', GraduationDeleteView.as_view(), name='deleteGraduation'),
	path('<int:pk>/graduation/project/edit/', GraduationProjectUpdateView.as_view(), name='editProjGraduation'),
	path('<int:pk>/graduation/project/delete/', GraduationProjectDeleteView.as_view(), name='deleteProjGraduation'),
	path('<int:pk>/company/', CompanyCreateView.as_view(), name='newCompany'),
	path('company/edit/<int:pk>/', CompanyUpdateView.as_view(), name='editCompany'),
	path('company/delete/<int:pk>/', CompanyDeleteView.as_view(), name='deleteCompany'),
	path('graduation/project/<int:pk>/', GraduationProjectCreateView.as_view(), name='newProject'),
	path('job/<int:pk>/', JobCreateView.as_view(), name='newJob'),
	path('job/edit/<int:pk>/', JobUpdateView.as_view(), name='editJob'),
	path('job/delete/<int:pk>/', JobDeleteView.as_view(), name='deleteJob'),
]
