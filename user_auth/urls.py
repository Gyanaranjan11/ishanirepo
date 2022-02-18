from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from pgbooking import settings
from .views import home, login,logout, signup, welcom_user, sociallogin
from user_auth import views

urlpatterns = [
    path('', home, name='home'),
    path('profile', views.profile, name='profile'),
    path('login', login, name='login'),
    path('w_login', views.woner_login, name='w_login'),
    path('sociallogin', sociallogin, name='sociallogin'),
    path('logout', logout, name='logout'),
    path('log_out', LogoutView.as_view(), name='log_out'),
    path('signup', signup, name='signup'),
    path('welcom', welcom_user, name='welcom'),
    path('accounts/', include('allauth.urls')),
    path('edit_bd', views.edit_bd, name='edit_bd'),
    path('edit_ad/<int:id>/', views.edit_ad, name='edit_ad'),
    path('edit_photo', views.edit_photo, name='edit_photo'),
    path('forgot_pass/', views.forgot_password, name='forgot_pass'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)