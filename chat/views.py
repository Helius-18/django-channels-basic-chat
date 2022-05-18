from django.shortcuts import redirect, render

# Create your views here.

def lobby(request,room_name):
    return render(request, 'chat/lobby.html',{"room_name":room_name,"user_name":request.GET.get('q', 'Anonymous')})

def front(request):
    if request.method=="POST":
        return redirect("/lobby/{}?q={}".format(request.POST["room_name"],request.POST["user_name"]))
    return render(request,"chat/front.html")