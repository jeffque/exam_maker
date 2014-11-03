from django.shortcuts import render

from quest_viewer.models import *

def index(request):
	discipline_list = Discipline.objects.all()
	context = {'discipline_list': discipline_list}
	return render(request, 'quest_viewer/index.html', context)

def discipline(request,discipline_id):
	discipline = Discipline.objects.get(id=discipline_id)
	subject_list = discipline.subject_set.all()
	context = {'subject_list': subject_list,
			'discipline_id': discipline_id,
			'discipline': discipline}
	return render(request, 'quest_viewer/discipline.html', context)

def subject(request,subject_id):
	subject = Subject.objects.get(id=subject_id)
	discipline_list = subject.disciplinessubject_set.all()
	context = {'discipline_list': discipline_list,
			'subject_id': subject_id,
			'subject': subject}
	return render(request, 'quest_viewer/subject.html', context)
