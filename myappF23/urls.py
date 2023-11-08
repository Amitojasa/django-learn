from django.urls import path
from myappF23 import views

app_name = 'myappF23'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'courses/', views.courses, name='courses'),
    path(r'test/<int:pk>', views.TestView.as_view(), name='test-detail'),
    path(r'<int:category_no>/', views.detail, name='detail'),
    path(r'instructor/<int:instructor_id>/', views.instructor_detail, name='instructor_detail'),
]
