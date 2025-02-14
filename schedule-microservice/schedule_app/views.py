import json
from datetime import date

from django.utils.decorators import method_decorator
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .decorations import validate_jwt
from .models import Association, Schedule
from .serializers import (AssociationDisplaySerializer, AssociationSerializer,
                          ScheduleSerializer)
from .utils import (make_internal_request, send_create_notification,
                    send_returned_notification)


@method_decorator(validate_jwt, name='dispatch')
class ScheduleListView(APIView):
    def get(self, request, *args, **kwargs):
        schedule = Schedule.objects.all().order_by('cvid')
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)
    
    def post(self, request,*args, **kwargs):
        cvid = request.data.get("cvid")
        customerid = request.data.get("cvcustomerid")

        productlist = request.data.get("productidlist")
        
        if cvid:
            schedule = Schedule.objects.get(pk=cvid)
            serializer = ScheduleSerializer(schedule, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            customerdata = make_internal_request(f'customer-services:8003/customers/internal/by-id/{customerid}/')
            if customerdata:
                if productlist and len(productlist) > 0 and customerid:
                    products = make_internal_request(f'product-services:8002/products/internal/validate-ids/', productlist)
                    if products:
                        serializer = ScheduleSerializer(data=request.data)
                        if serializer.is_valid():
                            serializer.save()
                            schedule = serializer.data
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
                        for id in productlist:
                            associate = AssociationSerializer(data={
                                "cvproductid":id,
                                "cvscheduleid":schedule.get("cvid")
                            })
                            if associate.is_valid():
                                associate.save()

                        make_internal_request(f'product-services:8002/products/internal/update-storage/', productlist)
                        send_create_notification(schedule, customerdata, schedule.get("cvid"))
                        return Response(schedule, status=status.HTTP_200_OK)
                    else:
                        return Response("Invalid Products", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Customer Not Exists", status=status.HTTP_400_BAD_REQUEST)
            

@method_decorator(validate_jwt, name='dispatch')
class ReturnView(APIView):
    def post(self, request, pk, *args, **kwargs):
        try:
            schedule = Schedule.objects.get(pk=pk)

            if not schedule.cdreturneddate:
                schedule.cdreturneddate = date.today()
                schedule.save()
    
                association = Association.objects.filter(cvscheduleid=pk)
                productsidlist = AssociationDisplaySerializer(association, many=True)

                make_internal_request(f'product-services:8002/products/internal/withdraw-storage/', [ass.get("cvproductid") for ass in productsidlist.data])
                customerdata = make_internal_request(f'customer-services:8003/customers/internal/by-id/{schedule.cvcustomerid}/')
                products = make_internal_request(f'product-services:8002/products/internal/id-list/', [ass.get("cvproductid") for ass in productsidlist.data])
                
                prodstrlist = [ass.get("ccdescription") for ass in products]
                result_string = ", ".join(prodstrlist)
                send_returned_notification(schedule, customerdata, pk, result_string)
                return Response("OK", status=status.HTTP_200_OK)
            return Response("Schedule already returned", status=status.HTTP_200_OK)
        except Schedule.DoesNotExist:
            return Response("Schedule Not exists",status=status.HTTP_404_NOT_FOUND)

@method_decorator(validate_jwt, name='dispatch')
class FindScheduleView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            schedule = Schedule.objects.get(pk=pk)
            serializer = ScheduleSerializer(schedule, many=False)

            scheduledata = serializer.data
            customerid = scheduledata.get("cvcustomerid")

            customerdata = make_internal_request(f'customer-services:8003/customers/internal/by-id/{customerid}/')
            if customerdata:
                association = Association.objects.filter(cvscheduleid=pk)
                productsidlist = AssociationDisplaySerializer(association, many=True)
                products = make_internal_request(f'product-services:8002/products/internal/id-list/', [ass.get("cvproductid") for ass in productsidlist.data])
                
                scheduledata["customer"] = customerdata
                scheduledata["products"] = products
                return Response(scheduledata, status=status.HTTP_200_OK)
            else:
                return Response("Error retrieving customer",status=status.HTTP_404_NOT_FOUND)
        except Schedule.DoesNotExist:
            return Response("Schedule Not exists",status=status.HTTP_404_NOT_FOUND)


    

