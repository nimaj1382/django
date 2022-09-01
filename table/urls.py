from django.urls import path
from . import views

urlpatterns = [
        path('' , views.red , name = "redirect"),
        path('<int:page>/' , views.index , name = "index"),
        path('kar<int:id>/' , views.detail , name = "detail"),
]
