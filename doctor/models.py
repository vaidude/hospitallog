# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class reg(models.Model):
    STATUS_CHOICE=(
        ('pending','PENDING'),
        ('approved','APPROVED'),
        ('rejected','REJECTED'),
    )
    name=models.CharField(max_length=30)
    pid=models.CharField(max_length=10)
    email=models.CharField(max_length=100,null=True,blank=True)
    phno=models.IntegerField()
    passw=models.CharField(max_length=30)
    cpassw=models.CharField(max_length=30)
    status=models.CharField(max_length=30,choices=STATUS_CHOICE,default='pending')


class drreg(models.Model):
    dimage=models.ImageField(upload_to='media/')
    dname=models.CharField(max_length=30)
    did=models.CharField(max_length=10)
    ddep=models.CharField(max_length=30)
    dphn=models.IntegerField()
    fee=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    dpass=models.CharField(max_length=30)
    dpassre=models.CharField(max_length=30)

class breg(models.Model):
    STATUS_CHOICE=(
        ('pending','PENDING'),
        ('approved','APPROVED'),
        ('rejected','REJECTED'),
    )
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    phno=models.IntegerField()
    dname=models.CharField(max_length=30)
    did=models.CharField(max_length=30)
    dphn=models.IntegerField()
    ddep=models.CharField(max_length=100)
    fee=models.CharField(max_length=30)
    bdate=models.CharField(max_length=30)
    btime=models.CharField(max_length=30)
    status=models.CharField(max_length=30,choices=STATUS_CHOICE,default='pending')

class lreg(models.Model):
    lname=models.CharField(max_length=30)
    lpass=models.CharField(max_length=30)

class labservice(models.Model):
    category=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    time=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    tokens=models.IntegerField()


class lbreg(models.Model):
    name=models.CharField(max_length=30)
    pid=models.CharField(max_length=10)
    phno=models.IntegerField()
    category=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.CharField(max_length=300)
    time=models.CharField(max_length=100)
    lbdate=models.CharField(max_length=30)
    tokens=models.IntegerField()

class pay(models.Model):
    pid=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    phno=models.CharField(max_length=20)
    did=models.CharField(max_length=30)
    dname=models.CharField(max_length=30)
    dphn=models.IntegerField()
    ddep=models.CharField(max_length=100)
    bdate=models.CharField(max_length=30)
    fee=models.CharField(max_length=30)
    priscription=models.ImageField(upload_to='media/')

class labpay(models.Model):
    name=models.CharField(max_length=30)
    pid=models.CharField(max_length=10)
    phno=models.IntegerField()
    category=models.CharField(max_length=30)
    price=models.IntegerField()
    lbdate=models.CharField(max_length=30)
    result=models.ImageField(upload_to='media/')


class ChatRoom(models.Model):
    user = models.ForeignKey('reg', on_delete=models.CASCADE, related_name='chat_rooms')
    designer = models.ForeignKey('drreg', on_delete=models.CASCADE, related_name='chat_rooms')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'designer']

class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender_type = models.CharField(max_length=10, choices=[('FARMER', 'Farmer'), ('BUYER', 'Buyer')])
    sender_id = models.IntegerField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']


from django.utils.timezone import now

class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)  
    receiver = models.CharField(max_length=100)  
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)
    media=models.FileField(upload_to='chat_media/',null=True,blank=True)

    def _str_(self):
        return f"From {self.sender} to {self.receiver}"

