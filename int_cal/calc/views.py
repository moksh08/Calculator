from django.shortcuts import render,redirect
from .forms import calculationform
from .models import Calculation

def index(request):
    if request.method == 'POST':
        form = calculationform(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.result = instance.principle * (instance.rate / 100) * instance.time 
            instance.save()

        return redirect('index')
    
    else:
        form = calculationform()

    calculations = Calculation.objects.all().order_by('timestamp')
    return render(request, 'index.html', {'form':form, 'calculations':calculations})
