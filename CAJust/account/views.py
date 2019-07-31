from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_200_OK,HTTP_201_CREATED,HTTP_404_NOT_FOUND


from account.serializers import ClientSerializer,AccountSerializer
from account.models import Account,Client

# Create your views here.

class AccountView(APIView):
    def get(self,request):
        account=Account.objects.all()
        serializer= AccountSerializer(account,many=True)
        return Response(serializer.data)

class ClientView(APIView):
    def get(self,request):
        clients=Client.objects.all()
        serializer= ClientSerializer(clients,many=True)
        return Response(serializer.data,status=HTTP_200_OK)

    def post(self,request):
        clientserializer=ClientSerializer(data=request.data)
        if clientserializer.is_valid():
            clientserializer.save()
            return Response(clientserializer.data,status=HTTP_201_CREATED)
        else:
            return Response(clientserializer.errors,status=HTTP_400_BAD_REQUEST)

class ClientDetail(APIView):
    def get_object(self,pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return HTTP_404_NOT_FOUND

    def get(self,request,pk):
        client=self.get_object(pk)
        serializer=ClientSerializer(client)
        return Response(serializer.data)

    def put(self,request,pk):
        client=self.get_object(pk)
        serializer = ClientSerializer(client,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)



