from django.urls import path, include
from .views import (
    register_view,
    login_view,
    logout_view,
    account_view,
    account_search_view,
    edit_account_view
)

app_name = 'account'

urlpatterns = [
    path('register', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('search/', account_search_view, name="search"),
    path('<user_id>/', account_view, name='profile'),
    path('<user_id>/edit/', edit_account_view, name='edit')
]
