from django.urls import path
from .views import homeView,indexView,BookView,ShowBookView,updateBookView,deleteBookView,StudentView,registerView,loginView,logoutView,BookDetails,BookInfo

#Create urls for all views here
urlpatterns=[
    path('index/',indexView,name='index_url'),
    path('home/',homeView,name='home_url'),
    path('addbook/',BookView,name='addbook_url'),
    path('showbook/',ShowBookView,name='showbook_url'),
    path('ub/<int:id>/',updateBookView,name='updatebook_url'),
    path('db/<int:id>/',deleteBookView,name='deletebook_url'),
    path('ssv/',StudentView,name='show_book_records_url'),
    path('reg/',registerView,name='register_url'),
    path('login/',loginView,name='login_url'),
    path('logout/',logoutView,name='logout_url'),
    path('bookdetails/',BookDetails.as_view()),
    path('bookinfo/<int:id>/',BookInfo.as_view())
   

]