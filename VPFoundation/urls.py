from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('joinform/',views.joinform,name="joinForm"),
    path('validateUser/',views.validateUser,name="validateUser"),
    path('needhelp/',views.needhelp,name="needhelp"),
    path('contact/',views.contact,name='contact'),
] 
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)