from django.db import models
from django.core.validators import MinValueValidator


class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Invoice #{self.pk}"



class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(
        Invoice, related_name="details", on_delete=models.CASCADE
    )
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Detail for Invoice #{self.invoice.pk}: {self.description}"

