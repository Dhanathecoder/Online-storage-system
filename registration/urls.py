from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

admin.site.site_header = 'FILE STORAGE SYSTEM'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
    path('upload/', views.index, name="upload"),
    path('', views.index, name='index'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


