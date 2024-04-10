from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from .forms import PaymentForm
from .models import Payment
from django.contrib import messages

def initiatePayment(request: HttpRequest) -> HttpRequest:
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'payment/make_payment.html', {'payment': payment})
    else:
        payment_form = PaymentForm()
    
    return render(request, 'payment/initiate_payment.html')

def verifyPayment(request: HttpRequest, reference: str):
    payment = get_object_or_404(Payment, reference=reference)
    verified = payment.verifyPayment()
    if verified:
        messages.success(request, 'Verification Succesful!')
    else:
        messages.error(request, 'Veirfication Failed!')
    return redirect(initiatePayment)