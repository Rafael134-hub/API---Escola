from django.urls import path 
from .views import * 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('teachers1/', listar_professores), 
    path('teachers/', TeacherAPIView.as_view(), name = 'teachers_api'), 
    path('teachers/<str:teacher>/', TeacherAPIView.as_view(), name='get_or_update_teacher'),
    path('teacher1/', TheachersView.as_view()),
    path('teachers1/<int:pk>/', TeachersDetailView.as_view()),
    path('teachers/<int:pk>/', TeacherAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

