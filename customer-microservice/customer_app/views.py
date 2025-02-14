import json

from customer_project.serializer import (CustomerChargeLogSerializer,
                                         CustomerDisplaySerializer,
                                         CustomerSerializer, PenaltySerializer)
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .decorations import validate_internal_jwt, validate_jwt
from .models import Customer, CustomerChargeLog, Penalty


# View to list and create customers
@method_decorator(validate_jwt, name='dispatch')
@method_decorator(validate_jwt, name='dispatch')
class CustomerListView(APIView):
    def get(self, request, *args, **kwargs):
        # Retrieve all customers and serialize them
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def post(self, request,*args, **kwargs):
      
        cvid = request.data.get("cvid")
        if cvid:
            customer = Customer.objects.get(pk=cvid)
            serializer = CustomerSerializer(customer, data=request.data)
        else:
            serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("OK", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(validate_internal_jwt, name='dispatch')   
class CustomerInternalView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerDisplaySerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



# View to retrieve and delete a specific customer
@method_decorator(validate_jwt, name='dispatch')
class CustomerDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        # Retrieve a specific customer by primary key (pk)
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerDisplaySerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk, *args, **kwargs):
        # Delete a specific customer by primary key (pk)
        try:
            customer = Customer.objects.get(pk=pk)
            customer.delete()
            return Response("Deleted", status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@method_decorator(validate_jwt, name='dispatch')
# View to update a specific customer
@method_decorator(validate_jwt, name='dispatch')
class CustomerUpdateView(APIView):
    def put(self, request, pk, *args, **kwargs):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to list and create customer charge logs
@method_decorator(validate_jwt, name='dispatch')
class CustomerChargeLogListView(APIView):
    def get(self, request, *args, **kwargs):
        # Retrieve all customer charge logs and serialize them
        charge_logs = CustomerChargeLog.objects.all()
        serializer = CustomerChargeLogSerializer(charge_logs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create a new customer charge log
        serializer = CustomerChargeLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("OK", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to retrieve, update, and delete a specific charge log
@method_decorator(validate_jwt, name='dispatch')
class CustomerChargeLogDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        # Retrieve a specific charge log by primary key (pk)
        try:
            charge_log = CustomerChargeLog.objects.get(pk=pk)
            serializer = CustomerChargeLogSerializer(charge_log)
            return Response(serializer.data)
        except CustomerChargeLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
        # Update a specific charge log by primary key (pk)
        try:
            charge_log = CustomerChargeLog.objects.get(pk=pk)
            serializer = CustomerChargeLogSerializer(charge_log, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("OK", status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomerChargeLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk, *args, **kwargs):
        try:
            charge_log = CustomerChargeLog.objects.get(pk=pk)
            serializer = CustomerChargeLogSerializer(charge_log, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomerChargeLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk, *args, **kwargs):
        # Delete a specific charge log by primary key (pk)
        try:
            charge_log = CustomerChargeLog.objects.get(pk=pk)
            charge_log.delete()
            return Response("Deleted", status=status.HTTP_204_NO_CONTENT)
        except CustomerChargeLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# View to list and create penalties
@method_decorator(validate_jwt, name='dispatch')
class PenaltyListView(APIView):
    def get(self, request, *args, **kwargs):
        # Retrieve all penalties and serialize them
        penalties = Penalty.objects.all()
        serializer = PenaltySerializer(penalties, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create a new penalty
        serializer = PenaltySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to retrieve, update, and delete a specific penalty
@method_decorator(validate_jwt, name='dispatch')
class PenaltyDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        # Retrieve a specific penalty by primary key (pk)
        try:
            penalty = Penalty.objects.get(pk=pk)
            serializer = PenaltySerializer(penalty)
            return Response(serializer.data)
        except Penalty.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
        # Update a specific penalty by primary key (pk)
        try:
            penalty = Penalty.objects.get(pk=pk)
            serializer = PenaltySerializer(penalty, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("OK", status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Penalty.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk, *args, **kwargs):
        try:
            penalty = Penalty.objects.get(pk=pk)
            serializer = PenaltySerializer(penalty, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Penalty.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        # Delete a specific penalty by primary key (pk)
        try:
            penalty = Penalty.objects.get(pk=pk)
            penalty.delete()
            return Response("Deleted", status=status.HTTP_204_NO_CONTENT)
        except Penalty.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@method_decorator(validate_jwt, name='dispatch')
class BalanceView(APIView):
    def get(self, request, *args, **kwargs):
        # Retrieve balance for the authenticated customer
        customer = request.user.customer
        return Response({"balance": customer.cvbalance}, status=status.HTTP_200_OK)

@method_decorator(validate_jwt, name='dispatch')
class RechargeBalanceView(APIView):
    def post(self, request, *args, **kwargs):
        amount = request.data.get("amount", 0)
        if amount <= 0:
            return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)
        
        customer = request.user.customer
        customer.cvbalance += amount
        customer.save()

        CustomerChargeLog.objects.create(cvidcustomer=customer, cvvalue=amount)
        return Response({"message": "Balance recharged successfully"}, status=status.HTTP_200_OK)
    