"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic.base import TemplateView


from config import settings
from core.views import AboutUs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('comment/', include('comment.urls')),
    path('favorite/', include('favorite.urls')),
    path('order/', include('order.urls')),
    path('product/', include('product.urls')),
    path('', TemplateView.as_view(template_name='_base.html')),
    path('about-us',AboutUs.as_view(),name="about_us"),

]
if settings.DEBUG:
    urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
                    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT_custom))
