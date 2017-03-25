from django.shortcuts import render
import mongoengine
# Create your views here.
user=authenticate(username=username,password=password)
assert isinstance(user,mongoengine.django.auth.User)