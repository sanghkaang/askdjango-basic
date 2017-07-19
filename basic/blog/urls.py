# blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    # ^ 문자열의 시작
    # $ 문자열의 끝
    # ^$ 아무것도없으니 즉 최상위를 의미

    # 함수를 호출하는게 아니라 함수자체를 넘겨주는것
    url(r'^$', views.post_list),
]