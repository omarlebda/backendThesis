from rest_framework import serializers
from alumni.models import Alumni, Graduation, GraduationProject, Company, Job, User


class GraduationProjectSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField()

    class Meta:
        fields = ('pk', 'title', 'description', 'mark', 'gitLink',)
        model = GraduationProject


class GraduationSerializer(serializers.ModelSerializer):
    grad_project = GraduationProjectSerializer(read_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        fields = ('id', 'degree', 'faculty', 'yearOfGraduation',
                  'groupNumber', 'grad_project', 'description', 'university',)
        model = Graduation


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        fields = ('id', 'name', 'address', 'email', 'information',)
        model = Company


class WorkSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        fields = ('id', 'position', 'startDate', 'endDate', 'company',)
        model = Job


class AlumniSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.CharField(source="user.email", read_only=True)
    phone_number = serializers.CharField(
        source="user.phone_number", read_only=True)
    first_name = serializers.CharField(
        source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    # bio = serializers.CharField(source="user.bio", read_only=True)
    # current_city = serializers.CharField(source="user.current_city", read_only=True)
    # birthdate = serializers.CharField(source="user.birthdate", read_only=True)
    graduation = GraduationSerializer(many=True, read_only=True)
    work = WorkSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'username', 'email', 'graduation', 'work', 'profile_pic', 'phone_number', 'bio', 'birthdate', 'current_city',
                  'current_job', 'facebook_link', 'twitter_link', 'instagram_link', 'skype_link', 'linkedin_link', 'first_name', 'last_name', 'user_id')
        model = Alumni


class CreateGraduationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('alumni', 'faculty', 'degree', 'yearOfGraduation',
                  'groupNumber', 'description', 'university')
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
