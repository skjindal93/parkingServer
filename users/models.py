from django.db import models

class UserManager(BaseUserManager):
	def create_user(self, email, password, first_name):
		if not email:
			raise ValueError('Users must have an email address')
		
		user = self.model(
			email=self.normalize_email(email),
			first_name=first_name
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, first_name):
		user = self.create_user(email,
				password=password,
				first_name=first_name
		)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Info(AbstractBaseUser, PermissionsMixin):
	email = models.CharField(max_length=255, unique=True)
	first_name = models.CharField(max_length=30, blank=False)
	last_name = models.CharField(max_length=30, blank=True)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	created = models.DateTimeField('created', auto_now_add=True)
	updated = models.DateTimeField('updated', auto_now=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name']

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()
	def get_short_name(self):
		return self.first_name
