from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# modules for generating the pdf
# Libraries
from fpdf import FPDF
from datetime import date

# Today's date
today = date.today()
today = today.strftime("%B %d, %Y")

# Create your views here.


# def home(request):
#     return HttpResponse("this is front page\n")


def complain_view(request):
    complains = complain.objects.all().order_by('-date')
    dictionary = {
        'complains': complains
    }
    return render(request, 'complain_view.html', dictionary)


def complain_view_each(request, id):
    complains = complain.objects.get(id=id)
    total_likes = complains.total_likes()
    total_dislikes = complains.total_dislikes()

    dictionary = {
        'complains': complains,
        'likes': total_likes,
        'dislikes': total_dislikes
    }
    return render(request, 'complain_each.html', dictionary)


def idea_view_each(request, id):
    ideas = idea.objects.get(id=id)
    total_likes = ideas.total_likes()
    total_dislikes = ideas.total_dislikes()
    dictionary = {
        'ideas': ideas,
        'likes': total_likes,
        'dislikes': total_dislikes
    }
    return render(request, 'idea_each.html', dictionary)


def idea_view(request):
    ideas = idea.objects.all().order_by('-date')
    dictionary = {
        'ideas': ideas
    }
    return render(request, 'idea_view.html', dictionary)


@login_required
def complain_add(request):
    complain_box = complain_form()
    if request.method == 'POST':
        complain_box = complain_form(request.POST,request.FILES)
        if (complain_box.is_valid()):
            complain = complain_box.save(commit=False)
            complain.users= request.user
            complain.save()
            return redirect('home')
        else:
            print("not valid")
        #     messages.success(request,"complain successfully registered")
        # else:
        #     messages.error(request,'complain not registered')
    dictionary = {
        'complain': complain_box
    }
    # return HttpResponse("this is complain page\n",dictionary)
    return render(request, 'complain_add.html', dictionary)




@login_required
def idea_add(request):
    idea_box = idea_form()
    if (request.method == 'POST'):
        idea_box = idea_form(request.POST, request.FILES)
        if (idea_box.is_valid()):
            idea = idea_box.save(commit=False)
            idea.users = request.user
            idea.save()
            return redirect('home')
        # else:
        #     messages.error(request,'idea not registered')
    dictionary = {
        'idea': idea_box
    }
    return render(request, 'idea_add.html', dictionary)


# def suggestion(request):
#     return HttpResponse("this is suggestion page\n")


def complain_like_view(request, id):
    posts = get_object_or_404(complain, id=request.POST.get('post_id'))
    posts.upvote.add(request.user)
    return HttpResponseRedirect(reverse('complain_view_each', args=[str(id)]))


def complain_dislike_view(request, id):
    post = get_object_or_404(complain, id=request.POST.get('post_id'))
    post.downvote.add(request.user)
    return HttpResponseRedirect(reverse('complain_view_each', args=[str(id)]))


def idea_like_view(request, id):
    posts = get_object_or_404(idea, id=request.POST.get('post_id'))
    posts.upvote.add(request.user)
    return HttpResponseRedirect(reverse('idea_view_each', args=[str(id)]))


def idea_dislike_view(request, id):
    post = get_object_or_404(idea, id=request.POST.get('post_id'))
    post.downvote.add(request.user)
    return HttpResponseRedirect(reverse('idea_view_each', args=[str(id)]))

# -----------------------------------------------------------------------------------------------------------------------------------


