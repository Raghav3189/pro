from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
import uuid

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,default="User")
    image = models.ImageField(upload_to="app1/images", default="/media/app1/imagesloginimage1.jpg")
    location = models.CharField(max_length=100,default="Laughtale")
    email = models.EmailField(default="User@gmail.com")
    def __str__(self):
        return self.user.username

class Product(models.Model):
    product_id=models.IntegerField(default=0)
    product_category=models.CharField(max_length=100,default="")
    product_name=models.CharField(max_length=40,default="")
    product_desc=models.CharField(max_length=300,default="")
    product_price=models.IntegerField(default=0)
    product_image=models.ImageField(upload_to="app1/images",default="")
    product_rating=models.IntegerField(default=0)
    product_time=models.IntegerField(default=0)
    product_discountprice=models.IntegerField(default=0)

    def __str__(self):
        return self.product_name 

class Order(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    zipcode=models.CharField(max_length=111)
    phone=models.CharField(max_length=111)
    def __str__(self):
        return self.name+"-"+str(self.order_id)

class OrderUpdate(models.Model):
    orderupdate_id= models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.TextField(default="")
    mymessage=models.CharField(max_length=500,default="The Order Has Been Placed Sucessfully")
    timestamp = models.DateTimeField(auto_now_add=True)
    ordercontact=models.CharField(max_length=20,default="9965479094")
    def __str__(self):
        return str(self.orderupdate_id)

class Booking(models.Model):
    booking_id= models.AutoField(primary_key=True)
    remarks= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    phone=models.CharField(max_length=111)
    date=models.CharField(max_length=111)
    time=models.CharField(max_length=111)
    timed=models.CharField(max_length=111)
    guests=models.CharField(max_length=111)
    def __str__(self):
        return str(self.booking_id)

class BookingUpdate(models.Model):
    bookingupdate_id=models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=111,default="pending")
    name=models.CharField(max_length=90)
    date=models.CharField(max_length=111)
    time=models.CharField(max_length=111)
    timed=models.CharField(max_length=111)
    guests=models.CharField(max_length=111)
    def __str__(self):
        return str(self.bookingupdate_id)


class BlogPost(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_category = models.CharField(default="",max_length=100)
    blog_image = models.ImageField(upload_to="app1/images",default="")
    blog_title = models.CharField(default="",max_length=200)
    blog_author = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_author_image = models.ImageField(upload_to="app1/images",default="")
    blog_time = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='post')
    like_status = models.CharField(default="",max_length=100)

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_image = models.ImageField(upload_to="app1/images",default="/media/app1/imagesloginimage1.jpg")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



