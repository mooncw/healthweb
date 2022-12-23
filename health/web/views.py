from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# def testindex(request):
#     return render(request, 'testindex.html')

def screen(request, id):
    return render(request, 'screen.html', {'id': id})

def testweb(request):
    return render(request, 'testweb.html')

def testweb2(request):
    return render(request, 'testweb2.html')

def testweb3(request):
    return render(request, 'testweb3.html')