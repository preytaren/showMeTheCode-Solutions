from datetime import datetime
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from models import MemoModel
from forms import MemoForm


class MemoView(View):

    def get(self, request):
        form = MemoForm()
        if MemoModel.objects.count() >= 10:
            recent_message = MemoModel.objects.order_by('time')[-10:]
        else:
            recent_message = MemoModel.objects.all()
        return render(request, 'memo.html', {'form':form, 'historys':recent_message})

    @csrf_exempt
    def post(self, request):
        form = MemoForm(request.POST)
        if form.is_valid():
            MemoModel.objects.create(username=form.clean_data['username'],
                                     message=form.clean_data['message'],
                                     time=datetime.now())
            return HttpResponseRedirect('/memo/')

@csrf_exempt
def memo_handler(request):
    if MemoModel.objects.count() >= 10:
        recent_message = MemoModel.objects.order_by('time')[-10:]
    else:
        recent_message = MemoModel.objects.all()
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            MemoModel.objects.create(username=form.cleaned_data['username'],
                                     message=form.cleaned_data['message'],
                                     time=datetime.now())
    return render(request, 'memo.html', {'historys':recent_message})
