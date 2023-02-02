from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import get_user

# Create your views here.
def home(request):
    questions = question.objects.all()
    dictionary = {
        'questions':questions
    }
    return render(request,'home.html',dictionary)

def question_view(request,id):
    questions = question.objects.get(id = id)
    answer = answers.objects.filter(ans__id = id)
    
    answer_box = answer_form()
    if (request.method == 'POST'):
        answer_box= answer_form(request.POST)
        if (answer_box.is_valid()):
            answered = answer_box.save(commit=False)
            answered.ans = questions
            answered.users = request.user
            answered.save()
        else:
            print("invalid")
    dictionary ={
        'question':questions,
        'answers':answer,
        'answer_box':answer_box
    }
    return render(request,'question.html',dictionary)

@login_required
def discussion(request):
    question_box = question_form()
    if (request.method == 'POST'):
        question_box= question_form(request.POST,request.FILES)
        if (question_box.is_valid()):
            discuss =question_box.save(commit=False)
            discuss.users = request.user
            discuss.save()
            redirect('home')
        else:
            print("invalid")
    dictionary ={
        'question':question_box,
    }
    return render(request,'discussion.html',dictionary)
    
