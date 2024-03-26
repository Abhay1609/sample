from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupCreateAPIView
from .views import StudentViewSet, TeacherViewSet, StudentDetailsViewSet, TeacherDetailsViewSet, BatchViewSet, RoleViewSet, SubjectViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'student-details', StudentDetailsViewSet)
router.register(r'teacher-details', TeacherDetailsViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-group/', GroupCreateAPIView.as_view(), name='create_group'),
]
