from django.shortcuts import render
from .models import Users,registration,AdminUsers
from django.core.files.storage import FileSystemStorage
 
# Create your views here.


def Home(request):
    return render(request,'Home.html',{})


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            #print(email,password)
            user = Users.objects.get(email=email)
            if user.password == password:
                request.session["user_email"]=email
                return render(request,'Home.html')
            else:
                return render(request,'login.html',{'msg':'Enter Correct Password','tag':'danger'})
        except Exception:
            return render(request,'login.html',{'msg':'Enter Correct Email','tag':'danger'})

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            mobile = request.POST.get('mobile')
            user = Users()
            user.name = name
            user.email = email
            user.password = password
            user.mobile = mobile
            user.save()
            return render(request,'signup.html',{'msg':'Successfully Signup','tag':'success'})
        except Exception:
            return render(request,'signup.html',{'msg':'Error on Signup','tag':'danger'})

def application(request):
    if request.method == 'GET':
        return render(request,'application.html')
    if request.method == 'POST':
        try:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            father = request.POST.get('father')
            mother = request.POST.get('mother')
            bdate = request.POST.get('bdate')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            sadd = request.POST.get('sadd')
            padd = request.POST.get('padd')
            district = request.POST.get('district')
            state = request.POST.get('state')
            lang = request.POST.get('lang')
            cast = request.POST.get('cast')
            Category = request.POST.get('Category')
            sboard = request.POST.get('sboard')
            spassyear = request.POST.get('spassyear')
            sscmark = request.POST.get('sscmark')
            sscmarkobt = request.POST.get('sscmarkobt')
            spercentage = request.POST.get('spercentage')
            hboard = request.POST.get('hboard')
            hpassyear = request.POST.get('hpassyear')
            hscmark = request.POST.get('hscmark')
            hscmarkobt = request.POST.get('hscmarkobt')
            hpercentage = request.POST.get('hpercentage') 
            gboard = request.POST.get('gboard')
            gpassyear = request.POST.get('gpassyear')
            gmark = request.POST.get('gmark')
            gmarkobt = request.POST.get('gmarkobt')
            print(gmarkobt)
            gpercentage = request.POST.get('gpercentage')
            ortho = request.POST.get('ortho')
            previousapp = request.POST.get('previousapp')
            r = registration()
            r.fname = fname
            r.lname = lname
            r.father = father
            r.mother = mother
            r.bdate = bdate
            r.mobile = mobile
            r.email = email
            r.sadd = sadd
            r.padd = padd
            r.district = district
            r.state = state
            r.lang = lang
            r.cast = cast
            r.Category = Category
            r.sboard = sboard
            r.spassyear = spassyear
            r.sscmark = sscmark
            r.sscmarkobt = sscmarkobt
            r.spercentage = spercentage
            r.hboard = hboard
            r.hpassyear = hpassyear
            r.hscmark = hscmark
            r.hscmarkobt = hscmarkobt
            r.hpercentage = hpercentage
            r.gboard = gboard
            r.gpassyear = gpassyear
            r.gmark = gmark
            r.gmarkobt = gmarkobt
            r.gpercentage = gpercentage
            r.ortho = ortho
            r.previousapp = previousapp
            r.save()
            return render(request,'application.html',{'msg':'Successfully Signup','tag':'success'})
        except Exception:
            return render(request,'application.html',{'msg':'Error on Signup','tag':'danger'}) 


def rules(request):
    return render(request,'rules.html',{})

def table(request):
    return render(request,'table.html',{})

def Eligibility(request):
    return render(request,'Eligibility.html',{})


def exampattern(request):
    return render(request,'exampattern.html',{}) 

def syllabus(request):
    return render(request,'syllabus.html',{})


def files(request):
    if request.method == 'GET':
        return render(request,'files.html')
    if request.method=='POST':
        try:
            uploaded_file=request.FILES['document']
            fs=FileSystemStorage()
            fs.save(uploaded_file.name,uploaded_file)
            return render(request,'files.html',{'msg':'Successfully uploaded data','tag':'success'})
        except Exception:
            return render(request,'files.html',{'msg':'Error on in upload data','tag':'danger'})

def logout(request):
    del request.session["user_email"]
    return render(request,'login.html')


def profile(request):
    return render(request,'profile.html')


def editapplication(request):
    appfiled = registration.objects.all()
    # appfiled2 = registration.objects.get(email=)
    return render(request,'editapplication.html',{'list':appfiled})

def alluser(request):
    user = Users.objects.all()
    return render(request,'alluser.html',{'list':user})


def adminlogin(request):
    if request.method == 'GET':
        return render(request,'adminlogin.html')
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email,password)
            user = AdminUsers.objects.get(email=email)
            if user.password == password:
                request.session["user_email"]=email
                return render(request,'alluser.html')
            else:
                return render(request,'alluser.html',{'msg':'Enter Correct Password','tag':'danger'})
        except Exception:
            return render(request,'alluser.html',{'msg':'Enter Correct Email','tag':'danger'})

    
def singleuser(request,id):
    user = Users.objects.get(id=id)
    return render(request,'singleuser.html',{'user':user})

def edituser(request,id):
    if request.method == 'GET':
        user = Users.objects.get(id=id)
        return render(request,'edituser.html',{'user':user})
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        user = Users.objects.get(id=id)
        user.name = name
        user.password = password
        user.mobile = mobile
        user.save()
        users_list = Users.objects.all()
        return render(request,'alluser.html',{'list':users_list})

def deleteuser(request,id):
    Users.objects.filter(id=id).delete()
    users_list = Users.objects.all()
    return render(request,'alluser.html',{'list':users_list})


def faqs(request):
    return render(request,'faqs.html',{})

def report(request):
    return render(request,'report.html',{})



