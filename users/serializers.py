from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model

class NewUserSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance
		
	def update(self, instance, validated_data):
		for attr, value in validated_data.items():
			if attr == 'password':
				instance.set_password(value)
			else:
				setattr(instance, attr, value)
		instance.save()
		return instance
		
	class Meta:
		model = get_user_model()
		fields = ('email','name','password',)

class UserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ('id','email','name',)
