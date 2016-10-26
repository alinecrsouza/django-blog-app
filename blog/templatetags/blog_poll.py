from django import template
from random import randint

from polls.models import Question, Choice
from django.db.models import Sum

register = template.Library()

# render a random poll in poll.html
@register.inclusion_tag('blog/poll.html')
def get_poll(self=None):
    if Question.objects.count() > 0:
        return {
            'question': Question.objects.all()[randint(0, Question.objects.count() - 1)],
        }
    else:
        return {
            'question': None
        }

# calculate the percentage of votes of each question's choice
@register.simple_tag
def get_percentage(question_id, choice_id):
    # aggregate query that returns the sum of the votes, after that get the result
    total_votes = Choice.objects.filter(question = question_id).aggregate(Sum('votes')).get('votes__sum', 0.00)
    choice = Choice.objects.get(pk=choice_id)
    percentage = (choice.votes/total_votes)*100
    return percentage
