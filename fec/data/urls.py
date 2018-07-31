from django.conf.urls import url

from data import views
from data import views_datatables
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^data/$', views.landing),
    url(r'^data/search/$', views.search),
    url(r'^data/advanced/$', views.advanced),
    url(r'^data/candidate/(?P<candidate_id>\w+)/$', views.candidate),
    url(r'^data/committee/(?P<committee_id>\w+)/$', views.committee, name='committee-by-id'),
    url(r'^data/elections/(?P<office>\w+)/(?P<state>\w+)/(?P<district>\w+)/(?P<cycle>[0-9]+)/$', views.elections),
    url(r'^data/elections/(?P<office>\w+)/(?P<state>\w+)/(?P<cycle>[0-9]+)/$', views.elections),
    url(r'^data/elections/(?P<office>\w+)/(?P<cycle>[0-9]+)/$', views.elections, name='elections'),
    #url(r'^data/elections/(?P<office>\w+)/(?P<cycle>[0-9]+)/$', views.elections),
    #url(r'^data/elections/(?P<office>\w+)/(?P<cycle>[0-9]+)/(?P<tab>\w+)/$', views.elections_tab, name='elections'),
    url(r'^data/elections/$', views.elections_lookup),
    #url('articles/<slug:title>/', views.article, name='article-detail'),

    #url(r'^data/elections/(?P<office>\w+)/(?P<cycle>[0-9]+)/#individual-contributions/$', views.elections, name='new_view'),
    #url(r'^data/elections/(?P<office>\w+)/(?P<cycle>[0-9]+)/(?P<tab>contributions)/$', RedirectView.as_view(url='/')),


    #url(r'^elections/$', views.QuerystringRedirect.as_view(), name="elections_redirect"),
    #url(r'^data/elections/(?P<office>\w+)/(?P<cycle>[0-9]+)/?tab=contributions/$', views.QuerystringRedirect.as_view(), name='elections'),

    #url(r'^data/elections/(?P<office>\w+)/(?P<cycle>[0-9]+)/?P<contributions>/$', RedirectView.as_view(url='/')),
    #url(r'^data/elections/(?P<office>\w+)/(?P<cycle>[0-9]+)/(?P<contributions>)/$', views.elections),


    # Feedback Tool
    url(r'^data/issue/$', views.feedback),

    # Datatables
    url(r'^data/candidates/(?P<office>\w+)/$',
        views_datatables.candidates_office),
    url(r'^data/candidates/$', views_datatables.candidates),
    url(r'^data/committees/$', views_datatables.committees),
    url(r'^data/communication-costs/$',
        views_datatables.communication_costs),
    url(r'^data/disbursements/$', views_datatables.disbursements),
    url(r'^data/electioneering-communications/$',
        views_datatables.electioneering_communications),
    url(r'^data/filings/$', views_datatables.filings),
    url(r'^data/independent-expenditures/$',
        views_datatables.independent_expenditures),
    url(r'^data/individual-contributions/$',
        views_datatables.individual_contributions),
    url(r'^data/loans/$', views_datatables.loans),
    url(r'^data/party-coordinated-expenditures/$',
        views_datatables.party_coordinated_expenditures),
    url(r'^data/receipts/individual-contributions/$',
        views_datatables.individual_contributions),
    url(r'^data/receipts/$', views_datatables.receipts),
    url(r'^data/reports/(?P<form_type>[\w-]+)/$', views_datatables.reports),
    url(r'^legal-resources/enforcement/audit-search/$', views_datatables.audit),
]
