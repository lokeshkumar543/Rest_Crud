from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class ProductAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        try:
            if id is not None:
                pro_obj=Product.objects.get(id=id)
                serializer=ProductSerializer(pro_obj)
                return Response(serializer.data) 
        except:
            return Response({'msg':'This ID Does Not Matched Our Database'})      
        return Response({"msg":"Please Enter Id After Show Data"}) 
           
        # all objects listing
        # pro_obj=Product.objects.all()
        # serializer=ProductSerializer(pro_obj,many=True)
        # return Response(serializer.data)    

    def post(self,request,format=None):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)       
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def put(self,request,pk,format=None):
        id=pk
        pro_obj=Product.objects.get(id=id)
        serializer=ProductSerializer(pro_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Completed Data Updated'})       
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        id=pk
        pro_obj=Product.objects.get(id=id)
        serializer=ProductSerializer(pro_obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})       
        return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        id=pk
        pro_obj=Product.objects.get(id=id)
        pro_obj.delete()
        return Response({'msg':'Data Deleted'})    

