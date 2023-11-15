from django.shortcuts import render

def kaito(request):
    return render(request, 'camera/kaito.html', {})
