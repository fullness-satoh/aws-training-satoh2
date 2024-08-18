from django.urls import path
from .views import AccountTopView
from .views import AccountListView
from .views import AccountDetailView

app_name = 'account'

urlpatterns = [
    path('account-top', AccountTopView.as_view(), name='account-top'),
    path('account-list', AccountListView.as_view(), name='account-list'),
    path('account-detail/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
]


