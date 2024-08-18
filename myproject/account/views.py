from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Account

class AccountTopView(TemplateView):
    template_name = 'account/account-top.html'

class AccountListView(ListView):
    # 表示するページのhtmlを指定
    template_name = "account/account-list.html"
    # modelの指定
    model = Account
    # account リストを object_list に格納
    context_object_name = "accounts"

class AccountDetailView(DetailView):
    template_name = "account/account-detail.html"
    model = Account
