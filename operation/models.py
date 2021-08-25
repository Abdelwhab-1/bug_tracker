from django.db import models
from authinticator.utilities import get_sentinel_user
# Create your models here.
class Project(models.Model): 
    project_manager = models.ForeignKey("authinticator.User", on_delete=models.PROTECT, related_name='manager')
    developers = models.ManyToManyField("authinticator.User")
    title = models.CharField(max_length=263)
    descreption = models.TextField()
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True)
    url = models.URLField(max_length=1023)

    def __str__(self):
        return self.title 

statuses = [
    ("N", "new"),
    ("I", "in progress"),
    ("U", "updated"),
    ("R", "resolved")
]

priorities = [
    ("L", "low"),
    ("M", "medium"),
    ("H", "high"),

]

types = [
    ("Q", "question"),
    ("I", "Issue"),
    ("B", "bug"),
    ("D", "idea"),
    ("F", "feature wanted")
]

class Ticket(models.Model): 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(to='authinticator.User', on_delete=models.SET(get_sentinel_user), default=0)
    assigned_developer = models.ForeignKey("authinticator.User", on_delete=models.SET(get_sentinel_user),
        null=True, blank=True, related_name='assigned_tickets')
    creation_time = models.DateTimeField(auto_now_add=True)
    solved = models.BooleanField(default=False)
    solution_time = models.DateTimeField(blank=True, null=True)
    body = models.TextField()
    title = models.CharField(max_length=263)
    status = models.CharField(max_length=1, choices=statuses, default="N") 
    priority = models.CharField(max_length=1, choices=priorities, default="L") 
    kind = models.CharField(max_length=1, choices=types, default='Q') 
    last_update = models.DateTimeField(auto_now_add=True)


    def __str__(self): 
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(to="authinticator.User", on_delete=models.DO_NOTHING, null=False)
    project = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    replies_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    solution_to = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, related_name='solution', blank=True, null=True)
    body = models.TextField()
    

    def __str__(self): 
        return self.body[:50]


