from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),  
    path('products/', views.products, name='products'),
    path('products/<int:id>/', views.Pagebikes, name="PageBikes"),
    path('batteries/', views.batteries_page, name='batteries_page'),
    path('batteries/<int:id>/', views.batterie_elements, name="batterie_elements"),
    path('trotinette/', views.trotinette_page, name="trotinette_page"),
    path('trotinette/<int:id>', views.trotinette_elements, name='trotinette_elements'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
