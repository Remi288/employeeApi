from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt


from .serializers import UserSerializer, LoginSerializer


class RegisterView(GenericAPIView):
    '''This register new users for
        authentication

    '''
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            status_code = status.HTTP_201_CREATED
            response = {
                'message': 'successfully!',
                'payload': serializer.data
            }
            return Response(response, status=status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):

    '''This login register user and generate
        "token" for authentication


    '''
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {
                'payload': serializer.data,
                "token": auth_token
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response({"message": 'invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)