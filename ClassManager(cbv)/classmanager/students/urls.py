from django.urls import path
from .views import StudentView, StudentDetailView, StudentAddView, StudentEditView, StudentDelView


urlpatterns = [
    path('student_list/', StudentView.as_view(), name='student_list'),
    path('<int:pk>', StudentDetailView.as_view(), name='student_detail'),
    path('add/', StudentAddView.as_view(), name='student_add'),
    path('edit/<int:pk>', StudentEditView.as_view(), name='student_edit'),
    path('del/<int:pk>', StudentDelView.as_view(), name='student_del'),
]