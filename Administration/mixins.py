from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group

class OwnerOnlyUpdateMixin(UserPassesTestMixin):
    
    def test_func(self):
        obj = self.get_object()
        group = Group.objects.get(name="Admins")
        if group in self.request.user.groups.all() or obj.project.project_manager == self.request.user:
            return True 
        return obj.owner == self.request.user 
        
                