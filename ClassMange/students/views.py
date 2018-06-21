from django.shortcuts import render, get_object_or_404
from .models import Stu, Score
from .forms import AddForms
from django.http import HttpResponseRedirect


# Create your views here.


def home(request):
    context = {}
    return render(request, 'home.html', context)


def student_list(request):
    students = Stu.objects.all()
    context = {}
    context['students'] = students
    return render(request, 'students.html', context)


def edit_stu(request, stu_pk):
    student = get_object_or_404(Stu, pk=stu_pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        student.name = name
        student.age = age
        student.save()
        return HttpResponseRedirect('/students')
    context = {}
    context['student'] = student
    return render(request, 'edit.html', context)


def add_stu(request):
    if request.method == 'POST':
        add_form = AddForms(request.POST)
        if add_form.is_valid():
            name = add_form.cleaned_data['name']
            age = add_form.cleaned_data['age']
            sex = add_form.cleaned_data['sex']
            classes = add_form.cleaned_data['classes']
            new_stu = Stu()
            new_stu.name = name
            new_stu.age = age
            new_stu.sex = sex
            new_stu.classes = classes
            new_stu.save()
            return HttpResponseRedirect('/students')
    else:
        add_form = AddForms()
    context = {}
    context['add_form'] = add_form
    return render(request, 'add.html', context)


def stu_del(request, stu_pk):
    student = Stu.objects.filter(pk=stu_pk)
    student.delete()
    context = {}
    msg ='删除成功！'
    context['msg'] = msg
    return render(request, 'delete.html', context)


def score_list(request):
    scores = Score.objects.all()
    context = {}
    context['scores'] = scores
    return render(request, 'score.html', context)