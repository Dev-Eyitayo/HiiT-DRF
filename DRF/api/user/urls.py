from django.urls import path
from .views import UserHomeView, UserFanView, UserSchoolView

urlpatterns = [
    path('home/', UserHomeView.as_view(), name='home'),
    path('school/', UserSchoolView.as_view(), name='school'),
    path('fan/', UserFanView.as_view(), name='fan'),
]
