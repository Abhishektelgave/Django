from django.shortcuts import render,get_object_or_404,redirect
from .models import Students,Courses
# Create your views here.
def student_registration(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       email = request.POST['email']
       student = Students(first_name=first_name, last_name=last_name, email=email)
       student.save()
       return redirect('course_list')
    return render(request, 'student_registration.html')

def enroll_course(request):
    if request.method == 'POST':
       student_id = request.POST['student_id']
       course_id = request.POST['course_id']
       student = get_object_or_404(Students, id=student_id)
       course = get_object_or_404(Courses, id=course_id)
       course.Students.add(student)
       return redirect('course_list')
    students = Students.objects.all()
    courses = Courses.objects.all()
    return render(request, 'enroll_course.html', {'students': students, 'courses': courses})


def course_list(request):
    courses = Courses.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    students = course.Students.all()
    return render(request, 'course_detail.html', {'course': course, 'students': students})


def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        discription = request.POST['description']
        course = Courses(name=name, discription=discription)
        course.save()
        return redirect('course_list')
    return render(request, 'add_course.html')