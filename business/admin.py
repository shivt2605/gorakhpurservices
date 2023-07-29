from django.contrib import admin
from .models import *

class Internship_admin(admin.ModelAdmin):
    list_display=('id','response','submitter', 'created_at','update_at')

    list_per_page = 20 
admin.site.register(Internship,Internship_admin)

class Meeting_admin(admin.ModelAdmin):
    list_display=('id','response','business_info','meeting','comment','submitter', 'created_at','update_at')
    list_editable=('business_info','meeting','comment',) 
    list_filter = ('business_info','meeting','comment',) 
    search_fields = ('business_info','meeting','comment',)
    list_per_page = 20 
admin.site.register(Meeting,Meeting_admin)

class Follow_Up_admin(admin.ModelAdmin):
    list_display=('id','response','business_info', 'follow_up', 'comment','submitter', 'created_at','update_at')
    list_editable=('follow_up',) 
    list_filter = ('follow_up',) 
    search_fields = ('follow_up',)
    list_per_page = 20 
admin.site.register(Follow_Up,Follow_Up_admin)

class Visit_admin(admin.ModelAdmin):
    list_display=('id','response','business_info', 'comment','submitter', 'created_at','update_at')
    list_editable=('comment',) 

    search_fields = ('comment',)
    list_per_page = 20 
admin.site.register(Visit,Visit_admin)

class For_Coaching_admin(admin.ModelAdmin):
    list_display=('id','response', 'comment','submitter', 'created_at','update_at')
    list_editable=('comment',) 

    search_fields = ('comment',)
    list_per_page = 20 
admin.site.register(For_Coaching,For_Coaching_admin)

class For_Job_admin(admin.ModelAdmin):
    list_display=('id','response','business_info', 'comment','submitter', 'created_at','update_at')
    list_editable=('comment',) 

    search_fields = ('comment',)
    list_per_page = 20
admin.site.register(For_Job,For_Job_admin)


class Meeting(admin.TabularInline):
    model = Meeting

class Follow_Up(admin.TabularInline):
    model = Follow_Up

class Visit(admin.TabularInline):
    model = Visit

class For_Coaching(admin.TabularInline):
    model = For_Coaching

class For_Job(admin.TabularInline):
    model = For_Job
    
class Internship(admin.TabularInline):
    model = Internship


class Response_admin(admin.ModelAdmin):
    inlines = (Meeting,Follow_Up,Visit,For_Coaching,For_Job,Internship)  
    list_display=['id','city','name','number','status','call_status','comment','submitter','created_at','update_at']
    list_editable=('name','status','call_status',) 
    list_filter = ('submitter','created_at','update_at','call_status','status','city',) 
    search_fields = ('name','number','comment',)
    list_per_page = 20 
admin.site.register(Response,Response_admin)




class Business_Info_admin(admin.ModelAdmin):
    inlines = (Meeting,Follow_Up,Visit,)
    list_display=('id','category','locality','business_info','full_address','contact_person','contact_number','intested_type','image_tag','slug','submitter','created_at','update_at')
    list_filter = ('intested_type','submitter','created_at','update_at')  
    list_editable=('category','locality','business_info','full_address','contact_person','contact_number','intested_type',)  
    search_fields = ('business_name','full_address','contact_person','contact_number',)
    list_per_page = 25
admin.site.register(Business_Info,Business_Info_admin)



