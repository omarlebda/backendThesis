from rest_framework import serializers
from alumni.models import Alumni, Graduation, GraduationProject, Company, Job, User

class GraduationProjectSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('title', 'description', 'mark', 'gitLink',)
    model = GraduationProject

class GraduationSerializer(serializers.ModelSerializer):
    grad_project = GraduationProjectSerializer(read_only = True)
    class Meta:
        fields = ['degree', 'faculty', 'yearOfGraduation', 'groupNumber', 'grad_project',]
        model = Graduation

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'address', 'email', 'information',]
        model = Company


class WorkSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only = True)
    class Meta:
        fields = ['position', 'startDate', 'endDate', 'company',]
        model = Job

class AlumniSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.CharField(source="user.email", read_only=True)
    #graduation = serializers.StringRelatedField(many=True)
    graduation = GraduationSerializer(many=True, read_only=True)
    work = WorkSerializer(many=True, read_only=True)
    class Meta:
        fields = ('id', 'username', 'email', 'graduation', 'work',)
        model = Alumni


class CreateGraduationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('alumni', 'faculty', 'degree', 'yearOfGraduation', 'groupNumber',)
        model = Graduation

class CreateGraduationProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'description', 'mark', 'gitLink', 'graduation',)
        model = GraduationProject

class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('alumni', 'company', 'position', 'startDate', 'endDate',)
        model = Job

class CreateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'address', 'email', 'information',)
        model = Company