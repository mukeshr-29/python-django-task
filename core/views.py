from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
import requests
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return HttpResponse("Welcome to the Webhook App!")

@api_view(['GET'])
def incoming_data(request):
    return JsonResponse({'message': 'Data received successfully'})

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@api_view(['GET'])
def get_destinations(request, account_id):
    try:
        account = Account.objects.get(account_id=account_id)
        destinations = Destination.objects.filter(account=account)
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def handle_incoming_data(request):
    token = request.headers.get('CL-X-TOKEN')
    if not token:
        return Response({"error": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        account = Account.objects.get(app_secret_token=token)
    except Account.DoesNotExist:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

    data = request.data
    if not isinstance(data, dict):
        return Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)

    destinations = account.destinations.all()
    for destination in destinations:
        headers = destination.headers
        url = destination.url
        method = destination.http_method.lower()

        if method == 'get':
            requests.get(url, headers=headers, params=data)
        elif method in ['post', 'put']:
            getattr(requests, method)(url, headers=headers, json=data)

    return Response({"status": "Data forwarded successfully"})
