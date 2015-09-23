from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django import forms

class ParametersForm(forms.Form):
    inflation = forms.FloatField(label='inflation')
    appr_rate = forms.FloatField(label='appr_rate')
    years = forms.IntegerField(label='years')
    initial_capital = forms.FloatField(label='initial_capital')
    yearly_saving = forms.FloatField(label='Yearly Saving')

def thanks(request):
    return HttpResponse('thanks')

def index(request):
    form = ParametersForm()
    final_amt = 0
    if request.method == 'POST':
        form = ParametersForm(request.POST)
        if form.is_valid():
            form.inflation = form.cleaned_data['inflation']
            form.appr_rate = form.cleaned_data['appr_rate']
            form.years = form.cleaned_data['years']
            form.initial_capital = form.cleaned_data['initial_capital']
            form.yearly_saving = form.cleaned_data['yearly_saving']
            r = form.inflation + form.appr_rate
            final_amt = form.yearly_saving*((1-r**form.years)/(1-r))
            return render(request, 'index.html', {'form': form, 'final_amt':final_amt})
        else:
            print('test')
            form = ParametersForm()
    return render(request, 'index.html', {'form': form, 'final_amt':final_amt})

