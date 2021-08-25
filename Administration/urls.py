from django.urls import path 
from .views import CreateProject, UpdateProject, DeletProject, ManageRoles
app_name='administration'
urlpatterns = [
    path('projects/create/', CreateProject.as_view(), name='create_project'),
    path('projects/<int:pk>/edit/', UpdateProject.as_view(), name='update_project'),
    path('projects/delete/<int:pk>/', DeletProject.as_view(), name='delete_project'),
    path('manage_roles/', ManageRoles.as_view(), name='manage_roles'),
]