from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, default='')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_freelancer = models.IntegerField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS  = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class KycInfo(models.Model):
    userid = models.IntegerField(default=None, null=True)
    fullname = models.CharField(max_length=100)
    dob = models.DateField()
    mobile = models.CharField(max_length=17)
    idprooffront = models.ImageField(upload_to='pictures/')
    idproofback = models.ImageField(upload_to='pictures/')
    kycstatus = models.IntegerField(null=True)
    username = models.CharField(max_length=100, default=None, null=True)


class Categories(models.Model):
    categoryname = models.CharField(max_length=50)
    categorycode = models.CharField(max_length=60, default=None, null=True)
    subcategoryname = models.CharField(max_length=60)
    subcategorycode = models.CharField(max_length=60, default=None, null=True)


class PostProject(models.Model):
    projectname = models.CharField(max_length=50)
    projectcode = models.CharField(max_length=30, default=None, null=True)
    description = models.CharField(max_length=50)
    files = models.FileField(upload_to='pictures/files/', )
    userid = models.IntegerField(default=None, null=True)
    username = models.CharField(max_length=50, default=None, null=True)
