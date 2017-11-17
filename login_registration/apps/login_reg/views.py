# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt
# Create your views here.
def index(req):
    if 'id' not in req.session:
        req.session['id']=0
    if 'name' not in req.session:
        req.session['name']=""
    return render(req, 'login_reg/index.html')

def register(req):
    if req.method == "POST":
        results = User.objects.validate_register(req.POST)
        if len(results):
            for result in results:
                messages.error(req, results[result])
            return redirect('/')
        else:
            unhash = req.POST['pwd']
            pwd = bcrypt.hashpw(unhash.encode(), bcrypt.gensalt())
            User.objects.create(first_name=req.POST['fname'], last_name= req.POST['lname'],email_id = req.POST['email'],birthday = req.POST['bday'], age = req.POST['age'], gender = req.POST['gender'],password = pwd)
            req.session['name'] = req.POST['fname']
            messages.success(req, "Successfully registered (or logged in)!" )
            return redirect('/success')

def success(req):
    return render(req, 'login_reg/success.html')    

def login(req):
    results = User.objects.validate_login(req.POST)
    if results:
        for result in results:
            messages.error(req, results[result])
    else:
        user = User.objects.filter(email_id=req.POST['username'])
        if len(user) > 0:
            hash1 = user[0].password
            if bcrypt.checkpw(req.POST['pwd'].encode(), hash1.encode()):
                req.session['id'] = user[0].id
                req.session['name'] = user[0].first_name
                messages.success(req, "Successfully registered (or logged in)!")
                return redirect('/success')
            else:
                messages.error(req, "Invalid username or password")
        else:
            messages.error(req, "Please verify username or password")
    return redirect('/')
