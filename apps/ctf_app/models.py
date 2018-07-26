from __future__ import unicode_literals
import bcrypt
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z\s]\w+')


class UserManager(models.Manager):
    def validate_login(self, postData):
        errors = []
        # check DB for email
        if len(self.filter(username=postData['username'])) > 0:
            # check this user's password
            user = self.filter(username=postData['username'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors.append('Password Incorrect!')
        else:
            errors.append('username not found!')
        if errors:
            return errors
        return user

    def validate_registration(self, postData):
        errors = []

        if len(postData['name']) < 2:
            errors.append("Names must be at least 3 characters!")

        if len(postData['username']) < 2:
            errors.append("username must be at least 3 characters!")

        #error handling for passwords
        if len(postData['password']) < 8:
            errors.append("Passwords must be at least 8 characters!")

        # error handling for  letter characters
        if not re.match(NAME_REGEX, postData['name']):
            errors.append('Names must contain letter characters only!')

        #error handling for uniqueness of username
        if len(User.objects.filter(username=postData['username'])) > 0:
            errors.append("This username is already in use!")

        #error handling for password matches
        if postData['password'] != postData['password_confirm']:
            errors.append("Passwords do not match")

        if not errors:
            # make our new user
            # hash password
            hashed = bcrypt.hashpw(
                (postData['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                name=postData['name'],
                username=postData['username'],
                email=postData['email'],
                password=hashed,
            )
            return new_user
        return errors


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.name, self.username

    


