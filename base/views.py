from django.shortcuts import render


# Create your views here.
def index(request):
    if "recently_viewed" in request.session:
        del request.session["recently_viewed"]
    return render(request, "index.html")
