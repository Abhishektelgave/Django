from django.shortcuts import render

# Create your views here.
def home(request):
    fruits=['Apple','Banana','orange','Mango']
    students=['Abhishek','chandan','darshan','amit']
    context={
        'fruits':fruits,
        'students':students
    }
    return render(request,'home1.html',context)