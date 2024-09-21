from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.views import generic
from django.contrib import messages  # Import messages for success/error messages
import requests
from youtubesearchpython import VideosSearch
import wikipedia

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new note
            notes = Note(user=request.user, title=form.cleaned_data['title'], description=form.cleaned_data['description'])
            notes.save()
            messages.success(request, "Notes created successfully")
    else:
        form = NoteForm()

    # Get the notes for the current user
    notes = Note.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'dashboard/notes.html', context)

def dnotes(request, pk=None):
    Note.objects.get(id=pk).delete()
    return redirect('notes')

class Notesdview(generic.DetailView):
    model = Note

def homew(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            finished = request.POST.get('is_finished') == 'on'
            homework = Homework(
                user=request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                due=request.POST['due'],
                is_finished=finished
            )
            homework.save()
            messages.success(request, 'Homework added successfully')
            return redirect('homew')  # Redirect to avoid form resubmission on refresh
    else:
        form = HomeworkForm()
    
    homework = Homework.objects.filter(user=request.user)
    homework_done = not homework.exists()  # Simplify the check for homework completion

    context = {
        'homework': homework,
        'form': form,
        'homework_done': homework_done
    }
    return render(request, 'dashboard/homework.html', context)

def updatehw(request, pk=None):
    homework = Homework.objects.get(id=pk)
    homework.is_finished = not homework.is_finished
    homework.save()
    return redirect('homew')

def dhomew(request, pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homew')

def youtube(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            try:
                video = VideosSearch(text, limit=10)  # Ensure VideosSearch is the correct method
                result_list = []
                for i in video.result()['result']:
                    result_dict = {
                        'input': text,
                        'title': i['title'],
                        'duration': i['duration'],
                        'thumbnail': i['thumbnails'][0]['url'],  # Corrected to 'thumbnail'
                        'channel': i['channel']['name'],
                        'link': i['link'],
                        'views': i['viewCount']['short'],
                        'publishedTime': i['publishedTime'],
                    }
                    desc = ''
                    if i.get('descriptionSnippet'):
                        for j in i['descriptionSnippet']:
                            desc += j['text']
                    result_dict["description"] = desc
                    result_list.append(result_dict)

                context = {'results': result_list, 'form': form}  # Changed 'result' to 'results'
                return render(request, 'dashboard/youtube.html', context)
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
    
    form = DashboardForm()
    context = {'form': form}
    return render(request, 'dashboard/youtube.html', context)
def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST.get('is_finished')
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False

            todos = Todo(
                user=request.user,
                title=form.cleaned_data['title'],  # Removed extra space
                is_finished=finished,
            )
            todos.save()
            messages.success(request, 'Todo added successfully')
    else:
        form = TodoForm()
        
    todos = Todo.objects.filter(user=request.user)
    if len(todos) == 0:  # Fixed typo: changed 'todo' to 'todos'
        todo_done = True
    else:
        todo_done = False

    context = {'todos': todos, 'form': form, 'todo_done': todo_done}  # Use 'todo_done' to match the template
    return render(request, 'dashboard/todo.html', context)

def updatetd(request, pk=None):
    todo = Todo.objects.get(id=pk)
    todo.is_finished = not todo.is_finished
    todo.save()
    return redirect('todo')

def dtodo(request, pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')

def books(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url ='http://www.googleapis.com/books/v1/volumes?q='+text 
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                "title":answer['items'][i]['volumeInfo']['title'],
                "subtitle":answer['items'][i]['volumeInfo'].get['subtitle'],
                "description":answer['items'][i]['volumeInfo'].get['description'],
                "count":answer['items'][i]['volumeInfo'].get['pageCount'],
                "categories":answer['items'][i]['volumeInfo'].get['title'],
                "rating":answer['items'][i]['volumeInfo'].get['pageRating'],
                "thumbnail":answer['items'][i]['volumeInfo'].get['imageLinks'],
                "preview":answer['items'][i]['volumeInfo'].get['previewLinks'],
                     
            }
            result_list.append(result_dict)
            context = {'results': result_list, 'form': form}  # Changed 'result' to 'results'
        return render(request, 'dashboard/books.html', context)
    else:
        form = DashboardForm()
    context = {'form': form}    
    return render(request, 'dashboard/books.html', context)

def dic(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            url = f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{text}'
            r = requests.get(url)
            answer = r.json()
            result_list = []
            try:
                phonetics = answer[0]['phonetics'][0]['text']
                audio = answer[0]['phonetics'][0]['audio']
                definition = answer[0]['meanings'][0]['definitions'][0]['definition']
                example = answer[0]['meanings'][0]['definitions'][0].get('example', '')
                synonyms = answer[0]['meanings'][0]['definitions'][0].get('synonyms', [])
                context = {
                    "form": form,
                    'input': text,
                    'phonetics': phonetics,
                    'definition': definition,
                    'synonyms': synonyms,
                    'audio': audio,
                    'example': example
                }
            except:
                context = {"form": form, 'input': ''}
            return render(request, 'dashboard/dictionary.html', context)
    else:
        form = DashboardForm()
    context = {'form': form}
    return render(request, 'dashboard/dictionary.html', context)

import wikipedia  # Ensure you have imported the wikipedia module

def wiki(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        try:
            # Use wikipedia.search to handle potential disambiguation
            search_results = wikipedia.search(text)
            if search_results:
                # Get the first result's page
                page_title = search_results[0]
                search = wikipedia.page(page_title)
                context = {
                    "form": form,
                    'title': search.title,
                    'link': search.url,
                    'details': search.summary
                }
            else:
                # No results found
                context = {
                    "form": form,
                    'error': "No results found for the given query."
                }

        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation error - provide options to the user
            context = {
                "form": form,
                'error': f"Disambiguation error: The term '{text}' may refer to multiple topics.",
                'options': e.options  # List of possible options
            }

        except wikipedia.exceptions.PageError:
            # Handle page not found error
            context = {
                "form": form,
                'error': f"No page found for '{text}'."
            }

        except Exception as e:
            # General exception handling
            context = {
                "form": form,
                'error': f"An error occurred: {str(e)}"
            }

        return render(request, 'dashboard/wiki.html', context)
    
    else:
        form = DashboardForm()
        context = {'form': form}
    return render(request, 'dashboard/wiki.html', context)


def conv(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            measurement = form.cleaned_data['measurement']
            if measurement == 'length':
                measurement_form = ConversionLengthForm()
                context = {
                    'form': form,
                    'm_form': measurement_form,
                    'input': True
                }
                if 'input' in request.POST:
                    first = request.POST['measurement1']
                    second = request.POST['measurement2']
                    input_value = request.POST['input']
                    answer = ''
                    if input_value and int(input_value) >= 0:
                        if first == 'yard' and second == 'foot':
                            answer = f'{input_value} yard = {int(input_value) * 3} foot'
                        elif first == 'foot' and second == 'yard':
                            answer = f'{input_value} foot = {int(input_value) / 3} yard'
                    context['answer'] = answer

            if measurement == 'mass':
                measurement_form = ConversionMassForm()
                context = {
                    'form': form,
                    'm_form': measurement_form,
                    'input': True
                }
                if 'input' in request.POST:
                    first = request.POST['measurement1']
                    second = request.POST['measurement2']
                    input_value = request.POST['input']
                    answer = ''
                    if input_value and int(input_value) >= 0:
                        if first == 'pound' and second == 'kilogram':
                            answer = f'{input_value} pound = {int(input_value) * 0.45} kilogram'
                        elif first == 'kilogram' and second == 'pound':
                            answer = f'{input_value} kilogram = {int(input_value) / 0.45} pound'
                    context['answer'] = answer

            return render(request, "dashboard/conversion.html", context)
    
    form = ConversionForm()
    context = {'form': form, 'input': False}
    return render(request, "dashboard/conversion.html", context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, "dashboard/register.html", context)

def profile(request):
    homework = Homework.objects.filter(is_finished=False, user=request.user)
    todos = Todo.objects.filter(is_finished=False, user=request.user)
    todos_done = len(todos) == 0
    homework_done = len(homework) == 0

    context = {
        'homework': homework,
        'todos': todos,
        'homework_done': homework_done,
        'todos_done': todos_done
    }
    return render(request, 'dashboard/profile.html', context)
