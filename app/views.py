from django.shortcuts import render

from .forms import UserForm
from .models import User


def home(request):
    context = dict()
    form = UserForm()
    if request.method =='POST' and request.FILES['photo']:
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()

        return render(
            request, 'home.html',
            {
                'form': form,
                'user_photo_url': user.photo.url,
            },
        )

    return render(
        request, 'home.html',
        {
            'form': form,
        },
    )
