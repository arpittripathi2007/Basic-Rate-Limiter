from django.http import JsonResponse
from django.core.cache import cache
from handlers.models import User, RateLimitUser
from rest_framework import serializers
from django.db import models

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = [authentication.BasicAuthentication]

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.BasicAuthentication]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class Journey(APIView):
    authentication_classes = [authentication.BasicAuthentication]

    def get(self, request):
        try:
            user = request.user
            username = user.username
            rate_limit_object = cache.get(username, {})
            rate_limit = rate_limit_object['journey'] if 'journey' in rate_limit_object.keys() else 0

            if not 'journey' in rate_limit_object.keys():
                modify_entity('journey', user, -1)
                rate_limit = cache.get(username)['journey']
            if rate_limit == 0:
                return JsonResponse({
                    'status': 501,
                    'username': username,
                    'message': 'You have exceeded the api hit limit',
                    'time': f'You can try after sometime'})

            else:
                modify_entity('journey', user, rate_limit-1)
            return JsonResponse({
                'status': 200,
                'username': username,
                'limit_left': rate_limit-1,
                'message': 'You have successfully hit the api'})

        except Exception as e:
            return JsonResponse({'message': f'Some Error occured {e}'})

class ResetJourney(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    
    def get(self, request):
        user = request.user
        modify_entity('journey', user, -1)
        return JsonResponse({'status': 'Success'})


class Boundary(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    
    def get(self, request):
        try:
            user = request.user
            username = user.username
            rate_limit_object = cache.get(username, {})
            rate_limit = rate_limit_object['boundary'] if 'boundary' in rate_limit_object.keys() else 0
            rate_limit_object = {}
            if not 'boundary' in rate_limit_object.keys():
                modify_entity('boundary', user, -1)
                rate_limit = cache.get(username)['boundary']

            if rate_limit == 0:
                return JsonResponse({
                    'status': 501,
                    'username': username,
                    'message': 'You have exceeded the api hit limit',
                    'time': f'You can try after sometime'})
            else:
                modify_entity('boundary', user, rate_limit-1)
            return JsonResponse({
                'status': 200,
                'username': username,
                'limit_left': rate_limit-1,
                'message': 'You have successfully hit the api'})

        except Exception as e:
            return JsonResponse({'message': f'Some Error occured {e}'})


class ResetBoundary(APIView):
    authentication_classes = [authentication.BasicAuthentication]

    def get(self, request):
        try:
            user = request.user
            modify_entity('boundary', user, -1)
            return JsonResponse({'status': 'Success'})

        except Exception as e:
            return JsonResponse({'message': 'Some Error occured'})


def modify_entity(type, user, reset_value):
    username = user.username

    if reset_value == -1:
        rate_limit_user = RateLimitUser.objects.get(username=user, name=type)
        dict_initial = cache.get(username) if cache.get(username) else {}
        dict_initial[type] = rate_limit_user.rate_limit
    else:
        dict_initial = cache.get(username) if cache.get(username) else {}
        dict_initial[type] = dict_initial[type]-1

    cache.set(username, dict_initial)


def clear_cache(request):

    try:
        cache.clear()
        return JsonResponse({'status': 'Success'})

    except Exception as e:
        return JsonResponse({'message': 'Error Occured'})
