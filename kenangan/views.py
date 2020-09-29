from django.shortcuts import render


# Create your views here.
def dashboard(request):
    context = {}
    return render(request, 'kenangan/dashboard.html', context)


def balai(request):
    context = {}
    return render(request, 'kenangan/balai.html', context)


def paket(request):
    context = {}
    return render(request, 'kenangan/paket.html', context)
