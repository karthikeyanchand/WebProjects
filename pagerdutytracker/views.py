from django.shortcuts import render

# Create your views here.

from django_tables2 import SingleTableView
#from django_tables2.paginators import LazyPaginator

from pagerdutytracker.models import Incident
from pagerdutytracker.tables import PagerSemanticTable


class IncidentListView(SingleTableView):
    model = Incident
    table_class = PagerSemanticTable
    table_pagination = {"per_page": 20}
    template_name = 'pagerdutytracker/view.html'
