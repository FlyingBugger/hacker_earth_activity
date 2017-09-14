"""activity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin


from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^get_wexin_params',views.get_wexin_params),
    url(r'^get_form', views.get_form),
    url(r'MP_verify_XWsldS5dzRvbRcvT.txt',views.getMP_varify),

    url(r'^poster', views.poster_page),
    url(r'^signup', views.signup_page),
    url(r'^problems', views.problems_page),
	url(r'^verify/(?P<code>\w+)', views.get_certificate),
    url(r'^post_message\/?$',views.post_message),

    url(r'^software/', include('software_park.urls')),
]
