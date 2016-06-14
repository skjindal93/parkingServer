from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
	def create_user(self, email, password, name):
		if not email:
			raise ValueError('Users must have an email address')
		
		user = self.model(
			email=self.normalize_email(email),
			name=name
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, name):
		user = self.create_user(email,
				password=password,
				name=name
		)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Info(AbstractBaseUser, PermissionsMixin):
	email = models.CharField(max_length=255, unique=True)
	name = models.CharField(max_length=30, blank=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	created = models.DateTimeField('created', auto_now_add=True)
	updated = models.DateTimeField('updated', auto_now=True)
	wallet = models.IntegerField(default=1000)
	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']
	def get_short_name(self):
		return self.name
