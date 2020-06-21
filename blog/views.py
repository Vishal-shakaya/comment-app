from django.shortcuts import render
from blog.models import Post
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from django.views.generic.edit import  FormMixin, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from braces.views import FormMessagesMixin


class Home(TemplateView):
	template_name ='base.html'


class ListView(ListView):
	context_object_name = 'post_list'
	template_name = 'post_list.html'
	model = Post
	success_url = reverse_lazy('Post_app:post_list')


class CreateView(CreateView):
	template_name = 'post_create.html'
	model = Post
	fields =['author','title','body']

class DetailView(DetailView):
	context_object_name = 'posts'
	template_name = 'post_detail.html'
	model = Post


class SIGN_UP(FormMessagesMixin,SuccessMessageMixin,CreateView):
	template_name = 'signup.html'
	class_form = UserCreationForm
	success_url = reverse_lazy('login')
	form_valid_message = "Blog post created!"
	form_invalid_message = " Failed to Blog post created!"

