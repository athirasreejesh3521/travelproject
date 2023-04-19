from django.shortcuts import render
from. models import official
# Create your views here.
def demo(request):
    obj=official.objects.all()
    return render(request,"index.html",{'result':obj})
