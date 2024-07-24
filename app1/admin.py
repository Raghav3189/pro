from django.contrib import admin
from .models import Product,Order,OrderUpdate,UserProfile,Booking,BookingUpdate,BlogPost,Comment
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderUpdate)
admin.site.register(UserProfile)
admin.site.register(Booking)
admin.site.register(BookingUpdate)
admin.site.register(BlogPost)
admin.site.register(Comment)

