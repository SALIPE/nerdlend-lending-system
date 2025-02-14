from collections import Counter

from django.utils.decorators import method_decorator
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .decorations import validate_internal_jwt, validate_jwt
from .models import Tbfavorite, Tbproduct
from .serializers import (ProductListSerializer, TbfavoriteSerializer,
                          TbproductSerializer)


@method_decorator(validate_jwt, name='dispatch')
class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        products = Tbproduct.objects.all()
        serializer = TbproductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = TbproductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@method_decorator(validate_jwt, name='dispatch')
class ProductDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            product = Tbproduct.objects.get(pk=pk)
            serializer = TbproductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tbproduct.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk, *args, **kwargs):
        try:
            product = Tbproduct.objects.get(pk=pk)
            serializer = TbproductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tbproduct.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk, *args, **kwargs):
        try:
            product = Tbproduct.objects.get(pk=pk)
            serializer = TbproductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tbproduct.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk, *args, **kwargs):
        try:
            product = Tbproduct.objects.get(pk=pk)
            product.delete()
            return Response({"message": "Product deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Tbproduct.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(validate_jwt, name='dispatch')
class FavoriteView(APIView):
    def get(self, request, *args, **kwargs):
        favorites = Tbfavorite.objects.all()
        serializer = TbfavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = TbfavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(validate_jwt, name='dispatch')     
class TbfavoriteDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            favorite = Tbfavorite.objects.get(pk=pk)
            serializer = TbfavoriteSerializer(favorite)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tbfavorite.DoesNotExist:
            return Response({"error": "Favorite not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk, *args, **kwargs):
        try:
            favorite = Tbfavorite.objects.get(pk=pk)
            serializer = TbfavoriteSerializer(favorite, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tbfavorite.DoesNotExist:
            return Response({"error": "Favorite not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk, *args, **kwargs):
        try:
            favorite = Tbfavorite.objects.get(pk=pk)
            serializer = TbfavoriteSerializer(favorite, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tbfavorite.DoesNotExist:
            return Response({"error": "Favorite not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        try:
            favorite = Tbfavorite.objects.get(pk=pk)
            favorite.delete()
            return Response({"message": "Favorite deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Tbfavorite.DoesNotExist:
            return Response({"error": "Favorite not found"}, status=status.HTTP_404_NOT_FOUND)
        



@method_decorator(validate_internal_jwt, name='dispatch')   
class InternalValidateIdsView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            idlist = request.data
            products = Tbproduct.objects.filter(cvid__in=idlist)
            serializer = TbproductSerializer(products, many=True).data

            id_counts = Counter(idlist)

            for product in products:
                required_quantity = id_counts[product.cvid]  # Quantidade requisitada
                if product.cvamount < required_quantity:
                    return Response({
                    "detail": "Estoque insuficiente para os seguintes produtos.",
                }, status=status.HTTP_400_BAD_REQUEST)
            

            if set(idlist) == set([prodc.get("cvid") for prodc in serializer]):
                return Response(serializer)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        except Tbproduct.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@method_decorator(validate_internal_jwt, name='dispatch')   
class InternalListView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            idlist = request.data  
            
            products = Tbproduct.objects.filter(cvid__in=idlist)
            
            if not products.exists():
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            product_map = {product.cvid: product for product in products}
            
            result = []
            for cvid in idlist:
                if cvid in product_map:
                    result.append(product_map[cvid]) 
            
            serializer = ProductListSerializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        
@method_decorator(validate_internal_jwt, name='dispatch')   
class InternalUpdateStorageView(APIView):
     def post(self, request, *args, **kwargs):
        try:
            idlist = request.data 
            id_counts = Counter(idlist)
            
            products = Tbproduct.objects.filter(cvid__in=id_counts.keys())
            
            if not products.exists():
                return Response({"detail": "Produtos não encontrados."}, status=status.HTTP_404_NOT_FOUND)
            
            for product in products:
                decrement = id_counts[product.cvid] 
                product.cvamount -= decrement  
                product.save()  
            
            return Response("OK", status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
@method_decorator(validate_internal_jwt, name='dispatch')   
class InternalWitdrawStorageView(APIView):
     def post(self, request, *args, **kwargs):
        try:
            idlist = request.data 
            id_counts = Counter(idlist)
            
            products = Tbproduct.objects.filter(cvid__in=id_counts.keys())
            print(id_counts.keys())
            if not products.exists():
                return Response({"detail": "Produtos não encontrados."}, status=status.HTTP_404_NOT_FOUND)
            
            for product in products:
                decrement = id_counts[product.cvid] 
                product.cvamount += decrement  
                product.save()  
            
            return Response("OK", status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AllProductNoAuthView(APIView):
    def get(self, request, *args, **kwargs):
        products = Tbproduct.objects.all()
        serializer = TbproductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

