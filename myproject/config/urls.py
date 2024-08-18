from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import include
from .views import hello_world
from .views import hello_japan
from .views import FirstClassBaseView
from .views import CompanyDetailView
from .views import IndexView
from .views import FileUploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', hello_world),
    path('hellojapan/', hello_japan),
    path('first-class-base', FirstClassBaseView.as_view()),
    path('company-detail/', CompanyDetailView.as_view()),
    path('review/', include('review.urls')),
    path('account/', include('account.urls')),
    path('', IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
]
