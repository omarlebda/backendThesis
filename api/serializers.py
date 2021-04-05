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
    email = serializers.CharField(source="user.email")
    phone_number = serializers.CharField(
        source="user.phone_number")
    first_name = serializers.CharField(
        source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    graduation = GraduationSerializer(many=True, read_only=True)
    work = WorkSerializer(many=True, read_only=True)
    profile_pic = serializers.ImageField(read_only=True)

    class Meta:
        fields = ('id', 'username', 'email', 'graduation', 'work', 'profile_pic', 'phone_number', 'bio', 'birthdate', 'current_city',
                  'current_job', 'facebook_link', 'twitter_link', 'instagram_link', 'skype_link', 'linkedin_link', 'first_name', 'last_name', 'user_id')
        model = Alumni

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('user')
        profile = instance.user

        # User Info
        profile.first_name = profile_data.get(
            'first_name', profile.first_name)
        profile.last_name = profile_data.get(
            'last_name', profile.last_name)
        profile.email = profile_data.get(
            'email', profile.email)
        profile.phone_number = profile_data.get(
            'phone_number', profile.phone_number)
        profile.save()

        # Alumni Info
        instance.bio = validated_data.get(
            'bio', instance.bio)
        instance.birthdate = validated_data.get(
            'birthdate', instance.birthdate)
        instance.current_city = validated_data.get(
            'current_city', instance.current_city)
        instance.current_job = validated_data.get(
            'current_job', instance.current_job)
        instance.facebook_link = validated_data.get(
            'facebook_link', instance.facebook_link)
        instance.twitter_link = validated_data.get(
            'twitter_link', instance.twitter_link)
        instance.instagram_link = validated_data.get(
            'instagram_link', instance.instagram_link)
        instance.skype_link = validated_data.get(
            'skype_link', instance.skype_link)
        instance.linkedin_link = validated_data.get(
            'linkedin_link', instance.linkedin_link)
        instance.save()

        return instance


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
