# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.


class FriendManager(models.Manager):
    def make_friend(self, user, friend):
        if len(Friend.objects.filter(userr_id=user).filter(usera_id=friend))>0:
            print 'no'
            return None
        else:
            friend = Friend.objects.create(userr_id=user, usera_id=friend)
            other = Friend.objects.create(userr_id=friend.id, usera_id=user)
            print 'yes'
            friend.save()
            other.save()
            return friend

    def remove_friend(self, user, friend):
        Friend.objects.filter(userr_id=user).filter(usera_id=friend).delete()

        return

    def grab_friend(self, user):
        results = {'users':None, 'friends':None}
        user = User.objects.get(id=user)
        try:
            users = User.objects.all()
            potentials = []
            for potential in users:
                if (potential.id != user.id):
                    potentials.append(potential)
        except:
            users = None

        try:
            friends = Friend.objects.filter(userr=user)
            made_friends = []
            for friend in friends:
                made_friends.append(friend.usera)
            others = []
            for potential in potentials:
                if (potential not in made_friends):
                    others.append(potential)
        except:
            friends = None

        results['users'] = others
        results['friends'] = made_friends
        return results

class BlockManager(models.Manager):
    def make_block(self, user, friend):
        if len(Block.objects.filter(blokr_id=user).filter(bloka_id=friend))>0:
            return None
        else:
            friend = Block.objects.create(blokr_id=user, bloka_id=friend)
            other = Block.objects.create(blokr_id=friend.id, bloka_id=user)
            friend.save()
            other.save()
            return friend

    def remove_block(self, user, friend):
        Block.objects.filter(blokr_id=user).filter(bloka_id=friend).delete()

        return

    def grab_block(self, user):
        results = {'blockers':None, 'block':None}
        user = User.objects.get(id=user)
        try:
            users = User.objects.all()
            potentials = []
            for potential in users:
                if (potential.id != user.id):
                    potentials.append(potential)
        except:
            users = None

        try:
            blocks = Block.objects.filter(blokr=user)
            made_blocks = []
            for block in blocks:
                made_blocks.append(block.bloka)
            others = []
            for potential in potentials:
                if (potential not in made_blocks):
                    others.append(potential)
        except:
            blocks = None

        results['blockers'] = others
        results['block'] = made_blocks
        return results


class Friend(models.Model):
    userr = models.ForeignKey(User, related_name='userf_request')
    usera = models.ForeignKey(User, related_name='userf_acceptor')
    objects = FriendManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Block(models.Model):
    blokr = models.ForeignKey(User, related_name='userb_request')
    bloka = models.ForeignKey(User, related_name='userb_acceptor')
    objects = BlockManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
