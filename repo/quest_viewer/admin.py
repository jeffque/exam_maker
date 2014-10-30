from django.contrib import admin

from quest_viewer.models import *

class DisciplinesSubjectRelationshipInline(admin.TabularInline):
	model = DisciplinesSubject
	extra = 1

class DisciplineAdmin(admin.ModelAdmin):
	inlines = (DisciplinesSubjectRelationshipInline, )

class SubjectAdmin(admin.ModelAdmin):
	inlines = (DisciplinesSubjectRelationshipInline, )
	list_display = ('name', 'main_disciplines_list_comma_separated')

admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Institute)
admin.site.register(Source)
admin.site.register(Comment)
