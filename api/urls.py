from .views import BankListAPIView, BranchNameListAPIView, AllBankListAPIView

from django.urls import path

urlpatterns = [
    path('branches/autocomplete/', BranchNameListAPIView.as_view()),
    path('branches/', BankListAPIView.as_view()),
    # path('allbanks/', AllBankListAPIView.as_view())
]
