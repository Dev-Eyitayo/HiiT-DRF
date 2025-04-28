from django.urls import path
from .views import LoginView, SignUpView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('refresh-token/', TokenRefreshView.as_view()),
]


