from django.urls import path
from .views import RegisterView, LoginView, LogoutView, CreatePostView, GetAllPostsView

urlpatterns = [
    # User Authentication
    path('auth/register', RegisterView.as_view(), name="register"),
    path('auth/login', LoginView.as_view(), name="login"),
    path('auth/logout', LogoutView.as_view(), name="logout"),
     
    # Blog CRUD
    path('blog/create', CreatePostView.as_view(), name='create-post'),
    path('blog/getAll', GetAllPostsView.as_view(), name='get-all-post'),
    
    
    
    

]
