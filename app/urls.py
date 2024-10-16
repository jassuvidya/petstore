from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.user_login),
    path('login/', views.user_login),
    path('logout', views.user_logout),
    path('product', views.product),
    path('register/', views.register),
    path('productdetail/<pid>', views.productdetail),
    path('catfilter/<cv>', views.catfilter),
    path('pricefilter', views.sortbyprice),
    path('sort/<sv>', views.sortbyprice),
    path('addtocart/<pid>', views.addtocart),
    path('viewcart', views.viewcart),
    path('placeorder', views.placeorder),
    path('fetchorder', views.fetchorder),
    path('updateqty/<x>/<cid>', views.updateqty),
    path('remove', views.remove),
    path('landing', views.landing),
    path('orderhistory', views.orderhistory),
    path('search', views.search),
    path('makepayment', views.makepayment),
    path('paymentsuccess', views.paymentsuccess),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
