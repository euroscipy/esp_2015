from django.contrib import admin

from .models import TalkProposal, PosterProposal, TutorialProposal


admin.site.register(TalkProposal)
admin.site.register(PosterProposal)
admin.site.register(TutorialProposal)
