from rest_framework.response import Response
from .models import Bank
from .serializers import BankSerializer
from rest_framework.generics import ListAPIView
from django.db import connection, transaction
from django.http import HttpResponse


# return all Bank objects

class AllBankListAPIView(ListAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()


# return possible matches across all columns and all rows,
# ordered by IFSC code (ascending order) with limit and offset.

class BankListAPIView(ListAPIView):
    serializer_class = BankSerializer

    def get_queryset(self, *args, **kwargs):
        q1 = self.request.GET.get("q")
        q2 = self.request.GET.get("limit")
        q3 = self.request.GET.get("offset")

        if q1 is None:
            q1 = ""

        if q2 is None or q2 == "" or q3 is None or q3 == "":
            empty_list = []
            return empty_list

        query = "SELECT * FROM api_bank WHERE \"ifsc\" LIKE '%" + q1 + "%'" + \
                " OR \"branch\" LIKE '%" + q1 + "%' OR \"address\" LIKE '%" + q1 + "%' OR \"city\" " \
                                                                                   "LIKE '%" + q1 + "%' OR \"district\" LIKE '%" + q1 + "%' OR \"state\" LIKE '%" + q1 + \
                "%' ORDER BY \"ifsc\" LIMIT " + q2 + " OFFSET " + q3

        cursor = connection.cursor()
        cursor.execute(query)
        transaction.commit()
        query_list2 = cursor.fetchall()

        query_set = []
        for i in query_list2:
            obj = Bank(ifsc=i[0], bank_id=i[1], branch=i[2], address=i[3], city=i[4], district=i[5], state=i[6])
            query_set.append(obj)
        return query_set

    def list(self, request, *args, **kwargs):
        q2 = self.request.GET.get("limit")
        q3 = self.request.GET.get("offset")
        if q2 is None or q2 == "" or q3 is None or q3 == "":
            return HttpResponse(status=422)

        queryset = self.get_queryset()
        serializer = BankSerializer(list(queryset), many=True)
        return Response(serializer.data)


# return possible matches based on the branch name ordered
# by IFSC code (ascending order) with limit and offset.

class BranchNameListAPIView(ListAPIView):
    serializer_class = BankSerializer

    def get_queryset(self, *args, **kwargs):
        q1 = self.request.GET.get("q")
        q2 = self.request.GET.get("limit")
        q3 = self.request.GET.get("offset")

        if q1 is None:
            q1 = ""

        if q2 is None or q2 == "" or q3 is None or q3 == "":
            empty_list = []
            return empty_list

        query = "SELECT * FROM api_bank WHERE \"branch\" LIKE '%" + q1 + "%' ORDER BY \"ifsc\" LIMIT " + q2 + " OFFSET " + q3
        cursor = connection.cursor()
        cursor.execute(query)
        transaction.commit()
        query_list2 = cursor.fetchall()

        query_set = []
        for i in query_list2:
            obj = Bank(ifsc=i[0], bank_id=i[1], branch=i[2], address=i[3], city=i[4], district=i[5], state=i[6])
            query_set.append(obj)
        return query_set

    def list(self, request, *args, **kwargs):
        q2 = self.request.GET.get("limit")
        q3 = self.request.GET.get("offset")
        if q2 is None or q2 == "" or q3 is None or q3 == "":
            return HttpResponse(status=422)

        queryset = self.get_queryset()
        serializer = BankSerializer(list(queryset), many=True)
        return Response(serializer.data)
