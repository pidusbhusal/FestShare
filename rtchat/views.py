from django.shortcuts import render, get_object_or_404,  redirect, get_object_or_404
from .models import ChatGroup, GroupMessage
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required
# Create your views here.
def chat_view(req):
    chat_group = get_object_or_404(ChatGroup, group_name = "public_chat")
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()
 
    if req.method == 'POST':
        form = ChatmessageCreateForm(req.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = req.user
            message.group = chat_group
            message.save()
            return redirect('/Chat')
    return render(req, 'Chat.html', {'chat_messages': chat_messages, 'form': form})