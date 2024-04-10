from typing import Iterable
from django.db import models
import secrets


class PaymentNumber(models.Model):
    payment_number = models.CharField(max_length=15, default='0243174494')

    def __str__(self) -> str:
        return self.payment_number

class Payment(models.Model):
    payment_number = models.ForeignKey(PaymentNumber, on_delete = models.CASCADE)
    amount = models.PositiveIntegerField()
    reference = models.CharField(max_length=50)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_paid = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_paid', )
    
    def __str__(self) -> str:
        return f'Paymet: {self.amount}, Email: {self.email}'
    
    def save(self, *args, **kwargs) -> None:
        while not self.reference:
            reference = secrets.token_urlsafe(20)
            object_with_similar_ref = Payment.objects.filter(reference=reference)
            if not object_with_similar_ref:
                self.reference = reference
            
        return super().save(*args, **kwargs)
    
    def amountValue(self) -> int:
        return self.amount * 100
    
    def verifyPayment(self):
        Paystack = Payment()
        status, result = Paystack.verifyPayment(self.reference, self.amount)
        if status:
            if result ['amount']/100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
