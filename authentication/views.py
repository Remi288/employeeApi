from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import UserSerializer


class RegisterView(GenericAPIView):
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
