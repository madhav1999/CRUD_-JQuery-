from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Sample
from .forms import printform
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


def first(request):
    form = printform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/details")
    return render(request, 'dboperations/index.html', {'form': form})


def listview(request):
    context = {}
    context['data'] = Sample.objects.all()
    return render(request, 'dboperations/listview.html', context)


def detailsview(request, id):
    context = {}
    context['data'] = Sample.objects.get(id=id)
    return render(request, 'dboperations/detailsview.html', context)


@login_required(login_url='/login')
def updateview(request, id):
    print(request.POST['Name'])
    print(id)
    context = {}
    # obj = get_object_or_404(Sample, id=id)
    # form = printform(request.POST or None, instance=obj)
    # if form.is_valid():
    #     t = form.save(commit=False)
    #     t.save()
    #     return HttpResponseRedirect("/details")
    # context['form'] = form
    return render(request, 'dboperations/updateview.html', context)


def deleteview(request, id):
    context = {}
    obj = get_object_or_404(Sample, id=id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/details")
    return render(request, 'dboperations/deleteview.html', context)


class signup(CreateView):
    form_class = UserCreationForm
    template_name = "dboperations/signupview.html"
    success_url = "/details"


class login(LoginView):
    template_name = 'dboperations/login.html'


class logout(LogoutView):
    template_name = 'dboperations/logout.html'
