from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# def testindex(request):
#     return render(request, 'testindex.html')

def screen(request, id):
    return render(request, 'screen.html', {'id': id})

def testweb(request):
    return render(request, 'testweb.html')