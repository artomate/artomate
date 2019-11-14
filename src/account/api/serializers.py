from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from account.models import Account, KycInfo, PostProject, Categories


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    # mobile = serializers.CharField(min_length=10, max_length=12)
    class Meta:
        model = Account
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],

        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class KYCInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KycInfo
        fields = ['id', 'fullname', 'dob', 'mobile', 'idprooffront', 'idproofback', 'kycstatus', 'userid']

    def save(self):
        kyc = KycInfo(
            fullname=self.validated_data['fullname'],
            dob=self.validated_data['dob'],
            mobile=self.validated_data['mobile'],
            idprooffront=self.validated_data['idprooffront'],
            idproofback=self.validated_data['idproofback'],
        )

        return kyc


class PostProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostProject
        fields = ('id', 'projectname', 'description', 'files', 'userid', 'username', 'projectcode')

        # extra_kwargs = {'files': { 'required': True, 'multiple': True}}

        def save(self):
            project = PostProject(
                projectname=self.validated_data['projectname'],
                description=self.validated_data['description'],
                files=self.validated_data['files'],
            )
            return project


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'categoryname', 'categorycode', 'subcategoryname', 'subcategorycode')

        def save(self):
            categories = Categories(
                categoryname=self.validated_data['categoryname'],
                subcategoryname=self.validated_data['subcategoryname'],
            )
            return categories


class CategorySubCategoryList(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'categoryname', 'categorycode')
