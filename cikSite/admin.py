from django.contrib import admin
from cikSite.models import Voting


class VotingAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'number_kand', 'number_izb', 'time', 'email')
