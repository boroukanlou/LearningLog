from django.shortcuts import redirect, render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.


def home_page(request):
    return render(request, 'Notes/home_page.html')


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('added_date')
    context = {
        'topics': topics
    }
    return render(request, 'Notes/topics.html', context)


@login_required
def topic(request, topicId):
    topic = Topic.objects.get(id=topicId)
    if topic.owner != request.user:
        raise Http404('this page is not found')
    entries = topic.entry_set.order_by('-added_date')
    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'Notes/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            newTopic = form.save(commit=False)
            newTopic.owner = request.user
            newTopic.save()
            return redirect('Notes:topics')

    context = {
        'form': form
    }
    return render(request, 'Notes/new_topic.html', context)


@login_required
def new_entry(request, topicId):
    topic = Topic.objects.get(id=topicId)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('Notes:topic', topicId=topicId)
    context = {
        'form': form,
        'topic': topic
    }
    return render(request, 'Notes/new_entry.html', context)


@login_required
def edit_entry(request, entryId):
    entry = Entry.objects.get(id=entryId)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404('this page is not found')

    if request.method != 'POST':
        form = EntryForm(instance=entry)

    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Notes:topic', topicId=topic.id)

    context = {
        'entry': entry,
        'topic': topic,
        'form': form
    }
    return render(request, 'Notes/edit_entry.html', context)
