from django.shortcuts import render
from .models import User
from .forms import UserForm


def home(request):
	context = {}
	form = UserForm()
	if request.method=='POST' and request.FILES['photo']:
		form = UserForm(request.POST, request.FILES)
		
		if form.is_valid():
			user = form.save()
	
		return render(request,
					'home.html',
					{
						'form': form,
						'user_photo_url': user.photo.url
					})

	return render(request,
				'home.html',
				{'form':form})


