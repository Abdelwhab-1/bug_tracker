from django.urls import path 
from .views import (ProjectsView, ProjectView, TicketView, TicketUpdate, UserProjects, 
    CreateTicket, UserTickets,ProfileUpdate, ViewProfile)
app_name = 'operation'
urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='projects'), 
    path('projects/<int:pk>/', ProjectView.as_view(), name='project_details'),
    path('my_projects/', UserProjects.as_view(), name='user_projects'),
    path('projects/<int:pk>/create_ticket', CreateTicket.as_view(), name='create_ticket'),


    path('my_tickets', UserTickets.as_view(), name='user_tickets'),
    path('ticket/<int:pk>/', TicketView.as_view(), name='view_ticket'),
    path('ticket/edit/<int:pk>/', TicketUpdate.as_view(), name='update_ticket'), 
    path('ticket/<int:pk>/add_comment', TicketUpdate.as_view(), name='add_comment'),


    path('profile/<int:pk>/', ViewProfile.as_view(), name='view_profile'), 
    path('my_profile/edit', ProfileUpdate.as_view(), name='update_profile'),

    
]
 