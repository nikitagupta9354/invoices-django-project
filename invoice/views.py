from rest_framework import generics
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer


class InvoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetailListCreateAPIView(generics.ListCreateAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer


class InvoiceDetailRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
