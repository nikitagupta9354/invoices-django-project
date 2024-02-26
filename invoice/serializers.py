from rest_framework import serializers
from .models import Invoice, InvoiceDetail


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ["id", "invoice", "description", "quantity", "unit_price", "price"]
        read_only_fields = ["id"]


class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ["id", "date", "customer_name", "details"]
        read_only_fields = ["id"]
