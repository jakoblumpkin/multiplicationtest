from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Test
from .extracode import testUser, findObject, gradeTest

# Create your views here.

def home(request):
    print(findObject('alex'))
    return render(request, 'home.html')


def firstQ(request):
    #adds user to database for test
    if request.method=='POST':
        thisuser=User.objects.get_or_create(username=request.POST["name"])
        testUser.append(request.POST["name"])
        Test.objects.get_or_create(username=User.objects.get(username=request.POST["name"]))
    context={"name": testUser[-1]}
    return render(request, 'index.html', context)


#grades question number1
def secondQ(request):
    if request.method=='POST':
        answer=request.POST['an']
        if answer==('a' or 'A'):
            objId=findObject(testUser[-1])
            obj=Test.objects.get(id=objId)
            obj.question1='correct'
            obj.save()
        else:
            objId = findObject(testUser[-1])
            obj = Test.objects.get(id=objId)
            obj.question1 = 'incorrect'
            obj.save()
    return render(request, 'sec.html')


#grades question number 2
def thirdQ(request):
    if request.method == 'POST':
        answer = request.POST['an']
        if answer == ('c' or 'C'):
            objId = findObject(testUser[-1])
            obj = Test.objects.get(id=objId)
            obj.question2 = 'correct'
            obj.save()
        else:
            objId = findObject(testUser[-1])
            obj = Test.objects.get(id=objId)
            obj.question2 = 'incorrect'
            obj.save()
    return render(request, 'third.html')

#grades question number 3
def fourthQ(request):
    if request.method == 'POST':
        answer = request.POST['an']
        if answer == ('d' or 'D'):
            objId = findObject(testUser[-1])
            obj = Test.objects.get(id=objId)
            obj.question3 = 'correct'
            obj.save()
        else:
            objId = findObject(testUser[-1])
            obj = Test.objects.get(id=objId)
            obj.question3 = 'incorrect'
            obj.save()
    return render(request, 'fourth.html')
#grades question number4
def gradeFourth(request):
    if request.method == 'POST':
        answer = request.POST['an']
        if answer == ('a' or 'A'):
            objId = findObject(testUser[-1])
            obj = Test.objects.get(id=objId)
            obj.question4 = 'correct'
            obj.save()
        else:
            objId = findObject(testUser[-1])
            obj = Test.objects.get(id=objId)
            obj.question4 = 'incorrect'
            obj.save()
    return redirect('/finalgrade/')

#Display final grade
def finalGrade(request):
    objId = findObject(testUser[-1])
    finalA=gradeTest(objId)
    context={"final": finalA}
    return render(request, 'finalGrade.html', context)