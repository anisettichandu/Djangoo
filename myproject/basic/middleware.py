from django.http import JsonResponse
import json
import re
class UsernameMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=="/signup/"):
            data=json.loads(request.body)
            username=data.get("username")
            if not username:
                return JsonResponse({"error":"username is required"},status=400)
            if len(username)<3 or len(username)>20:
                return JsonResponse({"error":"username should contain 3 to 20 charecters"},status=400)
            if username[0] in "._" or username[-1] in "._":
                return JsonResponse({"error":"username should not starts or ends with ._"},status=400)
            if not re.match(r"^[a-zA-Z0-9._]+$",username):
                return JsonResponse({"error":"username should contain letters,numbers,dot,underscore"},status=400)
            if ".." in username or "__" in username:
                return JsonResponse({"error":"username should not contain .. or __"})
        return self.get_response(request)
    
class EmailMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=="/signup/"):
            data=json.loads(request.body)
            email=data.get("email")
            if not email:
                return JsonResponse({"error":"Email should not be empty"},status=400) 
            if "," in email or " " in email:
                return JsonResponse({"error":"email should not contain any spaces or ,"},status=400) 
            if email[0]in ".0123456789@" or email[-1]==".":
                return JsonResponse({"error":"email should not starts with . or numbers or @"},status=400)
            if "@" not in email:
                return JsonResponse({"error":"email should contain @"})
            if not re.match(r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
                return JsonResponse({"error": "Invalid email format"}, status=400)
        return self.get_response(request)
    
class PasswordMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if (request.path=="/signup/"):
            data=json.loads(request.body)
            username=data.get("username")
            email=data.get("email")
            password=data.get("password")
            if not password:
                return JsonResponse({"error":"password should not be empty"})
            if len(password)<6:
                return JsonResponse({"error":"password must be morethan 6 charecters"})
            if (not any (c.islower()for c in password)) or (not any(c.isdigit() for c in password)):
                return JsonResponse({"error":"password must contain atleast one lower and one digit"})
            if not re.match(r"^[A-Z.@_a-z0-9]+$",password):
                return JsonResponse({"error":"Password should contain lowercase uppercase and charecters"})
            if password== username or password == email:
                return JsonResponse({"error":"password should not match with username or email"})
        return self.get_response(request)
            
                
            
                  
        
           