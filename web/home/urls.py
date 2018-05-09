from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('album/', views.album, name='album'),
    path('dangky/',views.dangky, name='dangky'),
    path('login/', auth_views.login,{'template_name':'login/login.html'},name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('upload/',views.model_form_upload, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)