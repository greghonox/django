from django.shortcuts import render
from .models  import EventMetherologic


def register_metherelogic(request):
    return render(request, 'register_metherelogic.html')

def query_metherelogic(request):
    events = EventMetherologic.objects.all()
    return render(request, 'query_metherelogic.html', {'events': events})
