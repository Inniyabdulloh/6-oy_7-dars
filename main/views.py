from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from .models import SocialMedia, HomePageDate, Contact, CustomUser
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

class HomeView(View):
    def get(self, request):
        social_media = SocialMedia.objects.all()
        dates = HomePageDate.objects.all()
        context = {'social_media': social_media, 'dates': dates}
        return render(request, 'index.html',context)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            return redirect('main:home')

        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')




class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        full_name = request.POST['full-name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact.objects.create(fullname=full_name, email=email, message=message)
        contact.save()
        messages.success(request, "Xabaringiz jo'natildi")
        return redirect("main:home")


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        full_name = request.POST['full-name']
        username = request.POST['username']
        password = request.POST['password']


        user = CustomUser.objects.create(fullname=full_name, username=username, password=password)
        user.set_password(password)
        user.save()

        messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz")
        return redirect("main:home")


class PasswordResetView(View):
    def get(self, request):
        return render(request, 'password-reset.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = CustomUser.objects.get(username=username)
        user.set_password(password)

        user.save()
        messages.success(request, "Password tiklandi")
        return redirect("main:home")


class NotFoundView(View):
    def get(self, request):
        return render(request, '404.html')