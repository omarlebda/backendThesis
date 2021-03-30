from django.urls import path
from .views import SignUpView, CustomObtainAuthToken

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('authenticate/', CustomObtainAuthToken.as_view()),
]
