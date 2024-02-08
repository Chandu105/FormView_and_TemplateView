from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class TemplateHtml(TemplateView):
    template_name='TemplateHtml.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='chandana'
        ECDO['surname']='bandaru'
        return ECDO




class InsertschoolbyTV(TemplateView):
    template_name='InsertschoolbyTV.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ECDO=super().get_context_data(**kwargs)
        ECDO['SFO']=SchoolForm
        return ECDO
    

    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid:
            SFDO.save()
            return HttpResponse('InsertschoolbyTV is done')
        
class InsertschoolbyFV(FormView):
    template_name='InsertschoolbyFV.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('InsertschoolbyFV is done')

    

