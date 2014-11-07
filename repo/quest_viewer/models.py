from django.db import models

# TODO refactor and put it in a lib
def non_empty_str(s):
	return s != None and s != ''

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
	comments = models.ManyToManyField(Comment,blank=True)

# The subject of a discipline, like Trigonometry
class Subject(models.Model):
	def __unicode__(self):
		return self.name

	def full_description(self):
		ret = []
		ret.append(self.name)
		ret.append("Discipline: " + ','.join(self.main_disciplines_list()))
		if (self.super_subject != None):
			ret.append("Super-subject<" + str(self.super_subject) + ">")
		return ';'.join(ret)

	def main_disciplines_list(self):
		return [discipline_subj.discipline for discipline_subj in self.disciplinessubject_set.all() if discipline_subj.main_discipline]

	def main_disciplines_list_comma_separated(self, comma=', '):
		return comma.join([str(discipline) for discipline in self.main_disciplines_list()])
	main_disciplines_list_comma_separated.short_description = 'Main disciplines'

	name = models.CharField(max_length=100)
	disciplines = models.ManyToManyField(Discipline, through='DisciplinesSubject')
	super_subject = models.ForeignKey('self', null=True, default=None, blank=True)
	comments = models.ManyToManyField(Comment, blank=True)

class DisciplinesSubject(models.Model):
	def __unicode__(self):
		return str(self.discipline) + ('(!)' if self.main_discipline else '') + ' - ' + str(self.subject)
	class Meta:
		unique_together = ('discipline', 'subject')
	discipline = models.ForeignKey(Discipline)
	subject = models.ForeignKey(Subject)
	main_discipline = models.BooleanField(default=False)

class Institute(models.Model):
	def __unicode__(self):
		return self.name + ((';' + self.acronym) if non_empty_str(self.acronym) else '')
	name = models.CharField(max_length=1000)
	acronym = models.CharField(max_length=100,null=True, blank=True)
	comments = models.ManyToManyField(Comment, blank=True)

class Source(models.Model):
	def __unicode__(self):
		return (self.institute.acronym if non_empty_str(self.institute.acronym) else self.institute.name) + (';' + str(self.year) if self.year != None else '')
	institute = models.ForeignKey(Institute)
	year = models.IntegerField(null=True, blank=True)
	comments = models.ManyToManyField(Comment, blank=True)
	class Meta:
		unique_together = ('institute','year')

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
	comments = models.ManyToManyField(Comment, blank=True)

class QuestionSubject(models.Model):
	question = models.ForeignKey(Question)
	subject = models.ForeignKey(Subject)
	main_subject = models.BooleanField(default=False)
	comments = models.ManyToManyField(Comment, blank=True)


class ObjectiveOptionItem(models.Model):
	identifier = models.CharField(max_length=3)
	item_text = models.ForeignKey(TextAlias)
	question = models.ForeignKey(Question)
	comments = models.ManyToManyField(Comment, blank=True)

# The same question may have some answers
class Answer(models.Model):
	answer_text = models.ForeignKey(TextAlias)
	question = models.ForeignKey(Question)
	comments = models.ManyToManyField(Comment, blank=True)
	
