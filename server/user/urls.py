from django.urls import path
from .views import *

urlpatterns = [
    path('choose-type', ChooseType.as_view()),
    path('get-typ', GetType.as_view()),
    path('add-about', AddAbout.as_view()),
    path('get-about', GetAbout.as_view()),
    path('update-about', UpdateAbout.as_view()),
    path('add-link', AddLink.as_view()),
    path('get-links', GetLinks.as_view()),
    path('update-link', UpdateLink.as_view()),
    path('add-notice', AddNotice.as_view()),
    path('get-all-notices', GetAllNotices.as_view()),
    path('remove-notice', RemoveNotice.as_view()),
    path('rate-photographer', RatePhotographer.as_view()),
    path('get-photographer-rating', GetPhotographerRating.as_view())
]
