from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer,ClubRegisterSerializer
from rest_framework.authtoken.models import Token
from clubs.models import Club_member,ClubInvite


class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )
        
        serializer.save()

       
        return Response(
            {
                "message": "Registered Successfully"
            },
            status=status.HTTP_201_CREATED
        )
        

class LoginView(APIView):
    
    def post(self,request):
        
        phone = request.data.get("phone")
        password = request.data.get("password")
        
        user = authenticate(
            username =phone,
            password =password
        )
        
        if not user:
            return Response({
                "error":"Invalid credentials"
            })
            
            
        token ,created = Token.objects.get_or_create(
            user = user
        )
        
        return Response({
            "token":token.key,
            "user_id":user.id,
            "name":user.name,
            "role":user.role,
            "phone":phone
        })
   
   
class ClubRegisterView(APIView):

    # permission_classes = []

    def post(self, request):

        serializer = ClubRegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {
                "message": "Club registered successfully.",
                "data":serializer.data
            },
            status=201
        )

        
     
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProfileSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)   

        
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out"})