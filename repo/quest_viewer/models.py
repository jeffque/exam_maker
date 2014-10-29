from django.db import models

# Generic comment, for whatever reason
class Comment(models.Model):
	def __unicode__(self):
		return self.text
	text = models.TextField()

# The discipline, like Math
class Discipline(models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=100)
	comments = models.ManyToManyField(Comment)

# The subject of a discipline, like Trigonometry
class Subject(models.Model):
	def __unicode__(self):
		ret = []
		ret.append(self.name)
		ret.append("Discipline: " + ','.join([str(discipline_subj.discipline) for discipline_subj in self.disciplinessubject_set.all() if discipline_subj.main_discipline]))
		if (self.super_subject != None):
			ret.append("Super-subject<" + str(self.super_subject) + ">")
		return ';'.join(ret)
	name = models.CharField(max_length=100)
	disciplines = models.ManyToManyField(Discipline, through='DisciplinesSubject')
	super_subject = models.ForeignKey('self', null=True, default=None)
	comments = models.ManyToManyField(Comment)

class DisciplinesSubject(models.Model):
	discipline = models.ForeignKey(Discipline)
	subject = models.ForeignKey(Subject)
	main_discipline = models.BooleanField(default=False)

class Institute(models.Model):
	def __unicode__(self):
		return self.name + ((';' + self.acronym) if (self.acronym != None) else '')
	name = models.CharField(max_length=1000)
	acronym = models.CharField(max_length=100,null=True)
	comments = models.ManyToManyField(Comment)

class Source(models.Model):
	institute = models.ForeignKey(Institute)
	year = models.IntegerField(null=True)
	comments = models.ManyToManyField(Comment)

class ImagesUrl(models.Model):
	url = models.CharField(max_length=1000)

class TextHTML(models.Model):
	text = models.TextField()
	images_url = models.ManyToManyField(ImagesUrl)

class TextTeX(models.Model):
	text = models.TextField()
	images_url = models.ManyToManyField(ImagesUrl)

class TextAlias(models.Model):
	textHTML = models.ForeignKey(TextHTML,null=True)
	textTeX = models.ForeignKey(TextTeX,null=True)

# A question in an exam
class Question(models.Model):
	question_text = models.ForeignKey(TextAlias)
	subjects = models.ManyToManyField(Subject,through='QuestionSubject')
	source = models.ForeignKey(Source)
	comments = models.ManyToManyField(Comment)

class QuestionSubject(models.Model):
	question = models.ForeignKey(Question)
	subject = models.ForeignKey(Subject)
	main_subject = models.BooleanField(default=False)
	comments = models.ManyToManyField(Comment)


class ObjectiveOptionItem(models.Model):
	identifier = models.CharField(max_length=3)
	item_text = models.ForeignKey(TextAlias)
	question = models.ForeignKey(Question)
	comments = models.ManyToManyField(Comment)

# The same question may have some answers
class Answer(models.Model):
	answer_text = models.ForeignKey(TextAlias)
	question = models.ForeignKey(Question)
	comments = models.ManyToManyField(Comment)
	
