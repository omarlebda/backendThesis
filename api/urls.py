from django.urls import path
from .views import AlumniList, AlumniDetail, AlumniEdit, APIGraduationCreateView, APIGraduationUpdateDeleteView, APIGraduationProjectCreateView, APIGraduationProjectUpdateDeleteView, APIJobCreateView, APIJobEditDeleteView, APICompanyCreateView
urlpatterns = [
path('<int:pk>/', AlumniDetail.as_view()),
path('edit_profile/<int:pk>/', AlumniEdit.as_view()),
path('', AlumniList.as_view()),
path('<int:pk>/add_graduation/', APIGraduationCreateView.as_view()),
path('edit_or_delete_graduation/<int:pk>/', APIGraduationUpdateDeleteView.as_view()),
path('<int:pk>/add_graduation_project/', APIGraduationProjectCreateView.as_view()),
path('<int:pk>/edit_or_delete_graduation_project/', APIGraduationProjectUpdateDeleteView.as_view()),
path('<int:pk>/create_job/', APIJobCreateView.as_view()),
path('<int:pk>/edit_delete_job/', APIJobEditDeleteView.as_view()),
path('create_company/', APICompanyCreateView.as_view()),
#path('<int:pk>/edit_delete_company/', APICompanyEditDeleteView.as_view()),
]
