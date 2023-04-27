from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, name, gender, age, intro, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,
            age=age,
            intro=intro
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    name = models.CharField(max_length=10, blank=True)

    gender_choices = [
        ('M', '남성'),
        ('W', '여성'),
        ('N', '선택하지 않음')
    ]

    gender = models.CharField(
        max_length=1,
        choices=gender_choices,
        default='N',
        blank=True
    )

    age = models.PositiveSmallIntegerField(blank=True, null=True)

    intro = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
