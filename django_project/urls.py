"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from django_project.views import GoogleCalendarInitView, GoogleCalendarRedirectView
from django.views.generic.base import RedirectView

urlpatterns = [
    # Endpoint for initiating the Google Calendar authentication
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view(), name='google-calendar-init'),

    # Endpoint for handling the redirect from Google Calendar authentication
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view(), name='google-calendar-redirect'),

    # Redirect for favicon.ico
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]

