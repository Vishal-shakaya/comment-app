
from django.urls import path,include
from blog import views

app_name = 'Post_app'

urlpatterns = [
    path('post-list/',views.ListView.as_view(),name='post_list'),
    path('post-create/',views.CreateView.as_view(),name='create'),
    path('post-detail/<pk>/',views.DetailView.as_view(),name='detail'),

]
