# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(req):
    courses = Course.objects.all()
    context = {
        'courses' : courses
    }
    return render(req, 'courses_app/index.html', context)

def add(req):
    if req.method == "POST":
        Course.objects.create(name= req.POST['name'], desc= req.POST['desc'])
        return redirect('/courses')
    else:
        return redirect('/courses')

def remove(req, id):
    course = Course.objects.get(id=id)
    context = {
        'course' : course
    }
    return render(req, 'courses_app/delete.html', context)

def delete(req, id):
    Course.objects.get(id = id).delete()
    return redirect('/courses')
