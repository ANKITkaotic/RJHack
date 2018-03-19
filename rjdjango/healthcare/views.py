from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from healthcare.models import Data


class Profile(LoginRequiredMixin, ListView):
    template_name = 'health/profile.html'

    def get_queryset(self):
        return Data.objects.filter(owner=self.request.user)
