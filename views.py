#from rest_framework.permissions import AllowAny
#from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from API.serializers import NewUserSerializer
from rest_framework import generics, permissions
from API.models import Employee
from rest_framework.decorators import action
from django.shortcuts import render

def homePage(request):
  return render(request,'home.html')

def loginPage(request):
  return render(request,'login.html')

def signUpPage(request):
  return render(request,'signup.html')


class NewUserViewSets(viewsets.ModelViewSet):
  queryset= Employee.objects.all()
  serilizer_class= NewUserSerializer

  #@action(detail=False, methods=['post'], name='register')
  def create(self, request):
    """
    Api to registration
    """
    try:
        EmpId = request.data.get("EmpId","")
        first_name = request.data.get("first_name","")
        last_name = request.data.get("last_name","")
        email_id = request.data.get("email_id","")
        password = request.data.get("password","")
        phoneNumber = request.data.get("phoneNumber","")
        DepartmentId = request.data.get("DepartmentId","")
        EmployeeType = request.data.get("EmployeeType","")
        ReportTo = request.data.get("ReportTo","")
        user_obj = Employee.objects.filter(email_id=email_id)
        print("...",user_obj)
        if user_obj:
            return Response("User Already Exist With This Email Id")
        else:
          user = Employee.objects.create(EmpId=EmpId,first_name=first_name,last_name=last_name,email_id=email_id,password=password,phoneNumber=phoneNumber,DepartmentId=DepartmentId,EmployeeType=EmployeeType,ReportTo=ReportTo)
          print("user",user)
          return Response("registration successfully")
    except Exception as e:
      print("hello")
      return Response( "invalid data")


'''
        name = request.data.get("name","")
        email= request.data.get("email","")'''



"""class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
"""
