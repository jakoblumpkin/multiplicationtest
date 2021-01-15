from .models import Test
testUser=[]

#find id of object with name
def findObject(name):
    obj=Test.objects.all()
    for i in obj:
        if str(i.username)==name:
            return i.id

#function that grades the test
def gradeTest(id):
    count=0
    obj=Test.objects.get(id=id)
    if obj.question1=='correct':count+=1
    if obj.question2 == 'correct': count += 1
    if obj.question3 == 'correct': count += 1
    if obj.question4 == 'correct': count += 1
    passed='Congratulations you passed with a'
    failed='You failed with a'
    if count/4==0.75:
        return f'{passed} 75%'
    if count/4==0.50:
        return f'{failed} 50% Try Again!'
    if count/4==1.00:
        return f'{passed} 100%'
    if count / 4 == 0.25:
        return f'{failed} 25% Try Again!'
    if count / 4 == 0.00:
        return f'{failed} 0% Try Again!'