def pdfs():
    pdf = FPDF(format='A4')

    ##########################################################################
    # Add cover page
    pdf.add_page()
    with open("/home/kingdom/Desktop/hackathon/temp/pragyanbhattarai04-Yatra_Hackathon_Team_Red/home/coverpage.txt", "r") as coverpage_txtfile:
        pdf.set_font("Times", 'B', size=30)
        for eachline in coverpage_txtfile:
            pdf.cell(180, 20, txt=eachline, align='C', ln=1, border=0)

    # coverpage_txtfile.close()

    pdf.set_font("Times", 'B', size=20)
    pdf.cell(180, 10, txt=today, align='C', ln=1, border=0)

    ##########################################################################
    # Abstract page
    txtfile = open(
        "/home/kingdom/Desktop/hackathon/temp/pragyanbhattarai04-Yatra_Hackathon_Team_Red/home/abstract.txt", "r")
    lines = txtfile.readlines()
    pdf.add_page()
    pdf.cell(180, 10, txt="ABSTRACT", ln=1, align='C', border=0)
    pdf.set_font("Times", size=13)
    for x in lines:
        pdf.multi_cell(180, 10, txt=x, align='L', border=0)

    ##########################################################################
    # Table of contents page
    pdf.add_page()
    pdf.set_font("Times", 'B', size=20)
    pdf.cell(180, 10, txt="TABLE OF CONTENTS", ln=1, align='C', border=0)
    with open("/home/kingdom/Desktop/hackathon/temp/pragyanbhattarai04-Yatra_Hackathon_Team_Red/home/table_of_contents.txt", "r") as txtFile:
        lines = txtFile.readlines()
        i = 1
        pdf.set_font("Times", size=16)
        for x in lines:
            pdf.multi_cell(180, 10, txt=str(i)+". " + x, align='L', border=0)
            i = i+1

    ##########################################################################
    # Introduction section
    pdf.add_page()
    pdf.set_font("Times", 'B', size=20)
    pdf.cell(180, 10, txt="INTRODUCTION", ln=1, align='L', border=0)
    with open("/home/kingdom/Desktop/hackathon/temp/pragyanbhattarai04-Yatra_Hackathon_Team_Red/home/introduction.txt", "r") as txtFile:
        lines = txtFile.readlines()
        pdf.set_font("Times", size=13)
        for x in lines:
            pdf.multi_cell(180, 10, txt=x, align='L', border=0)

        ##########################################################################
    # Complain section
    pdf.add_page()
    pdf.set_font("Times", 'B', size=20)
    pdf.multi_cell(180, 10, txt="Complains", align='L', border=0)
    # with open(file,"r") as txtFile:
    with open("/home/kingdom/Desktop/hackathon/temp/pragyanbhattarai04-Yatra_Hackathon_Team_Red/home/complains.txt", "r") as txtFile:
        lines = txtFile.readlines()
        pdf.set_font("Times", size=13)
        for x in lines:
            pdf.multi_cell(180, 10, txt=x, align='L', border=0)

    # ideas section
    pdf.add_page()
    pdf.set_font("Times", 'B', size=20)
    pdf.multi_cell(180, 10, txt="Major ideas", align='L', border=0)
    with open("/home/kingdom/Desktop/hackathon/temp/pragyanbhattarai04-Yatra_Hackathon_Team_Red/home/probable_solutions.txt", "r") as txtFile:
        lines = txtFile.readlines()
        i = 1
        pdf.set_font("Times", size=13)
        for x in lines:
            pdf.multi_cell(180, 10, txt=str(i)+". " + x, align='L', border=0)
            i = i+1

    # Conclusion section
    pdf.add_page()
    pdf.set_font("Times", 'B', size=20)
    pdf.multi_cell(180, 10, txt="Conclusion", align='L', border=0)
    with open("/home/kingdom/Desktop/hackathon/temp/pragyanbhattarai04-Yatra_Hackathon_Team_Red/home/conclusion.txt", "r") as txtFile:
        lines = txtFile.readlines()
        pdf.set_font("Times", size=13)
        for x in lines:
            pdf.multi_cell(180, 10, txt=x, align='L', border=0)

    pdf.output("mygfg.pdf")


def generate_txt(request):
    question = complain.objects.all().order_by('-date')
    ideas = idea.objects.all().order_by('-date')
    with open('/home/kingdom/Desktop/hackathon/temp/pragyanbhattarai04-Yatra_Hackathon_Team_Red/home/complains.txt', 'w') as file:
        for i in question:
            file.writelines(i.title)
            file.writelines("\n")
    with open('/home/kingdom/Desktop/hackathon/temp/pragyanbhattarai04-Yatra_Hackathon_Team_Red/home/probable_solutions.txt', 'w') as file:
        for i in ideas:
            file.writelines(i.title)
            file.writelines("\n")
    pdfs()
    return redirect('home')
