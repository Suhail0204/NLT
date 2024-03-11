from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import users_collection
from django.views.decorators.csrf import csrf_exempt
from transformerAPI import *
from googletrans import Translator
from google_trans_new import google_translator
# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        lang = request.POST['lang']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        record = {"name" : name ,"email" : email ,"language" : lang,"password" : password,"confirm password" : cpassword}
        users_collection.insert_one(record)
    return render(request,'register.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        record = {"email":username,"password":password}
        logincheck = users_collection.find_one(record)
        if logincheck != None:
            return HttpResponseRedirect('home')
        else :
            return HttpResponse("Invalid credential")
    return render(request,'index.html')

@csrf_exempt
def home(request):
    global output
    output ={}
    if request.method == "POST":
        txtmsg = request.POST['txtmsg']
        output = query({"inputs": txtmsg, "parameters" : { "src_lang":"en_XX","tgt_lang":"ta_IN"}})
    return render(request,'homepage.html',{"translatedtxt" : output})



def API(request):
    translator = google_translator()  
    translate_text = translator.translate('สวัสดีจีน',lang_tgt='en')  
    print(translate_text)
    return HttpResponse(translate_text)
#     translator = Translator(service_urls=['translate.googleapis.com'])
#     translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
#     print(translation.text) 
#     return HttpResponse(translation.text) 