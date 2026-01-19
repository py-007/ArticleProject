from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home_view,name='home'),
    path('form/', views.form_view,name='form'),
    path('allarticles/', views.all_articles,name='all_articles'),
    path('spec/<int:id>', views.specific_view,name='specific'),
    path('delete/<int:id>', views.delete_article,name='delete'),
    path('update/<int:id>', views.update_view,name='update'),
]
