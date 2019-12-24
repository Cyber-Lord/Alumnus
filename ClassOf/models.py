from django.db import models
from django.contrib.auth.models import User



GENDER = (("M","Male"),("F","Female"),("P","Prefer not to say"))

class School(models.Model):
	name 			= models.CharField("School Name", max_length=20)
	school_address 	= models.CharField(max_length=50)
	school_email 	= models.CharField(max_length=30)
	state 			= models.CharField(max_length=50)
	country 		= models.CharField(max_length=50)
	motto 			= models.CharField(max_length=50)
	institution_head= models.CharField(max_length=30)
	admin 			= models.ForeignKey(User, on_delete=models.PROTECT)
	logo 			= models.ImageField(upload_to="logo/")


class Faculty(models.Model):
	faculty_name 	= models.CharField(max_length = 60)
	faculty_id 		= models.CharField(max_length = 5)
	faculty_deen 	= models.CharField(max_length = 25)
	school 			= models.ForeignKey(School, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Faculties"

class Department(models.Model):
	dept_name 		= models.CharField(max_length = 50)
	dept_id 		= models.CharField(max_length = 5)
	dept_hod 		= models.CharField(max_length = 25)
	faculty 		= models.ForeignKey(Faculty, on_delete = models.CASCADE)
	admin 			= models.ForeignKey(User, on_delete=models.PROTECT)

	def get_dept_name(self):
		return self.dept_name

	def get_dept_id(self):
		return self.dept_id

	def __str__(self):
		return self.dept_name

class Graduate(models.Model):
	user 			= models.ForeignKey(User, on_delete=models.PROTECT)
	first_name 		= models.CharField(max_length = 15)
	last_name 		= models.CharField(max_length = 15)
	other_name 		= models.CharField(max_length = 15, blank = True, null = True)
	phone_number 	= models.CharField(max_length = 15, blank = True, null = True)
	email_address 	= models.EmailField()
	department 		= models.ForeignKey(Department, on_delete=models.CASCADE)
	lga_of_origin 	= models.CharField(max_length = 15)
	state_of_origin = models.CharField(max_length = 15)
	fav_quote = models.TextField(blank = True, null = True)
	admission_year 	= models.IntegerField()
	best_experience = models.TextField(blank = True, null = True)
	worst_experience = models.TextField(blank = True, null = True)
	nationality 	= models.CharField(max_length = 25)
	birth_day 		= models.DateField()
	gender			= models.CharField(max_length= 15, choices=GENDER)
	photo 			= models.ImageField(upload_to = "Photos/")


	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	def get_photos(self):
		return self.photo.url
