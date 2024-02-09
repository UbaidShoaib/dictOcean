from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactForm


def index(request):
    form = ContactForm()  # Instantiate your form
    return render(request, 'main.html', {'form': form})


def inner_page(request):
    return render(request, 'inner-page.html')


def portfolio_details(request):
    return render(request, 'portfolio-details.html')


def contact_view(request):
    if request.method == 'POST' and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Your message has been sent. Thank you!"})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"success": False, "errors": errors})
    else:
        form = ContactForm()
    return JsonResponse({"success": False, "message": "Invalid request"})
