from rest_framework import generics, permissions 
from alumni.models import Alumni, Graduation, GraduationProject, Company, Job
from .serializers import AlumniSerializer, CreateGraduationSerializer, CreateGraduationProjectSerializer, CreateJobSerializer, CreateCompanySerializer
from .permissions import IsAuthorOrReadOnly, IsTheOwnerOfGraduation


# Create your views here.
class AlumniList(generics.ListAPIView):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer


class AlumniDetail(generics.RetrieveAPIView):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer

class APIGraduationCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) 
    serializer_class = CreateGraduationSerializer
    queryset = Graduation.objects.all()

class APIGraduationUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    serializer_class = CreateGraduationSerializer
    queryset = Graduation.objects.all()

class APIGraduationProjectCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) 
    serializer_class = CreateGraduationProjectSerializer
    queryset = GraduationProject.objects.all()

class APIGraduationProjectUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsTheOwnerOfGraduation,) 
    serializer_class = CreateGraduationProjectSerializer
    queryset = GraduationProject.objects.all()

class APIJobCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) 
    serializer_class = CreateJobSerializer
    queryset = Job.objects.all()

class APIJobEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    serializer_class = CreateJobSerializer
    queryset = Job.objects.all()

class APICompanyCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) 
    serializer_class = CreateCompanySerializer
    queryset = Company.objects.all()

# class APICompanyEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CreateCompanySerializer
#     queryset = Company.objects.all()