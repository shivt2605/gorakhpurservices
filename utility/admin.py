from django.contrib import admin
from .models import *

# ---------------------------------------------------Register your models here.------------------------------------------


class Main_Category_admin(admin.ModelAdmin):    
    list_display=('id','name','image_tag','slug','user','created_at','update_at')
    list_editable=('name',)
admin.site.register(Main_Category,Main_Category_admin)


# ---------------------------------------------------Register your models here.------------------------------------------

class Category_admin(admin.ModelAdmin):    
    list_display=('id','name','image_tag','slug','submitter','created_at','update_at')
    list_editable=('name',)
admin.site.register(Category,Category_admin)

# ---------------------------------------------------Register your models here.------------------------------------------

class City_admin(admin.ModelAdmin):    
    list_display=('id','city_name','image_tag','slug','submitter','created_at','update_at')    
admin.site.register(City,City_admin)

# ---------------------------------------------------Register your models here.------------------------------------------

class Locality_admin(admin.ModelAdmin):    
    list_display=('id','name','slug','submitter','created_at','update_at')
    list_editable=('name',)
admin.site.register(Locality,Locality_admin)

# ---------------------------------------------------Register your models here.------------------------------------------
class Response_Form_admin(admin.ModelAdmin):    
    list_display=('id','response_from','submitter','created_at','update_at')    
admin.site.register(Response_Form,Response_Form_admin)

# ---------------------------------------------------Register your models here.------------------------------------------


class Response_Status_admin(admin.ModelAdmin):    
    list_display=('id','status','submitter','created_at','update_at')    
admin.site.register(Response_Status,Response_Status_admin)

# ---------------------------------------------------Register your models here.------------------------------------------

class Call_Status_admin(admin.ModelAdmin):    
    list_display=('id','name','submitter','created_at','update_at')    
admin.site.register(Call_Status,Call_Status_admin)


# ---------------------------------------------------Register your models here.------------------------------------------
class Intested_Type_admin(admin.ModelAdmin):    
    list_display=('id','submitter','created_at','update_at')    
admin.site.register(Intested_Type,Intested_Type_admin)


# ---------------------------------------------------Register your models here.------------------------------------------
class Intested_For_admin(admin.ModelAdmin):    
    list_display=('id','status','submitter','created_at','update_at')    
admin.site.register(Intested_For,Intested_For_admin)


