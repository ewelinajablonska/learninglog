from django.http.response import Http404
from django.shortcuts import redirect, render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """The home page for the requesting logs"""
    return render(request, 'learning_log/index.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all int entries"""
    topic = Topic.objects.get(id=topic_id)
    #Make shure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_log/topic.html', context)

@login_required
def new_topic(request):
    """Add new topic."""
    if request.method != 'POST':
        #No data submited, create a blank form
        form = TopicForm()
    else:
        #POST data submited; process data.
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_log:topics')
    
    #Display a blank or invalid form.
    context = {'form' : form}
    return render(request, 'learning_log/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #No data submited, create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return redirect('learning_log:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_log/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_log:topic', topic_id=topic.id)

    # Display a blank or invalid form.
    context = {'entry' : entry, 'topic': topic, 'form': form}
    return render(request, 'learning_log/edit_entry.html', context)
