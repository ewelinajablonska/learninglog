from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """The home page for the requesting logs"""
    return render(request, 'learning_log/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all int entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_log/topic.html', context)