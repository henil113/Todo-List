from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import dutyFilter

# Create your views here.
def index(request):
    duties = duty.objects.all()
    form = dutyForm()
    myFilter = dutyFilter(request.GET, queryset=duties)
    duties = myFilter.qs
    if request.method=='POST':
        form = dutyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'duties': duties,'form':form,'myFilter':myFilter}
    return render(request,'duties/List.html',context)

def updateDuty(request,pk):
    duties = duty.objects.get(id=pk)
    form = dutyForm(instance=duties)

    if request.method=="POST":
        form = dutyForm(request.POST, instance=duties)
        if form.is_valid():
            form.save()
            return redirect("/")

    context= {'form':form}
    return render(request,'duties/update.html',context)

def deleteDuty(request,pk):
    item = duty.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("/")
    context={'item':item}
    return render(request,'duties/delete.html',context)
