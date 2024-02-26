from django.urls import path
from .views import *

urlpatterns = [
    path("invoices/", InvoiceListCreateAPIView.as_view(), name="invoice-list-create"),
    path(
        "invoices/<int:pk>/",
        InvoiceRetrieveUpdateDestroyAPIView.as_view(),
        name="invoice-detail",
    ),
    path(
        "invoice_details/",
        InvoiceDetailListCreateAPIView.as_view(),
        name="invoice-detail-list-create",
    ),
    path(
        "invoice_details/<int:pk>/",
        InvoiceDetailRetrieveUpdateDestroyAPIView.as_view(),
        name="invoice-detail-detail",
    ),
]
