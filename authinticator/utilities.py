from django.apps import apps 

def get_sentinel_user():
    model = apps.get_model('authinticator', 'User')
    return model.objects.get_or_create(email='deleted@example.com',username='deleted')[0]