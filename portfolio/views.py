from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def budget(request):
    return render(request, 'budget.html')

def projects(request):
    return render(request, 'projects.html')

def submit_budget_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project_type = request.POST.get('projectType')
        project_details = request.POST.get('projectDetails')
        budget = request.POST.get('budget')
        deadline = request.POST.get('deadline')
        payment_method = request.POST.get('paymentMethod')
        payment_terms = request.POST.get('paymentTerms')

        subject = f"New Budget Request from {name}"
        message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Project Type: {project_type}
        Project Details: {project_details}
        Estimated Budget: {budget if budget else 'Not provided'}
        Project Deadline: {deadline if deadline else 'Not provided'}
        Preferred Payment Method: {payment_method if payment_method else 'Not provided'}
        Payment Terms: {payment_terms if payment_terms else 'Not provided'}
        """
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['moisessouzasantos001@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            # Redirect to a success page or display a success message
            return HttpResponseRedirect(reverse('budget_success'))
        except Exception as e:
            # Handle email sending error
            print(f"Error sending email: {e}")
            return render(request, 'budget.html', {'error_message': 'There was an error sending your request. Please try again later.'})
    return HttpResponseRedirect(reverse('budget'))

def budget_success(request):
    return render(request, 'budget_success.html')