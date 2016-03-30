from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
import pandas as pd
from resultanalysis.models import year,period,yeardata,student,grade,subject

# Create your views here.
def group_prom(request,group):#group
  syear="2013-2014"
  speriod="2. Ebaluazioa"
  ryear=year.objects.get(year=syear)
  rperiod=period.objects.get(name_eu=speriod)
  rstudents=yeardata.objects.filter(group=group,year=ryear)
  sst=[a.student for a in rstudents]
  gqs=grade.objects.filter(year=ryear,period=rperiod,student__in=sst)
  df=pd.DataFrame(list(gqs.all().values('student','subject__name_es','grade','period__name_eu')))
  pt=pd.pivot_table(df, values="grade",index="subject__name_es")
  labels=list(pt.index.values)
  data=list(pt.values)
  print(labels,data)
  #data=pt.to_json()
  return render(request, 'resultanalysis/group.html', {'data': data, 'labels': labels, 'group': group})
  #return HttpResponse(data, content_type='application/json')
  #grade.objects.filter(year__year=syear,period__name_eu=speriod,student__in=sst)
  
  

class ArticleDetailView(DetailView):

    model = grade

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        rstudents=yeardata.objects.filter(group=self.group,year=self.ryear)
        context['stats'] = grade.objects.filter(year__year=self.year,period__name_eu=self.period,student__in=rstudents)
        return context  