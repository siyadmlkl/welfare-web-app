from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('addtransaction',views.addtransaction),
    path('savetransaction',views.savetransaction),
    path('filter_transaction',views.filter_transaction),
]
