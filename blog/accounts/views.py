from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import FormView, RedirectView, CreateView


class LoginView(FormView):

    success_url = '/'
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)


class RegisterView(CreateView):

    success_url = '/'
    form_class = UserCreationForm
    template_name = 'accounts/register.html'


class LogoutView(RedirectView):

    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
