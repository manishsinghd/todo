from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ListForm
from .models import List
from django.contrib import messages
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordrepeat = request.POST['passwordrepeat']
        # if len(username) > 10:
        #     messages.error(request, 'usermame must under 10 charactor')
        #     return redirect('register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                        password=password,
                                        email=email)
        user.save();
        messages.success(request, f'Account created for {username}!')
        return redirect('/')

        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     messages.success(request, f'Account created for {username}!')

    else:
        # form = UserRegisterForm()
        return render(request, 'users/register.html')

def dashboard(request):
    if request.user.is_authenticated:
        user = User.objects.filter(user=rahul123)
        user.profile
        return render (request,'users/profile', {'all_items': all_items})
@login_required
def profile(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(request, 'users/profile.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'users/profile.html', {'all_items': all_items})


@login_required
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("icvbnbvb"))
    return redirect('profile')

@login_required
def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    messages.success(request, ("icvbnbvb"))
    return redirect('profile')

@login_required
def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    messages.success(request, ("icvbnbvb"))
    return redirect('profile')

@login_required
def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('profile')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'users/edit.html', {'item': item})
