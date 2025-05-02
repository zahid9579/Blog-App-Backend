from django.urls import path
from .views import RegisterView, LoginView, LogoutView, CreatePostView, GetAllPostsView, UpdatePostView, DeletePostView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Token based Authentication
    path("api-token-auth/", obtain_auth_token),
    path('auth/register', RegisterView.as_view(), name="register"),
    path('auth/login', LoginView.as_view(), name="login"),
    path('auth/logout', LogoutView.as_view(), name="logout"),
     
    # Blog CRUD
    path('blog/create', CreatePostView.as_view(), name='create-post'),
    path('blog/getallposts', GetAllPostsView.as_view(), name='get-all-post'),
    path('blog/update/<int:pk>/', UpdatePostView.as_view(), name='update'),
    path('blog/delete/<int:pk>/', DeletePostView.as_view(), name="delete")
    
    

]
