# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login.models import User
from django.contrib import messages
from .models import Friend, Block


# Create your views here.
def index(request):
    if 'logged' not in request.session:
        return redirect('login:index')
    else:
        try:
            context = {
                    'user': User.objects.get(id=int(request.session['logged'])),
                    'recents': User.objects.order_by('-pk')[2],
                    'more' : User.objects.order_by('-pk')[1],
                    'most' :User.objects.order_by('-pk')[0],
                }
            return render(request, 'friend/index.html', context)
        except:
            return redirect('login:index')


def list(request):
    if 'logged' not in request.session:
        return redirect('login:index')
    else:
        user = int(request.session['logged'])
        grab = Friend.objects.grab_friend(user)
        grab_blocks = Block.objects.grab_block(user)
        others = grab['users']
        block = grab_blocks['block']
        friends = grab['friends']
        context = {
            'logged': User.objects.get(id=int(request.session['logged'])),
            'users' : others,
            'friends': friends,
            'blocks':block,
        }
        return render(request, 'friend/list.html',context)

def add(request):
    if 'logged' not in request.session:
        return redirect('login:index')
    else:
        user = int(request.session['logged'])
        grab = Friend.objects.grab_friend(user)
        others = grab['users']
        friends = grab['friends']
        context = {
            'logged': User.objects.get(id=int(request.session['logged'])),
            'users' : others,
            'friends': friends,
        }
        return render(request, 'friend/add.html', context)

def block(request):
    if 'logged' not in request.session:
        return redirect('login:index')
    else:
        user = int(request.session['logged'])
        grab = Block.objects.grab_block(user)
        others = grab['blockers']
        block = grab['block']
        context = {
            'logged': User.objects.get(id=int(request.session['logged'])),
            'users' : others,
            'block': block,
        }
    return render(request, 'friend/block.html', context)

def make_friend(request, id):
    if 'logged' not in request.session:
        return redirect('login:index')
    user = int(request.session['logged'])
    friend = int(id)
    friend_make = Friend.objects.make_friend(user, friend)
    return redirect('friend:add')

def remove(request, id):
    if 'logged' not in request.session:
        return redirect('login:index')
    user = int(request.session['logged'])
    friend = int(id)
    remove_friend = Friend.objects.remove_friend(user, friend)
    return redirect('friend:list')

def make_block(request, id):
    if 'logged' not in request.session:
        return redirect('login:index')
    user = int(request.session['logged'])
    friend = int(id)
    block_make = Block.objects.make_block(user, friend)
    return redirect('friend:block')

def remove_block(request, id):
    if 'logged' not in request.session:
        return redirect('login:index')
    user = int(request.session['logged'])
    friend = int(id)
    remove_block = Block.objects.remove_block(user, friend)
    return redirect('friend:list')

def profile(request, id):
    if 'logged' not in request.session:
        return redirect('login:index')
    friend = User.objects.get(id=id)
    context = {
        'friend':friend
    }
    return render(request, 'friend/profile.html', context)
