from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, phone,password=None):
        """
        Creates and saves a User with the given email, name, and phone.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone,  password=None, password2= None):
        """
        Creates and saves a superuser with the given email, name, and phone.
        """
        if password == password2:
            raise ValueError("Password Did't match")
        user = self.create_user(
            email=email,
            name=name,
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    status = models.CharField(max_length=255)
    online_status = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, default="student")
    user_location = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)
    user_create_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Handle permissions here (if needed)
        return True

    def has_module_perms(self, app_label):
        # Handle module permissions here (if needed)
        return True

    @property
    def is_staff(self):
        # Use the is_superuser field provided by AbstractBaseUser
        return self.is_admin
