from django.urls import path
from . import views

urlpatterns = [
        path('' , views.red , name = "redirect"),
        path('<int:page>/' , views.index , name = "index"),
        path('job<int:id>/' , views.detail , name = "detail"),
        path('logout/' , views.logout , name = 'logout'),
        path('addjob/' , views.addjob , name = 'addjob'),
]
