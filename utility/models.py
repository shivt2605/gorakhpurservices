from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.

class Main_Category(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to="maincategory")
    slug = models.SlugField(max_length=200, blank=True)
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Main_Category, self).save(*args, **kwargs)

    def save_formset(self, request,formset, ):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.entered_by = request.user
            instance.save()
        formset.save_m2m()
        
    class Meta:
        verbose_name_plural='1. Main Category'
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.name
    
    

class Category(models.Model):
    main_category = models.ForeignKey(Main_Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to="category")
    slug = models.SlugField(max_length=200, blank=True)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural='2. Categories'
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.name + " -- " + self.main_category.name
    

class City(models.Model):
    city_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="city")
    slug = models.SlugField(max_length=200, blank=True)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.city_name)
        super(City, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural='3. City'
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.city_name    



class Locality(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Locality, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural='4. Locality'
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.name + " -- " + self.city.city_name
   

# Create your models here.
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
class Response_Status(models.Model):
    status = models.CharField(max_length=500)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.status    
    class Meta:
        verbose_name_plural='5. Response Status'


class Response_Form(models.Model):
    response_from = models.CharField(max_length=500)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.response_from   
    class Meta:
        verbose_name_plural='6. Response Form'

class Call_Status(models.Model):
    name = models.CharField(max_length=500)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='7. Call Status'


class Intested_Type(models.Model):
    status = models.CharField(max_length=500)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.status    
    class Meta:
        verbose_name_plural='8. Intested Type'

class Intested_For(models.Model):
    status = models.CharField(max_length=500)
    submitter = models.ForeignKey(User,blank=True, null=True, on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.status    
    class Meta:
        verbose_name_plural='9. Intested For'
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
 
