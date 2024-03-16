from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
   

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Perhaps you want to redirect to a success page here
            # return redirect('success_url')

    else:
        form = UserCreationForm()
           
         
        
 

    return render(request,'useraccounts/register.html', {'form':form})