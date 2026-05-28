from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Register
from .models import Photo
user_data={}

# views.py

from django.shortcuts import render, redirect
from .models import Register


def index(request):

    error = ""

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # username check
        user_name_check = Register.objects.filter(
            username=username
        ).first()

        if not user_name_check:
            error = "Username Incorrect"

        else:

            # password check
            password_check = Register.objects.filter(
                username=username,
                password=password
            ).first()

            if not password_check:
                error = "Password Incorrect"

            else:
                return redirect('home')

    return render(request, 'index.html', {'error': error})


def home(request):

    photos = Photo.objects.all()

    return render(request, 'home.html', {
        'photos': photos
    })

def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # SAVE DATA
        Register.objects.create(
            username=username,
            password=password
        )

        return redirect('index')

    return render(request, 'register.html')


def photo_detail(request, id):

    photo = get_object_or_404(Photo, id=id)

    return render(request, 'photo_detail.html', {

        'photo': photo
        
    })
