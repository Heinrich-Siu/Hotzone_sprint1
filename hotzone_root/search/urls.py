from django.urls import path
from . import views

urlpatterns = [
    path('searchbox',
         views.ViewSearchBox.as_view(),
         name='search box'),
    path('result',
         views.ConfirmResultPage.as_view(),
         name="result"),
    path('cancel',
         views.CancelInput.as_view(),
         name='cancel')
]
