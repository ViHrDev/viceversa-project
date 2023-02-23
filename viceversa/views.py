from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def reverse(request):
    get_r = request.GET['usertext']
    r_get = get_r[::-1]
    return render(request, 'reverse.html', {'usertext' : get_r, 'reversedtext' : r_get})
