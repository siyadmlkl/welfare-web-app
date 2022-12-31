from django.http import Http404
from django.shortcuts import render
from .models import transaction
from django.contrib.auth.decorators import login_required,permission_required
import datetime

@login_required(login_url='/')
def home(request):
    transactions = transaction.objects.all().values().order_by('-transDate')
    balance = calculateBalance(transactions)
    return render(request, 'accounts.html', {'transactions': transactions, 'balance': balance})

@permission_required('accounting.add_transaction',raise_exception='Permission Denied...!')
def addtransaction(request):
    return render(request, 'addtransaction.html')


def savetransaction(request):
    message=''
    if request.method == 'POST':
        particulars = request.POST['particulars']
        type = request.POST['type']
        amount = request.POST['amount']
        addBy=request.user
        transDate = datetime.datetime.now()

        transaction(particulars=particulars,
                type=type,
                amount=amount,
                addBy=addBy,
                transDate=transDate).save()
        transactions=transaction.objects.all().values().order_by('-transDate')
        balance = calculateBalance(transactions)
        return render(request,'accounts.html',{'transactions': transactions, 'balance': balance})

def filter_transaction(request):
    print(request)
    try:
        if request.method == 'POST':
            type=request.POST['type']
            transactions=transaction.objects.filter(type=type).values().order_by('-transDate')
            alltransactions=transaction.objects.all().values().order_by('-transDate')
            balance = calculateBalance(alltransactions)
            return render(request,'accounts.html',{'transactions':transactions,'balance':balance})
    except:
        raise Http404("No valid filter...")
    return render(request,'accounts.html')

def calculateBalance(transactions):
    blnce=0
    credit=0
    expense=0
    for item in transactions:
        if item['type'] == 'Credit':
            credit += item['amount']
        else:
            expense += item['amount']
        print(item['transDate'])
    blnce = credit-expense
    return blnce
