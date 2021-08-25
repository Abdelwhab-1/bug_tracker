from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import resolve
class DemoNoSave(LoginRequiredMixin):
    
    def pass_with_out_save(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_demo:
            self.form_valid = self.pass_with_out_save
        return super().dispatch(request, *args, **kwargs)



