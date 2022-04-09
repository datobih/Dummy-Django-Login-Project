from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from my_login_app.models import UserProfile


class MyEmailBackend(BaseBackend):
	def authenticate(request,username=None,password=None):
		try:
			user=User.objects.get(email=username)
			if user.check_password(password):
				return user
			
		except User.DoesNotExist:
			return None

	
			

		return None

