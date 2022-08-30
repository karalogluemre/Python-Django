from django.urls import path
from Customer.API import views as api_views

urlpatterns = [
    # path('Customer',api_views.customer_list_create_api_view, name='Customer Listesi'),
    # path('Customer/<int:pk>', api_views.customer_detail_api_view, name='Customer-detay'),
    path('yazarlar/',api_views.GazeteciListCreateAPIView.as_view(), name='yazar-listesi'),
    path('makaleler/',api_views.MakaleListCreateAPIView.as_view(), name='makale-listesi'),
    path('makaleler/<int:pk>', api_views.MakaleDetailAPIView.as_view(), name='makale-detay'),
]
