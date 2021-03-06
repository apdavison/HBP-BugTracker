"""issuetracker URL Configuration

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
from django.conf.urls import url
from django.conf.urls import include

from issuetracker.views import config

from issuetracker.views import CreateTicketView
from issuetracker.views import create_project, edit_project
from issuetracker.views import TicketListView
from issuetracker.views import TicketListView2
from issuetracker.views import Test_Menu_deroulant
from issuetracker.views import TicketDetailView
from issuetracker.views import ProjectListView
from issuetracker.views import AdminTicketListView
from issuetracker.views import AdminTicketListView2
from issuetracker.views import AdminTicketDetailView

from django.contrib import admin

from issuetracker.utils.database_functions import remove_ticket, close_ticket

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('hbp_app_python_auth.urls', namespace='hbp-social')),

    url(r'^create_ticket/(?P<ctx>.+)$', CreateTicketView.as_view(), name='ticket-create'), 
    url(r'^Menu_deroulant$', Test_Menu_deroulant, name='Menu_deroulant'), 
    url(r'^project_list/(?P<ctx>.+)$',ProjectListView.as_view(), name='project-list'),
    url(r'^create_project/(?P<ctx>.+)$', create_project, name='project-create'),
    url(r'^edit_project/$', edit_project, name='project-edit'),
    url(r'^$',TicketListView.as_view(), name='ticket-list'),
    url(r'^list(?P<ctx>.+)$',TicketListView2.as_view(), name='ticket-list2'),
    url(r'^ticket/(?P<pk>\d+)/(?P<ctx>.+)$', TicketDetailView.as_view(), name='ticket-detail'),
    url(r'^config.json$', config, name='config'),
    #admin
    url(r'^edit/$', AdminTicketListView.as_view(), name='ticket-admin'),
    url(r'^edit/(?P<ctx>.+)$', AdminTicketListView2.as_view(), name='ticket-admin2'),
    url(r'^admin_ticket/(?P<pk>\d+)/(?P<ctx>.+)$', AdminTicketDetailView.as_view(), name='ticket-detail-admin'),

]