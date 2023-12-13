from django.shortcuts import render

# Create your views here.
def fortune(request):
    return render(request, "randomfortune/fortune.html")