
from django.urls import path
from users.views import CustomTokenRefreshView, MyTokenObtainPairView, UserCreate, UsersList

urlpatterns = [
    path('', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    path('user-list/', UsersList.as_view()),
    path('create/', UserCreate.as_view()),
]
