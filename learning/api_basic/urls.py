from django.urls import path,include
from .views import article_list,article_details,ArticleAPIViews

urlpatterns = [
    # path('article_list/', article_list),
    path('article_details/<int:pk>/', article_details),
    path('ArticleAPIViews/', ArticleAPIViews.as_view()),
]