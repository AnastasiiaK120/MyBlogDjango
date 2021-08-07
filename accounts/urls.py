from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUPView.as_view(), name='signup'),
]