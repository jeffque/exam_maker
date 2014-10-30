from django.contrib import admin

from quest_viewer.models import *

class DisciplinesSubject__relationshipInline(admin.TabularInline):
	model = DisciplinesSubject
	extra = 1

class DisciplineAdmin(admin.ModelAdmin):
	inlines = (DisciplinesSubject__relationshipInline, )

class SubjectAdmin(admin.ModelAdmin):
	inlines = (DisciplinesSubject__relationshipInline, )
	list_display = ('name', 'main_disciplines_list_comma_separated')

admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Institute)
admin.site.register(Source)
