# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
NAME_REGEX = re.compile(r'^([^0-9]*)$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWD_REGEX = re.compile(r'^(?=.*?[A-Z]).*\d')
# Create your models here.
class UserManager(models.Manager):
    def validate_register(self, postdata):
        errors = {}

        if postdata['fname'] == "" :
            errors['fname'] = "Please enter Firstname"
        else:            
            if len(postdata['fname']) < 2:
                errors["fname"] = "First Name should not be fewer than 2 characters"
            if not NAME_REGEX.match(postdata['fname']):
                errors['fname'] = "Numeric characters are not allowed in Firstname"
        
        if postdata['lname'] == "":
            errors['lname'] = "Please enter Lastname"
        else:
            if len(postdata['fname']) < 2:
                errors["lname"] = "Last Name should not be fewer than 2 characters"
            if not NAME_REGEX.match(postdata['fname']):
                errors['lname'] = "Numeric characters are not allowed in Lastname"

        if postdata['email'] == "":
            errors['email'] = "Please enter Email Id"
        else:
            if not EMAIL_REGEX.match(postdata['email']):
                errors["email"] = "Invalid Email Address! please follow abc@xyz.com"

        if postdata['pwd'] == "":
            errors['pwd'] = "Please enter passwod"
        else:
            if len(postdata['pwd']) < 8:
                errors['pwd'] = " Password must be 8 characters long"
            if not PWD_REGEX.match(postdata['pwd']):
                errors['pwd'] = "Invalid password! Password must contain atleast 1 Uppercase and 1 numeric value "
            
        if postdata['cpwd'] == "":
            errors['cpwd'] = "Please enter confirm passwod"
        else:
            if postdata['pwd'] != postdata['cpwd']:
                errors['pwd'] = "Confirm Password does not match with Password "

        return errors

    
    def validate_login(self, postdata):
        errors = {}
        if postdata['username'] == "":
            errors['username'] = "Please enter email or userid"        
        if postdata['pwd'] == "":
            errors['pwd'] = "Please enter password"            
        return errors
            


class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    birthday = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    password = models.CharField(default="", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()