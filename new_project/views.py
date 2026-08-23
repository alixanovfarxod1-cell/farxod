
from django.shortcuts import render
from .models import News, Contact

def news(request):
  news = News.objects.all()
  return render(request, 'farxod.html', {'news': news})

def  home_page_view(request):
  return render(request, 'index.html', context={})

def page_error_404(request):
  return render(request, '404.html', context={})

def contact(request):
    if request.method == "POST":
      name = request.POST.get("name")
      email = request.POST.get("email")
      message = request.POST.get("message")

      Contact.objects.create(
        name=name,
        email=email,
        message=message
      )

      return render(request, "contact.html", {
        "success": "Xabaringiz yuborildi!"
      })

    return render(request, "contact.html")


def about(request):
  context = {}
  return render(request, "about.html")