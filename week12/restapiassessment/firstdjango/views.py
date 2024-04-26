from django.shortcuts import render
from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from datetime import datetime
from firstdjango.models import Emailsender,StockData
from pytube import *
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.views import APIView
from .serializers import viewDataSerializer
from rest_framework import generics
import requests
class SaveData(APIView):
    def post(self,request):
        symbol = request.data.get('symbol')
        
        if not symbol:
            return Response({'error': 'Symbol parameter is required'}, status=400)
        url = f"https://yahoo-finance127.p.rapidapi.com/price/{symbol}"

        headers = {
        "X-RapidAPI-Key": "11a9317e4bmsh45d55b906008e11p158722jsnd5086ba06d52",
        "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
        }
        res=requests.get(url,headers=headers)
        if res.status_code ==200:
            data=res.json()
            inst=StockData(stock_sym=data['symbol'],stockprice=float(data['regularMarketOpen']['fmt']))
            inst.save()
            return Response({'message': 'Data saved successfully'} ,status=res.status_code)
        else:
            return Response({'error': 'Failed to fetch data from the external API'}, status=res.status_code)

class viewStock(generics.ListAPIView):
    queryset=StockData.objects.all()
    serializer_class= viewDataSerializer

    




        


