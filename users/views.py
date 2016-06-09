from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from braces.views import CsrfExemptMixin
from oauth2_provider.views.mixins import OAuthLibMixin
from django.views.generic import View
import json
from oauth2_provider.settings import oauth2_settings
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.http import HttpResponse

class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
	def has_permission(self, request, view):
		if request.method == 'POST':
			return True
		return super(IsAuthenticatedOrCreate, self).has_permission(request, view)

class NewUser(generics.CreateAPIView):
	serializer_class = NewUserSerializer
	model = get_user_model()
	permission_classes = (IsAuthenticatedOrCreate,)

class TokenView(CsrfExemptMixin, OAuthLibMixin, View):
	server_class = oauth2_settings.OAUTH2_SERVER_CLASS
	validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
	oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

	@method_decorator(sensitive_post_parameters('password'))
	def post(self, request, *args, **kwargs):
		url, headers, body, status = self.create_token_response(request)
		body = json.loads(body)
		if ("refresh_token" in body):
			del body["refresh_token"]
		body = json.dumps(body)
		response = HttpResponse(content=body, status=status)
		
		for k, v in headers.items():
			response[k] = v
		return response
