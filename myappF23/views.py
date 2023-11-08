from django.shortcuts import render

from django.http import HttpResponse
from .models import Category, Course, Student, Instructor
from .forms import InterestForm
from django.shortcuts import get_object_or_404

from django.views.generic import DetailView
def index(request):
    category_list = Category.objects.all().order_by('id')[:10]
    instructor_list = Instructor.objects.all().order_by('id')[:10]
    forms=InterestForm()
    return render(request, 'myappF23/index.html', {'category_list': category_list,'instructor_list':instructor_list, 'forms':forms})


def about(request):
    return render(request,'myappF23/about.html')


class TestView(DetailView):
    model=Category
    template_name="myappF23/test.html"
    context_object_name = 'category'

def detail(request,category_no):
    category = get_object_or_404(Category,pk=category_no)

    courses=category.course_set.all()
    return render(request,'myappF23/detail.html',{"category":str(category),"courses":courses})

def instructor_detail(request,instructor_id):
    instructor = get_object_or_404(Instructor,pk=instructor_id)

    courses=instructor.course_set.all()

    students=instructor.students.all()

    return render(request,'myappF23/instructor_detail.html', {
        "instructor":instructor,
        "courses":courses,
        "students":students
    })

def courses(request):

    courses=Course.objects.all().order_by('id')


    return render(request,'myappF23/courses.html', {
    "courses":courses, })