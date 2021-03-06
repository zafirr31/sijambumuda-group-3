from django import forms
from django.contrib.auth.models import User
from .models import *
import re


class RegisterMember(forms.Form):

	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())
	re_password = forms.CharField(widget=forms.PasswordInput())

	def clean(self):
		# Cleans all fields

		def clean_username(self):
			# Checks if username is already in database
			cleaned_data = super(RegisterMember, self).clean()

			username = cleaned_data.get('username')
			try:
				user = User.objects.get(username=username)
			except:
				return username
			raise forms.ValidationError(
					'Username already taken!'
				)

		def clean_email(self):
			# Checks if email is already in database
			cleaned_data = super(RegisterMember, self).clean()
	
			email = cleaned_data.get('email')
			try:
				email_taken = User.objects.get(email=email)
			except:
				return email
			raise forms.ValidationError(
					'Email already taken!'
					)
		def clean_password(self):
			# Cleans password inputted, synchronously
			cleaned_data = super(RegisterMember, self).clean()

			password = cleaned_data.get('password')
			re_password = cleaned_data.get('re_password')

			# password length is greater than or equal to 8 
			validation_1 = (len(password) >= 8)

			# Password is equal to re_password 
			validation_2 = (password == re_password)

			# Password contains atleast one number
			validation_3 = bool(re.search(r'\d+', password))

			# Password contains atleast one uppercase character
			validation_4 = bool(re.search(r'[A-Z]+', password))

			# Password contains atleast one lowercase character
			validation_5 = bool(re.search(r'[a-z]+', password))		

			if not validation_1:
				raise forms.ValidationError(
						'Password must be atleast 8 characters long!'
					)
			if not validation_2:
				raise forms.ValidationError(
						'Passwords do not match!'
					)
			if not validation_3:
				raise forms.ValidationError(
						'Password must contain atleast one number!'
					)
			if not validation_4:
				raise forms.ValidationError(
						'Password must contain atleast one uppercase character!'
					)
			if not validation_5:
				raise forms.ValidationError(
						'Password must contain atleast one lowercase character!'
					)

		clean_username(self)
		clean_email(self)
		clean_password(self)
