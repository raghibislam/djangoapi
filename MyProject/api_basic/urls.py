
from django.urls import path
from .views import article_list , article_detail,ArticleAPIView,GenericAPIView
urlpatterns = [
    # path('article/',article_list),
    path('article/',ArticleAPIView.as_view()),
    path('detail/<int:pk>/',article_detail),
    path('generic/article/<int:id>/',GenericAPIView.as_view()),

]