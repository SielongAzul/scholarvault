from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authenticate_view
from useraccounts import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scholarship.urls')),
    path('register/', user_views.register, name="register"),
    path('login/', authenticate_view.LoginView.as_view(template_name = 'useraccounts/login.html'), name="register"),
    path('logout/', authenticate_view.LoginView.as_view(template_name = 'useraccounts/logout.html'), name="logout"),
]
