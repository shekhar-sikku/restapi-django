from django.urls import path
from .views import GenericApiView, ArticleApiView, ArticleDetails

urlpatterns = [
    # Function based views urls 
    # path('article/', article_list),
    # path('article/<int:sno>/', article_detail),

    # Class based views urls
    path('article/', ArticleApiView.as_view()),
    path('article/<int:sno>/', ArticleDetails.as_view()),

    # GenericApi based views urls
    # path('article/', GenericApiView.as_view()),
    # path('article/<int:sno>/', GenericApiView.as_view()),
]
