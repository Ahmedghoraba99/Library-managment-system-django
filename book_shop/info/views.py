from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about_us(request):
    return HttpResponse("<h1>About Us</h1>")
    # return render(request, 'about_us.html') 
def contact_us(request):
    return HttpResponse("<h1>Contact Us</h1>")

def frequently_asked_questions(request):
    return HttpResponse("<h1>Frequently Asked Questions</h1>")