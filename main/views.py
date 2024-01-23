from django.shortcuts import render

# Create your views here.
def main (request):
    return render(request, 'index.html')

def services (request):
    return render(request, 'services.html')


def blog (request):
    return render(request, 'blog.html')

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
