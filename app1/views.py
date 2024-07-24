from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product,Order,OrderUpdate,UserProfile,Booking,BookingUpdate,BlogPost,Comment
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.http import JsonResponse
from .forms import UserProfileForm

def k(request):
    return render(request,'app1/k.html')

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request,'app1/homm.html')

def order(request):
    products=Product.objects.all()
    params={'products':products}
    return render(request,'app1/order.html',params)



def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login before going to checkout')
        return redirect('login')
    products=Product.objects.all()
    params={'products':products}
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name1=request.POST.get('name', '')
        amount=request.POST.get('amount', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address', '')
        city=request.POST.get('city', '')
        zipcode=request.POST.get('zipcode', '')
        phone=request.POST.get('phone', '')

        order_items = json.loads(items_json)

        order_details_string = ""
        for item_key, details in order_items.items():
            quantity, name, price, imglink = details
            order_details_string += f"Item: {name}\n Quantity: {quantity}\n"

        order = Order(items_json= items_json, name=name1,amount=amount, email=email, address= address, city=city, zipcode=zipcode, phone=phone)
        order.save()
        user = request.user
        orderupdate = OrderUpdate.objects.create(user=user,orderupdate_id=order.order_id, items=order_details_string)
        thank=True
        id=order.order_id
        print(thank,id)
        return render(request, 'app1/checkout.html', {'thank':thank, 'id':id})
    return render(request,'app1/checkout.html',params)


def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES,instance=user_profile)
        if form.is_valid():
            form.save()
            updated_user_profile = UserProfile.objects.get(user=request.user)
            user = request.user
            orders = OrderUpdate.objects.filter(user=user).order_by('-timestamp')
            bookings = BookingUpdate.objects.filter(user=user).order_by('-bookingupdate_id')
            return render(request,'app1/dashboard.html', {'orders': orders,'user_profile':user_profile,'bookings':bookings})
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'app1/editprofile.html', {'form': form})

def contact(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'app1/contact.html')

def feedback(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        rating=request.POST.get('rating','')
        comments=request.POST.get('comments','')
        feed=Feedback(name=name,email=email,rating=rating,comments=comments)
        feed.save()
    return render(request,'app1/feedback.html')

def signuppage(request):
    error_message=""
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            error_message = "Your password and confirm password are not the same!"
        elif User.objects.filter(username=uname).exists():
            error_message = "Username already exists, please choose another username!"
        elif User.objects.filter(email=email).exists():
            error_message = "Email already exists, please choose another email!"
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'app1/signup.html',{'error_message': error_message})

def loginpage(request):
    error_message=""
    messages_list = messages.get_messages(request)
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('checkout')
        else:
            error_message = "Username or Password is incorrect!!!"
    return render (request,'app1/login.html',{'error_message': error_message})

def logoutpage(request):
    logout(request)
    return redirect('login')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    orders = OrderUpdate.objects.filter(user=user).order_by('-timestamp')
    user = request.user
    bookings = BookingUpdate.objects.filter(user=user).order_by('-bookingupdate_id')
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None
    return render(request,'app1/dashboard.html', {'orders': orders,'user_profile':user_profile,'bookings':bookings})

def booking(request):
    if request.method == "POST":
        remarks=request.POST.get('remarks','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        timed=request.POST.get('timed','')
        guests=request.POST.get('guests','')
        book=Booking(remarks=remarks,name=name,email=email,phone=phone,date=date,time=time,timed=timed,guests=guests)
        book.save()
        user = request.user
        bookupdate = BookingUpdate.objects.create(user=user,remarks=remarks,bookingupdate_id=book.booking_id,name=name,date=date,time=time,timed=timed,guests=guests)
    return render(request,'app1/booking.html')



def Blog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts=BlogPost.objects.all()
    params={'posts':posts}
    return render(request,'app1/blog.html',params)


# def post_detail(request, blog_id):
#     post = get_object_or_404(BlogPost, pk=blog_id)
#     comments = Comment.objects.filter(post_id=blog_id)

#     if request.method == 'POST':
#         comment = request.POST.get('comment')
#         user = request.user
#         post.comment_count += 1
#         post.save()
#         com = Comment(content=comment, commenter=user, post_id=blog_id)
#         com.save()
#         return JsonResponse({'success': True, 'comment': comment})
#     return render(request, 'app1/post_detail.html', {'post': post, 'comments': comments})




def post_detail(request, blog_id):
    post = get_object_or_404(BlogPost, pk=blog_id)
    comments = Comment.objects.filter(post_id=blog_id)
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    like_cnt = post.like_count

    if request.method == 'POST':
        if 'comment' in request.POST:
            print("hi3")
            comment = request.POST.get('comment')
            user = request.user
            post.comment_count += 1
            post.save()
            user_profile = UserProfile.objects.get(user=user)
            com = Comment(content=comment, commenter=user,comment_image=user_profile.image, post_id=blog_id)
            com.save()
            print(user_profile.image.url)
            return JsonResponse({'success': True, 'comment': comment,'commenter':user_profile.name,'comment_image':user_profile.image.url})
        else:
            if request.user.is_authenticated:
                user = request.user
                if user in post.likes.all():
                    post.likes.remove(user)
                    post.like_count -= 1
                    post.like_status = "no"
                    liked = False
                else:  
                    post.likes.add(user)
                    post.like_count += 1
                    liked = True
                    post.like_status = "yes"

                post.save()
                return JsonResponse({'success': True, 'liked': liked, 'like_count': post.like_count})
            else:
                return JsonResponse({'success': False, 'error': 'User is not authenticated'})
    return render(request, 'app1/post_detail.html', {'post': post, 'comments': comments,'like_cnt':like_cnt,'like_status':post.like_status,'user_profile':user_profile})







