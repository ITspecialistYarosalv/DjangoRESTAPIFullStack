from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Advocate,Companies
from .serializer import AdvocateSerializer,CompanySerializer
from django.db.models import Q
# Create your views here.

@api_view(['GET'])
def endpoint(request):
    data = ['/advocates','advocates/:username']
    return Response(data)


@api_view(['GET','POST'])
def advocates_list(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        advocates = Advocate.objects.filter(Q(username__icontains=query)| Q(bio__icontains = query))
        serializer =AdvocateSerializer(advocates,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        advocate=Advocate.objects.create(
            username=request.data['username'],
            bio = request.data['bio']
        )
        serializer = AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)



class AdvocatesDetails(APIView):

    def get_object(self,username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExists:
            raise Response("Ther is no user")

    def get(self,requset,username):
        advocates = self.get_object(username=username)
        serializer = AdvocateSerializer(advocates, many=False)
        return Response(serializer.data)

    def put(self,request,username):
        advocates = self.get_object(username=username)
        advocates.bio = request.data['bio']
        advocates.save()
        serializer = AdvocateSerializer(advocates, many=False)
        return Response(serializer.data)

    def delete(self,request,username):
        advocates = self.get_object(username=username)
        advocates.delete()
        return Response('user was deleted')


@api_view(['GET'])
def companies(request):
    companies = Companies.objects.all()
    serializer = CompanySerializer(companies,many=True)
    return Response(serializer.data)