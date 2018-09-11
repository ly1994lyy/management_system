from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Students
# Create your views here.


class StudentView(ListView):
    queryset = Students.objects.all()
    template_name = 'students_list.html'
    context_object_name = 'student_list'


class StudentDetailView(DetailView):
    model = Students
    template_name = 'student_detail.html'
    context_object_name = 'student'


class StudentAddView(CreateView):
    model = Students
    fields = ['name', 'age', 'sex', 'classes']
    template_name = 'student_add.html'


class StudentEditView(UpdateView):
    model = Students
    fields = ['name', 'age', 'sex', 'classes']
    template_name = 'student_edit.html'


class StudentDelView(DeleteView):
    model = Students
    success_url = reverse_lazy('student_list')
    template_name = 'student_del.html'