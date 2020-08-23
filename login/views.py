from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from base.models import Cliente, Consumidor


class IndexView(generic.View):
    def get(self, request):
        return render(request, 'login/index.html', {})
