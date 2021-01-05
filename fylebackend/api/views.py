import os
from django.conf import settings
from django.http import HttpResponse
import pandas as pd
from .models import Bank
from .serializers import BankSerializer
from rest_framework.generics import ListAPIView


def load_data(request):
    Bank.objects.all().delete()
    df = pd.read_csv(os.path.join(settings.BASE_DIR, "datasets", "bank_branches.csv"), sep=',')
    for i in range(len(df)):
        _, created = Bank.objects.update_or_create(
            ifsc=df.iloc[i][0],
            bank_id=df.iloc[i][1],
            branch=df.iloc[i][2],
            address=df.iloc[i][3],
            city=df.iloc[i][4],
            district=df.iloc[i][5],
            state=df.iloc[i][6],
            bank_name=df.iloc[i][7]
        )
    return HttpResponse(status=204)


def testing(request):
    return HttpResponse(status=204)


class BankListAPIView(ListAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()