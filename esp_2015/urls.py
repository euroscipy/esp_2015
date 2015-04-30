from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

import symposion.views
from simple_shop.views import shop

WIKI_SLUG = r"(([\w-]{2,})(/[\w-]{2,})*)"


urlpatterns = patterns(
    "",
    url(r"^$", "symposion.cms.views.page", {'path' : 'home/'}, name="home"),
    url(r"^_edit/$", "symposion.cms.views.page_edit", {'path' : 'home/'}, name="cms_page_edit"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/signup/$", symposion.views.SignupView.as_view(), name="account_signup"),
    url(r"^account/login/$", symposion.views.LoginView.as_view(), name="account_login"),
    url(r"^account/", include("account.urls")),

    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),
    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^boxes/", include("symposion.boxes.urls")),
    url(r"^teams/", include("symposion.teams.urls")),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),
    url(r"^markitup/", include("markitup.urls")),
    url(r"^ticketing/", include("simple_shop.urls")),

    url(r"^", include("symposion.cms.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
