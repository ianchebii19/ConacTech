from email import message
from pyexpat.errors import messages
from turtle import title
from django.shortcuts import redirect, render
from . forms import *
from . models import *
from django.views import generic
from youtubesearchpython import VideoSearch
import requests
import wikipedia
# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')
def notes(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new note
               notes = Note( user = request.user, title = request.POST['title'], description = request.POST['description'])
               notes.save()
        message.success( request, f"Notes created successfully")
    else:
        form = NoteForm()

    # Get the notes for the current user
    notes = Note.objects.filter(user = request.user)

    context = {'notes': notes, 'form': form}
    return render(request, 'dashboard/notes.html', context)

"""def dnotes(request , pk=None):
     Note.objects.get( id=pk).delete()
     return redirect('notes')


def Notesdview(generic.DetailView):
     model =Note

def homew(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['finished']
                if finished == 'on':
                  finished =True
                else:
                    finished =False
                homework = Homework(
                    user = request.user,
                    suject = request.POST['suject'],
                    title = request.POST['title'],
                    description = request.POST['description'],
                    is_finished = request.POST['is_finished']
                )
                homework.save()
                message.Success(request, 'Homework added')
        else:
            form = HomeworkForm()
    homework = Homework.objects.filter(user =request.user)

    if len(homework) ==0:
         homework_done = True
    else:
       homework_done = False  
    context = {'homework':homework, 'form': form  , 'homework_done':homework_done}
    return render(request, 'dashboard/homework.html', context)

def updatehw(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished():
        homework.is_finished = True
    else:
        homework.is_finished = False
    homework.save()
    return redirect('homew')

def dhomew(request, pk=None):
    homework = Homework.objects.get(id=pk).delete()
    return redirect('homew')

def youtube(request):

    if request.method == 'POST':
        form =DashboardForm(request.POST)
        text = request.POST.get["text"]
        video = VideoSearch(text, limit =10)
        result_list = []
        for i in video.result()['result']:
            result_dict ={
                'input': text,
                'title': i['title'],
                'duration': i['duration'],
                'thumbnails': i['thumbnails'][0]['url'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'videoCount': i['videoCount']['short'],
                'publishedTime': i['publishedTime'],
                       }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc +=j['text']
            result_dict["description"] = desc
            result_list.append(result_dict)
            context ={"result": result_list, 'form': form}
            return render(request, 'dashboard/youtube.html')
    form = DashboardForm()
    context ={ 'form':form}
    return render(request, 'dashboard/youtube.html')

def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.Post['is_finished'
                                        if finished == 'on':
                                          finished =True
                                        else:
                                        finished = False
                                        ]
            except:
                finished = False
                todos= Todo (
                    user = request.user,
                    title = request.POST['title'],
                    is_finished = request.POST['is_finished'],
                )
                todos.save()
                message.success(request, 'Todo added successfully')
    else:
      form =TodoForm()
    todo = Todo.objects.filter(user=request.user)
    
    if len(todos) ==0:
         todo_done = True
    else:
       todo_done = False  
    context = { 'todo':todo, 'form': form}
    return render(request, 'dashboard/todo .html')

def updatetd(request, pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished():
        todo.is_finished = True
    else:
        todo.is_finished = False
    todo.save()
    return redirect('todo')
def dtodo(request, pk=None):
    todo= Todo.objects.get(id=pk).delete()
    return redirect('todo')
def books(request):
   return render(request, 'dashboard/books.html')

def youtube(request):

    if request.method == 'POST':
        form =DashboardForm(request.POST)
        text = request.POST.get["text"]
        url = 'https://ww.google.com/books/vl/volumes?q'+text
        r =requests.get(url)
        answer = r.json()
        for i in range(10):
            result_dict ={
                'title': answer['items'][i]['volumeInfo']['title'],
                'subtitle':  answer['items'][i]['volumeInfo'].get['subtitle'],
                'description':  answer['items'][i]['volumeInfo'].get['description'],
                'count':  answer['items'][i]['volumeInfo'].get['count'],
                'categories':  answer['items'][i]['volumeInfo'].get['categories'],
                'rating':  answer['items'][i]['volumeInfo'].get['pagerating'],
                'thumnail':  answer['items'][i]['volumeInfo'].get['imageLinks'],
                'preview': answer['items'][i]['volumeInfo'].get['previewlink'],
            }
            result_list.append(result_dict)
            context ={"result": result_list, 'form': form}
            return render(request, 'dashboard/youtube.html')
        else:
            form = DashboardForm()
    context ={ 'form':form}
    return render(request, 'dashboard/books.html')

def dic(request):
    
    if request.method == 'POST':
        form =DashboardForm(request.POST)
        text = request.POST.get["text"]
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/?'+text
        r =requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            try
                phenotics = answer[0]['phenotics'][0]['text']
                audio = answer[0]['phenotics'][0]['audio']
                definition = answer[0]['meanings'][0]['definitions'][0]['definition']
                example = answer[0]['meanings'][0]['definitions'][0]['example']
                synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
                context ={"form": form, 'input': text, 'phonetics':phenotics, 'definition': definition, 'synonyms':synonyms, 'audio':audio, 'example':example   }
            expect:
            context ={"form": form, 'input':''}
            return render(request, 'dashboard/dictionary.html')
        else:
            form = DashboardForm()
    context ={ 'form':form}
    return render(request, 'dashboard/dictionary.html', context)

def wiki(request):
    
    if request.method == 'POST':
        form =DashboardForm(request.POST)
        text = request.POST.get["text"]
        url = 'https://ww.google.com/books/vl/volumes?q'+text
        r =requests.get(url)
        answer = r.json()
        for i in range(10):
            result_dict ={
                'title': answer['items'][i]['volumeInfo']['title'],
                'subtitle':  answer['items'][i]['volumeInfo'].get['subtitle'],
                'description':  answer['items'][i]['volumeInfo'].get['description'],
                'count':  answer['items'][i]['volumeInfo'].get['count'],
                'categories':  answer['items'][i]['volumeInfo'].get['categories'],
                'rating':  answer['items'][i]['volumeInfo'].get['pagerating'],
                'thumnail':  answer['items'][i]['volumeInfo'].get['imageLinks'],
                'preview': answer['items'][i]['volumeInfo'].get['previewlink'],
            }
            result_list.append(result_dict)
            context ={"result": result_list, 'form': form}
            return render(request, 'dashboard/youtube.html')
        else:
            form = DashboardForm()
    context ={ 'form':form}
    return render(request, 'dashboard/books.html')

def dic(request):
    
    if request.method == 'POST':
        form =DashboardForm(request.POST)
        text = request.POST.get["text"]
        search = wikipedia.pages[text]
        context ={"form": form, 'title' :search.title, 'link': search.url, 'details':search.summary   }
    else:
            form = DashboardForm()
    context ={ 'form':form}
    
    return render(request, 'dashboard/wiki.html')

def conv(request):
    if request.method =='POST':
        form =ConversionForm(request.POST)
        if request.POST['measurement'] == 'length':
            measurement_form = ConversionLengthForm()
            context ={
                'form': form,
                'm_form': measurement_form,
                'input' :True
            }
            if 'input' in request.POST:
                first =request.POST['measure1']
                second = request.POST['measurement2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >= 0:
                    if first == 'yard' and second == 'foot':
                        answer = f'{input} yard = {int(input)*3} foot'
                    if first == 'foot' and second == 'yard' : 
                        answer = f'{input} yard ={int(input)/3} yard

                context ={
                    'form': form,
                    'input' : True,
                    'answer': answer,
                    'm_form': measurement_form,
                  

                }   
        if request.POST['measurement'] == 'mass':
            measurement_form = ConversionMassForm()
            context ={
                'form': form,
                'm_form': measurement_form,
                'input' :True
            }
            if 'input' in request.POST:
                first =request.POST['measure1']
                second = request.POST['measurement2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >= 0:
                    if first == 'pound' and second == 'kilogram':
                        answer = f'{input} pound = {int(input)*0.45} kilogram'
                    if first == 'kilogram' and second == 'pound' : 
                        answer = f'{input} kilogram ={int(input)/0.45} pound

                context ={
                    'form': form,
                    'input' : True,
                    'answer': answer,
                    'm_form': measurement_form,
                  

                }      

    form = ConversionForm()
    context={'form': form, 'input': False
             }
    
    return render(request, "dashboard/conversion.html")

def register(request):
  if request.method =='POST':
      form =UserRegistrationForm()
      if form.is_valid():
         form.save()
         username =form.clean_data('username')
         messages.success(request, f'Account created succesfull')
         redirect('login')
  else:
      form =UserRegistrationForm()
  context ={'form':form}
  return render(request, "dashboard/register.html", context)


def profile(request):
    homework = Homework.objects.filter(is_finished=False, user=request.user)
    todos = Todo.objects.filter(is_finished=False, user=request.user)
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False

    context ={
        'homework': homework,
        'todos' : todos,
        'homework_done': homework_done,
        'todos_done': todos_done


    }
    return render(request, 'dashboard/profile.html', context)
    
"""