from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import re
import random

# Create your views here.

def signout(request, id):
    logout(request)
    
    UserModel = get_user_model()
    try: 
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
        
    except UserModel.DoesNotExist:
        return JsonResponse({'error' : 'Invald user ID'})
    
    return JsonResponse({'success' : 'Logout succes'})

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))

@csrf_exempt
def sigin(request):
    if not request.method == 'POST':
        return JsonResponse({'error' : 'Send a post request with valid parameter only '})
    
    # username = request.POST['email']
    
    if "email" in request.POST:
       username = request.POST['email']
    
    else:
       username = "Mr.test"
       
    username = request.POST.get("email")

    password = request.POST['password'] 

    # validattion_part
    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return JsonResponse({'error' : 'Enter a valid email'})
    if len(password) < 3:
        return JsonResponse({'error' : 'Password needs to be at least fo 3 char'})
    
    UserModel = get_user_model()
    print(UserModel)
    
    try:
        user = UserModel.objects.get(email = username)
        print(user)
        if user.check_password(password):
            user_dict = UserModel.objects.filter(email=username).values().first()
            user_dict.pop('password')
        
            if user.session_token != "0":
               user.session_token = "0"  
               user.save()
               return JsonResponse({'erron': "Previous session exists!"})
        
            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user) 
            return JsonResponse({'token' : token,'user': user_dict})
        else:
            return JsonResponse({'error' : 'Invalid password'})
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create' : [AllowAny]}    
    
    queryset = CustomUser.objects.all().order_by('id')
    
    serializer_class = UserSerializer
    
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        
        except KeyError:
            return [permission() for permission in self.permission_classes]