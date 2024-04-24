from django.db import models
from decimal import Decimal

class TechHiveDeparments(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department_name
    
class Section(models.Model):
    department = models.ForeignKey(TechHiveDeparments, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=100, blank=False, unique=True)
    short_description = models.CharField(max_length=100, blank=False, unique=True)
    full_description = models.CharField(max_length=1500, blank=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.section_name
    
class Payment(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Price for {self.section.section_name} = {self.price}"
    
class Discount(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    discount = models.BooleanField(default=False)
    discount_percent = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def set_discount(self, amount):
        if self.discount:
            self.discount_percent = amount
            self.payment.price = self.payment.price - self.discount_percent
            self.payment.save()

class Promotions(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name='promotion', null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    percentage = models.DecimalField(decimal_places=2, max_digits=5, default=0)

    def apply_promotion(self):
        if not self.payment.discount:
            self.payment.price = self.payment.price * (1 - self.percentage / 100)
            self.payment.save()