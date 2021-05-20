from django.shortcuts import render,redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request, post, get, put
from django.http import JsonResponse
import ipinfo
import socket
import re 
from .utils import Account

class ChooseType(APIView):
    def post(self, request, format=None):
        user_type = request.data.get('user_type')
        user_id = request.data.get('user_id')

        kwargs = {
            'user_type': user_type,
            'user_id': user_id
        }
        a = Account()
        type = a.addTypeOfAccount(**kwargs)

        if type != '200':
            return JsonResponse({'msg': 'Something went wroung. Try again in 5 minutes'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'msg': 'Success'}, status=status.HTTP_200_OK)

class GetType(APIView):
    def get(self, request, format=None):
        user_id = request.data.get('user_id')

        a = Account()
        type = a.getAccountType(user_id)

        if type == '404':
            return JsonResponse({'msg': 'Account type not found'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'msg': type}, status=status.HTTP_200_OK)

class AddAbout(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        about = request.data.get('about')

        kwargs = {
            'user_id': user_id,
            'about': about
        }

        a = Account()
        about = a.addAboutToAccount(**kwargs)

        if about != '200':
            return JsonResponse({'msg': 'Something went wrong. Try again in 5 minutes'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'msg': 'About section added'}, status=status.HTTP_200_OK)
    

class GetAbout(APIView):
    def get(self, request, format=None):
        user_id = request.data.get('user_id')

        a = Account()
        about = a.getAccountAbout(user_id)

        if about == '404':
            return JsonResponse({'msg': 'About section not found'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'msg': about}, status=status.HTTP_200_OK)
            

class UpdateAbout(APIView):
    def put(self, request, format=None):
        user_id = request.data.get('user_id')
        about = request.data.get('about')

        kwargs = {
            'user_id': user_id,
            'about': about
        }

        a = Account()
        update = a.updateAbout(**kwargs)

        if update != '200':
            return JsonResponse({'msg': 'Something went wrong. Try again in 5 minutes'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'msg': 'Updated about section'}, status=status.HTTP_200_OK)

class AddLinks(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        link_name = request.data.get('link_name')
        link_url = request.data.get('link_url')

        kwargs = {
            'user_id': user_id,
            'link_name': link_name,
            'link_url': link_url
        }

        a = Account()
        link = a.AddLinksToAccount(**kwargs)

        if link != '200':
            return JsonResponse({'msg': 'Something went wrong. Try again in 5 minutes'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'msg': 'Link added'}, status=status.HTTP_200_OK)

class GetLinks(APIView):
    def get(self, request, format=None):
        user_id = request.data.get('user_id')

        a = Account()
        links = a.getAccountLinks(user_id)

        if links == '404':
            return JsonResponse({'msg': 'Links not found'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'msg': links}, status=status.HTTP_200_OK)

class UpdateLinks(APIView):
    def put(self, request,format=None):
        link_id = request.data.get('id')
        link_name = request.data.get('link_name')
        link_url = request.data.get('link_url')

        kwargs = {
            'id': link_id,
            'link_name': link_name,
            'link_url': link_url
        }

        a = Account()
        link = a.updateLinks(**kwargs)

        if link != '200':
            return JsonResponse({'msg': 'Something went wrong. Try again in 5 minutes'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'msg': 'Link updated'}, status=status.HTTP_200_OK)

class AddNotice(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        message = request.data.get('message')

        kwargs = {
            'user_id': user_id,
            'message': message
        }

        a = Account()
        notice = a.addNoticeToAccount(**kwargs)

        if notice != '200':
            return JsonResponse({'msg': 'Something went wrong. Try again in 5 minutes'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'msg': 'Notice Added'}, status=status.HTTP_200_OK)

class GetAllNotices(APIView):
    def get(self, request, format=None):
        user_id = request.data.get('id')

        a = Account()
        notice = a.getAccountNotices(user_id)

        if notice == '404':
            return JsonResponse({'msg': 'Notices not found'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'msg': notice}, status=status.HTTP_200_OK)

class RemoveNotice(APIView):
    def delete(self, request, format=None):
        id = request.data.get('id')

        a = Account()
        notice = a.removeNotice(id)

        if notice != '200':
            return JsonResponse({'msg': 'Something went wrong. Try again in 5 minutes'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'msg': 'Notice removed'}, status=status.HTTP_200_OK)

class RatePhotographer(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        photographer_id = request.data.get('photographer_id')
        rating = request.data.get('rating')

        kwargs = {
            'user_id': user_id,
            'photographer_id': photographer_id,
            'rating': rating
        }

        a = Account()
        rate = a.rateAccount(**kwargs)

        if rate != '200':
            return JsonResponse({'msg': 'Something went wrong. Try again in 5 minutes'})
        return JsonResponse({'msg': 'Rate added'}, status=status.HTTP_200_OK)

class GetPhotographerRating(APIView):
    def get(self, request, format=None):
        photographer_id = request.data.get('photographer')

        a = Account()
        rating = a.getAccountRating(photographer_id)

        if rating == '404':
            return JsonResponse({'msg': 'Photographer not rated'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'msg': rating}, status=status.HTTP_200_OK)