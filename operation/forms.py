from django import forms 
from .models import Ticket
from authinticator.models import Profile
class TicketFile(forms.ModelForm):

    class Meta:
        model = Ticket 
        fields = ['title', 'body', 'kind', 'priority']
    def back_door_save(self,commit, project, owner):
        ticket = super().save(commit=False)
        ticket.project = project
        ticket.owner = owner 
        ticket.save() 
        return ticket 

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm):
    email= forms.EmailField(required=True)


    
    class Meta:
        model = Profile 

        fields = ['first_name','last_name','image', ]
    def back_door_save(self,commit, project, owner):
        ticket = super().save(commit=False)
        ticket.project = project
        ticket.owner = owner 
        ticket.save() 
        return ticket 

    


    def __init__(self, *args, **kwargs): 
        
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == "email": 
                visible.initial = self.instance.user.email
        
