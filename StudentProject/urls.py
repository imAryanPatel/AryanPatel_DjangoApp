from django.contrib import admin
from django.urls import path
from app1.views import home, app1_page
from app2.views import app2_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('app1/', app1_page, name='app1_page'),
    path('app2/', app2_page, name='app2_page'),
]
