from django.urls import path
from shopping_list_app.views import ShoppingListsView, shopping_list_view

urlpatterns = [
    path('', ShoppingListsView.as_view(), name='shoppinglists'),
    path('shopping_list/<int:id>/', shopping_list_view, name='shoppinglist')
]