from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import FormView, RedirectView, CreateView


class LoginView(FormView):

    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):

        if 'next' in self.request.POST:
            return self.request.POST.get('next')
        return reverse_lazy('posts:post-list')


class RegisterView(CreateView):

    success_url = reverse_lazy('accounts:login')
    form_class = UserCreationForm
    template_name = 'accounts/register.html'


class LogoutView(RedirectView):

    url = reverse_lazy('posts:post-list')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
