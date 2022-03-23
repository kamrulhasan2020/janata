from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('trade/', views.Trades.as_view(), name='trades'),
    path('trade/<str:code>/', views.Trades.as_view(), name='trades'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('latest-entry/', views.LatestEntry.as_view(), name='latest_entry'),
    path('load-data/', views.load_data_from_csv, name='load_data'),
    path('chart/', views.chart, name='chart'),
]
