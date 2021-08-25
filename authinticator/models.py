from django.db import models
from django.contrib.auth.models import PermissionsMixin, Permission
from django.contrib.auth.base_user import AbstractBaseUser
from .models_manager import UserManager 
from .utilities import get_sentinel_user 
from django.utils.translation import gettext as _
from django.core.files.storage import FileSystemStorage
# Create your models here.


roles = [
    ('A','Admin'),
    ('D','Developer'),
    ('N','Normal'),
]




class User(AbstractBaseUser, PermissionsMixin): 
    email = models.EmailField(_('email address'), unique=True)
    active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_demo = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    EMAIL_FILED = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    
    @property
    def is_active(self):
        return self.active 


    @property
    def is_staff(self):
        return self.is_admin


    def has_module_perms(self, app_label):
       return self.is_admin


    def has_perm(self, perm, obj=None):
        
        return self.is_admin


    def __str__(self): 
        return self.email



    def has_perms(self, perm, obj=None):
        gruop_perissions = self.get_group_permissions()
        user_permissions = self.get_user_permissions()
        print('=========================================')
        print(perm)
        for per in perm: 
            print(per)
            if per not in gruop_perissions :
                if per not in user_permissions:
                    return False
        return True 

image_fs = FileSystemStorage(location='/home/abdo/Documents/pyweb/dj_web/bug_tracking/bug_trackingts/media/profile')
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    first_name = models.CharField(max_length=127) 
    last_name = models.CharField(max_length=127)
    role = models.CharField(max_length=1, choices=roles)
    image = models.ImageField(upload_to='profils/%Y/%m/%d ', blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self): 
        return self.full_name

    def create(cls, user, first_name, last_name):
        profile = cls(user=user, first_name=first_name, last_name=last_name)
        profile.save()
        return profile 