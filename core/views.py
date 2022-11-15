from django.contrib import messages
from .models  import EventMetherologic
from .forms import EventMetherologicForms
from django.shortcuts import render, redirect


def register_metherelogic(request):
    data = {'form': EventMetherologicForms()}
    if request.method == 'POST':
        form = EventMetherologicForms(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Register the form success!!!')
            return redirect(to='query_metherelogic')
    return render(request, 'register_metherelogic.html', data)

def query_metherelogic(request):
    events = EventMetherologic.objects.all()
    return render(request, 'query_metherelogic.html', {'events': events})
