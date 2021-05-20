from django.shortcuts import render,redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request, post, get, put
from django.http import JsonResponse
import ipinfo
import socket
import re 
from .utils import User

class RegisterUser(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        if self.check_email(email) != '400':
            return JsonResponse({'msg': 'That email does already exist'}, status=status.HTTP_400_BAD_REQUEST)
        password = request.data.get('password')
        validate = self.validate_password(password)
        if validate != '200':
            return JsonResponse({'msg': validate }, status=status.HTTP_400_BAD_REQUEST)
        
        kwargs = {
            'fullname': request.data.get('fullname'),
            'email': request.data.get('email'),
            'password': password,
            'profile_image': request.data.get('profile_image'),
            'location': self.getUserLocation(),
        }

        p = User()
        registerUser = p.createUser(**kwargs)
        if registerUser != '200':
            return JsonResponse({'msg': 'Account Not Created'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'msg': 'Account Created'}, status=status.HTTP_200_OK)

    def checkEmail(self, email):
        c = User()
        return c.checkEmailExistence(email)
        

    def validatePassword(self, password):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

        compiling = re.compile(reg)

        searching = re.search(compiling, password)

        if searching:
            return '200'
        return searching

    def getUserLocation(self):
        h_name = socket.gethostname()
        ip_address = socket.gethostbyname(h_name)
        access_token = '79669c5cb85e52'
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip_address)
        location = {'city': details.city, 'region': details.region, 'country': details.country}
        return location

class LoginUser(APIView):
    def put(self,request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        id = self.checkEmailAndPassword(email,password)
        if id == '404':
            return JsonResponse({'msg': 'Email or Password is Incorrect'}, status=status.HTTP_404_NOT_FOUND)
        
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        p = User()
        updateToken = p.loginUser(id, self.request.session.session_key)

        if updateToken != '200':
            return JsonResponse({'msg': 'Could not login'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'msg': 'logged in'}, status=status.HTTP_200_OK)


    def checkEmailAndPassword(self, email, password):
        c = User()
        user = c.checkEmailAndPasswordExistence(email,password)
        if user != '404':
            return user
        return '404'

class LogoutUser(APIView):
    def put(self, request, format=None):
        id = request.data.get('id')

        l = User()
        user = l.logoutUser(id)

        if user != '200':
            return JsonResponse({'msg': 'Could Not Logout'}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'msg': 'Logged Out'}, status=status.HTTP_200_OK)


