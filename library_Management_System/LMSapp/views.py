from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework.response import Response
from LMSapp.serializers import BookSerializers
from rest_framework import status

# Create your views here.

#Layout Page
def indexView(request):
    return render(request, 'layout.html')

def homeView(request):
    return render(request, 'home.html')

@login_required
def BookView(request):
    form=BookForm()
    template_name="LMSapp/Book_form.html"
    context={'form':form}
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showbook_url')
    return render(request,template_name,context)

@login_required
def ShowBookView(request):
    template_name = 'LMSapp/show_book.html'
    obj = Book.objects.all()
    context = {'obj': obj}
    return render(request, template_name, context)

#Show Book records for Students
def StudentView(request):
    template_name = 'LMSapp/showbookrecords.html'
    obj = Book.objects.all()
    context = {'obj': obj}
    return render(request, template_name, context)
   
@login_required
def updateBookView(request,id):
    obj=Book.objects.get(srno=id)
    form=BookForm(instance=obj)
    template_name='LMSapp/Book_form.html'

    if request.method=='POST':
        form=BookForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showbook_url')
    context={"form":form}
    return render(request,template_name,context)

@login_required
def deleteBookView(request,id):
    obj=Book.objects.get(srno=id)
    template_name='LMSapp/conformation.html'
    context={'obj':obj}

    if request.method=='POST':
        obj.delete()
        return redirect('showbook_url')
    return render(request,template_name,context)

#Sign Up View
def registerView(request):
    form=UserCreationForm()
    template_name='authapp/register.html'
    context={'form':form}
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    return render(request,template_name,context)

#LoginView
def loginView(request):
    template_name='authapp/login.html'
    context={}
    if request.method=="POST":
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        user=authenticate(username=un,password=pw)
        if user is not None:
            login(request,user)
            return redirect('home_url')
    return render(request,template_name,context)

#Logout View
def logoutView(request):
    logout(request)
    return redirect('index_url')

# Create Your API Here
class BookDetails(APIView):
    def get(self,request):
        stu=Book.objects.all()
        serializer=BookSerializers(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookInfo(APIView):
    def get(self,request,id):
        try:
            stu=Book.objects.get(rno=id)
        except Book.DoesNotExist:
            msg={'msg':'Student Does Not Exist'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer=BookSerializers(stu)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            stu=Book.objects.get(srno=id)
        except Book.DoesNotExist:
            msg={'msg':'Student Does Not Exist'}
        serializer=BookSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def patch(self,request,id):
        try:
            stu=Book.objects.get(srno=id)
        except Book.DoesNotExist:
            msg={'msg':'Student Does Not Exist'}
        serializer=BookSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            stu=Book.objects.get(srno=id)
        except Book.DoesNotExist:
            msg={'msg':'Student Does Not Exist'}
        stu.delete()
        return Response({'msg':'Record Deleted!!'},status=status.HTTP_204_NO_CONTENT)
    