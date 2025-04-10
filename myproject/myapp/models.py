from django.db import models

class BussinessContact(models.Model):
    name = models.CharField(max_length= 255 , null= True ,blank= True)
    address = models.CharField(max_length= 255 , null= True ,blank= True)
    
    def __str__(self):
        return f'  {self.name}   {self.address} '








class Author(models.Model):
    id = models.CharField( max_length=5 ,primary_key=True , auto_created=True)
    firstname = models.CharField(max_length= 255 )
    lastname = models.CharField(max_length= 255 )
    phone = models.CharField(max_length= 255 , null= True ,blank= True)
    join_date = models.DateField(null= True ,blank= True)
    contact = models.OneToOneField(BussinessContact ,on_delete=models.CASCADE , default = "")
    
    def __str__(self):
        return f'  {self.firstname}   {self.lastname}   {self.phone}'




# Create your models here.
class Video ( models.Model):
    title = models.CharField(max_length= 255)   
    published_date = models.DateField()
    short_details = models.CharField(max_length= 255 , null= True ,blank= True)
    author = models.ForeignKey (Author,max_length=255 ,on_delete=models.DO_NOTHING ,null=True , blank=True)

    def __str__(self):
        return self.title
    


class Course(models.Model):
    title = models.CharField(max_length= 255)   
    video = models.ManyToManyField(Video ,default="" ,related_name='videos' ,related_query_name='q_video')
   
    def __str__(self):
        return self.title
    
class Product(models.Model):
    ptype = models.CharField(max_length= 255)     
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')    
   
    def __str__(self):
        return self.ptype  
    
