from .views import load_data, testing, BankListAPIView

from django.urls import path

urlpatterns = [
    path('branches/autocomplete/', testing),
    path('branches/', BankListAPIView.as_view()),
    # path('loaddata/', load_data)
]
