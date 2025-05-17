from django.shortcuts import render, redirect
from .models  import imageSignup
from .models import ImageOneSign
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import imageSignup, ImageOneSign
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def signup_login(request):
    image = imageSignup.objects.first()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('homepage')
        else:
                print("Form is invalid or credentials are incorrect. ")
    else:
        form = AuthenticationForm()
    context = {'image':image, 'form': form}
    return render(request, "signup_login.html", context)
def signup(request):
    Store_image = ImageOneSign.objects.first()
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('signup_login')
    context = {
        'storeImage' : Store_image,
        'form' : form
    }
    return render(request, 'signup.html', context)