from django.urls import path 
from .views import * 
urlpatterns = [
    path('api/teachers1/', listar_professores), 
    path('api/teachers/', TeacherAPIView.as_view(), name = 'teachers_api'), 
    path('api/teachers/<str:teacher>/', TeacherAPIView.as_view(), name='get_or_update_teacher'),
    path('api/teacher1/', TheachersView.as_view()),
    path('api/teachers1/<int:pk>/', TeachersDetailView.as_view()),
    path('api/teachers/<int:pk>/', TeacherAPIView.as_view())
]
