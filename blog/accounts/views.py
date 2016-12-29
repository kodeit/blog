from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView, RedirectView, CreateView


class LoginView(FormView):

    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    home_url = reverse_lazy('posts:post-list')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # Already logined, redirect to home page
            return HttpResponseRedirect(self.home_url)
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):

        if 'next' in self.request.POST:
            return self.request.POST.get('next')
        return self.home_url

    @method_decorator(cache_page(1000 * 60 * 2))
    @method_decorator(csrf_protect)
    def get(self, *args, **kwargs):
        return super(LoginView, self).get(*args, **kwargs)


class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    home_url = reverse_lazy('posts:post-list')
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # Already logined, redirect to home page
            return HttpResponseRedirect(self.home_url)
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    @method_decorator(cache_page(1000 * 60 * 2))
    @method_decorator(csrf_protect)
    def get(self, *args, **kwargs):
        return super(RegisterView, self).get(*args, **kwargs)


class LogoutView(RedirectView):

    url = reverse_lazy('posts:post-list')

    def get(self, request, *args, **kwargs):

        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
