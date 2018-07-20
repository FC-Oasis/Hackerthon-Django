from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, render

from ..forms import SignupForm

User = get_user_model()

__all__ = (
    'signup',
)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.signup()
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)


