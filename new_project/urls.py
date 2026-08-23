from django.urls import path
from .views import news, home_page_view, page_error_404, contact, about

urlpatterns = [
    path('new_project/', news, name='new_project'),
    path('', home_page_view, name='home_page'),
    path('error_404',page_error_404, name='page_not_found' ),
    path('contact/', contact, name='contact'),
    path("about/", about, name="about"),

]