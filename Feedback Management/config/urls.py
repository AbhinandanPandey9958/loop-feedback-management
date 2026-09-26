"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]




# from django.contrib import admin
# from django.urls import path
# from reviews import views






from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from reviews.views import dashboard, add_feedback, edit_feedback, delete_feedback


urlpatterns = [

    path('admin/', admin.site.urls),

    # Login
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    # Dashboard
    path(
        '',
        dashboard,
        name='dashboard'
    ),

    # Feedback
    path(
        'add-feedback/',
        add_feedback,
        name='add_feedback'
    ),

    path(
        'edit-feedback/<int:id>/',
        edit_feedback,
        name='edit_feedback'
    ),

    path(
        'delete-feedback/<int:id>/',
        delete_feedback,
        name='delete_feedback'
    ),

    path(
    'logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
    ),

]