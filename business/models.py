from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify
from utility.models import Category,City,Locality,Response_Status,Response_Form,Call_Status,Intested_Type,Intested_For
from django.contrib.auth.models import User
# Create your models here.


class Response(models.Model):
    response = models.ForeignKey(Response_Form, on_delete=models.DO_NOTHING, blank=True, null=True ,)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=True )
    number = models.CharField(max_length=12)
    name = models.CharField(max_length=500)    
    status = models.ForeignKey(Response_Status, blank=True, null=True, on_delete=models.DO_NOTHING,)
    intested_for = models.ManyToManyField(Intested_For, blank=True, null=True,)
    comment = models.TextField()
    call_status = models.ForeignKey(Call_Status, blank=True,null=True, on_delete=models.DO_NOTHING,)
    
    submitter = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " -- " + self.number + " -- " + self.comment
    class Meta:
        verbose_name_plural='1. Response'

 
class Business_Info(models.Model):
    category = models.ForeignKey(Category,blank=True, null=True ,on_delete=models.DO_NOTHING)
    locality = models.ForeignKey(Locality,blank=True, null=True ,on_delete=models.DO_NOTHING)
    business_info=models.CharField(max_length=100)
    full_address=models.CharField(max_length=100)
    contact_person=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=100)
    image=models.ImageField(upload_to="image")
    slug = models.SlugField(max_length=200, blank=True)
    intested_type = models.ForeignKey(Intested_Type,blank=True, null=True , on_delete=models.DO_NOTHING,)
    intested_for = models.ManyToManyField(Intested_For)      
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.locality.city.city_name +''+ self.category.name  +''+ self.business_info)
        super(Business_Info, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural='2. Business Info'
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.business_info + ",  " + self.full_address + ",  " + self.locality.name + ",  " + self.contact_person + ",  " + self.contact_number

# -------------------------------------------------------------------------------------------------------------
class Follow_Up(models.Model):
    response = models.ForeignKey(Response,blank=True, null=True , on_delete=models.CASCADE)
    business_info = models.ForeignKey(Business_Info,blank=True, null=True , on_delete=models.CASCADE)
    follow_up = models.DateTimeField(blank=True, null=True ,)
    comment = models.CharField(max_length=500)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    class Meta:
        verbose_name_plural='3. Follow Up'

class Meeting(models.Model):
    response = models.ForeignKey(Response,null=True,blank=True,on_delete=models.DO_NOTHING,)
    business_info = models.ForeignKey(Business_Info,null=True,blank=True,on_delete=models.DO_NOTHING,)
    meeting = models.DateTimeField(null=True, blank=True)
    comment = models.CharField(max_length=500)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment + ',' + self.meeting + ',' + self.business_info + ',' + self.response 
    
    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name_plural='4. Meeting'

class Visit(models.Model):
    response = models.ForeignKey(Response,null=True,blank=True,on_delete=models.DO_NOTHING,)
    business_info = models.ForeignKey(Business_Info,null=True,blank=True,on_delete=models.DO_NOTHING,)
    comment = models.CharField(max_length=500)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment + ',' + self.meeting + ',' + self.business_info + ',' + self.response 

    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name_plural='5. Visit'

#-------------------------------------------------------------------------------------------------------

class For_Job(models.Model):
    response = models.ForeignKey(Response,blank=True, null=True , on_delete=models.DO_NOTHING,)
    business_info = models.ForeignKey(Business_Info, blank=True, null=True , on_delete=models.DO_NOTHING,)
    comment = models.CharField(max_length=500)  
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment
    class Meta:
        verbose_name_plural='6. For Job'


class For_Coaching(models.Model):
    response = models.ForeignKey(Response,blank=True, null=True , on_delete=models.DO_NOTHING,)
    business_info = models.ForeignKey(Business_Info,blank=True, null=True, on_delete=models.DO_NOTHING,)
    comment = models.CharField(max_length=500)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    class Meta:
        verbose_name_plural='7. For Coaching'

class Internship(models.Model):
    response = models.ForeignKey(Response,blank=True, null=True , on_delete=models.DO_NOTHING,)
    business_info = models.ForeignKey(Business_Info, blank=True, null=True , on_delete=models.DO_NOTHING,)
    comment = models.CharField(max_length=500) 
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name_plural='8. Internship'

# --------------------------------------------------------------------------------------------------------------




