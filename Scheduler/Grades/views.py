from collections import defaultdict
from datetime import datetime
from django.shortcuts import render ,redirect
from .models import Link



from .forms import LinkModelForm ,GradesChoicesForm
from mainsite.models import User
from django.http import JsonResponse
import json

class Choice():
    def __init__(self, username):
        self.name = username
        self.choice = {}
user_choice = []

def form_choices(request):
    context = {}
    current_user = request.user
    
    options = current_user.get_grades_test_option()
    context['form'] = GradesChoicesForm([(v, v) for v in options])
    print(context['form'])
    
    # choice_form = GradesChoicesForm(())
    
    return render(request,'Grades/grades_form.html',context)

def GradesAJAX(request):

    if request.is_ajax() and request.method == 'POST':
        test_type = request.POST.get('test_type')

        current_user = request.user
        options = current_user.get_grades_test_option()
        options.append(test_type)
        current_user.set_grades_test_option(options)
        current_user.save()
        
        return JsonResponse({})
    return render(request,'Grades/grades_form.html')

def learning(request):
    roll = Link.objects.all()
    chart_subject = defaultdict(list)
    chart_scope = defaultdict(list)
    Labels = []
    str_Labels = []
    for l in roll:
        chart_subject[l.subject].append(l.grade)
        chart_scope[l.subject].append(l.scope)
        Labels.append(l.scope)
        
    user = User.objects.filter(account=request.user)
    str_Labels = str(Labels)
    current_user = request.user
    choices = current_user.get_grades_test_option()
    return render(request, 'Grades/grades.html',{
        'roll': roll,
        'chart_subject': dict(chart_subject),
        'user':user,
        'choices':choices,
        'cjart_scope':dict(chart_scope),
        'str_Labels': str_Labels,
    })

def subject_ajax(request):
    if request.is_ajax() and request.method == 'POST':
	    # test_object = User.get_grades_test_option().values.distinct()
         return render(request,'Grades/grades.html')

    return render(request,'Grades/grades.html')


    
def subject_to_test(request):
    return render(request,'Grades/grades.html')
