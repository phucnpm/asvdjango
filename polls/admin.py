from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# Class to define extension for admin UI of Polls CRUD
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Class to define admin UI of Polls CRUD
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # display Choice when CRUD a Poll using ChoiceInLine admin class
    inlines = [ChoiceInline]
    # display Polls as a list with 3 fields
    list_display = ('question', 'pub_date', 'was_published_recently')
    # display Poll filter control based on pub_date
    list_filter = ['pub_date']
    # display search field base on question
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)