
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from tourism.views import index,single_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index-page'),
    path('customer/<int:pk>/', single_page,name='single-page'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
