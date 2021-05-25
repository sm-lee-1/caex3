from django.views.generic import TemplateView

from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied

#--- Homepage
class HomeView(TemplateView):
    template_name = 'home.html'




class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)






