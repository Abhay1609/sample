from rest_framework import viewsets
from .models import Student, Teacher, StudentDetails, TeacherDetails, Batch, Role, Subject, Department
from .serializers import StudentSerializer, TeacherSerializer, StudentDetailsSerializer, TeacherDetailsSerializer, BatchSerializer, RoleSerializer, SubjectSerializer, DepartmentSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Group
from .permissions import IsTeacherOrHODOrAdmin
from rest_framework import permissions
class CheckPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            group = user.groups.id  # Assuming user belongs to only one group
            if group and hasattr(view, 'permission_parameter'):
                specific_role = Role.objects.get(name=group.name)
                permissions = specific_role.permissions.all()
                permission_names = [permission.name for permission in permissions]
                return view.permission_parameter in permission_names
        return False
class GroupCreateAPIView(APIView):
    def post(self, request, format=None):
        # Extract data from request
        group_name = request.data.get('name')

        # Check if group name is provided
        if not group_name:
            return Response({'error': 'Group name is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if group with the same name already exists
        if Group.objects.filter(name=group_name).exists():
            return Response({'error': 'Group with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the group
        new_group = Group.objects.create(name=group_name)
        
        # Return success response
        return Response({'message': 'Group created successfully', 'id': new_group.id}, status=status.HTTP_201_CREATED)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [CheckPermission]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission_parameter = "StudentViewSet"

    def get_permissions(self):
        permission_classes = self.permission_classes 
        return [permission() for permission in permission_classes]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [CheckPermission]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission_parameter = "TeacherViewSet"

    def get_permissions(self):
        permission_classes = self.permission_classes 
        return [permission() for permission in permission_classes]
  

class StudentDetailsViewSet(viewsets.ModelViewSet):
    queryset = StudentDetails.objects.all()
    serializer_class = StudentDetailsSerializer
    permission_classes = [CheckPermission]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission_parameter = "StudentDetailsViewSet"

    def get_permissions(self):
        permission_classes = self.permission_classes 
        return [permission() for permission in permission_classes]

class TeacherDetailsViewSet(viewsets.ModelViewSet):
    queryset = TeacherDetails.objects.all()
    serializer_class = TeacherDetailsSerializer
    permission_classes = [CheckPermission]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission_parameter = "TeacherDetailsViewSet"

    def get_permissions(self):
        permission_classes = self.permission_classes 
        return [permission() for permission in permission_classes]


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [CheckPermission]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission_parameter = "BatchViewSet"

    def get_permissions(self):
        permission_classes = self.permission_classes 
        return [permission() for permission in permission_classes]

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [CheckPermission]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission_parameter = "RoleViewSet"

    def get_permissions(self):
        permission_classes = self.permission_classes 
        return [permission() for permission in permission_classes]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [CheckPermission]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission_parameter = "SubjectViewSet"

    def get_permissions(self):
        permission_classes = self.permission_classes 
        return [permission() for permission in permission_classes]





    

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [CheckPermission]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permission_parameter = "DepartmentViewSet"

    def get_permissions(self):
        permission_classes = self.permission_classes 
        return [permission() for permission in permission_classes]