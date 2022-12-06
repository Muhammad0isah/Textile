from django.db import models

# Create your models here.

class detail(models.Model):
	FOOD_TYPE = (
		('CST/18/IFT/00125','CST/18/IFT/00125'),
		('CST/18/IFT/00119','CST/18/IFT/00119'),
		('CST/18/IFT/00118','CST/18/IFT/00118'),
		('CST/18/IFT/00107','CST/18/IFT/00107'),
		('CST/18/IFT/00101','CST/18/IFT/00101'),
		('CST/18/IFT/00109','CST/18/IFT/00109'),
		('CST/18/IFT/00140','CST/18/IFT/00140'),

	)
	FirstName = models.CharField(max_length=30)
	LastName = models.CharField(max_length=30)
	PhoneNumber = models.CharField(max_length=11)
	Reg_No = models.CharField(max_length=30, choices = FOOD_TYPE)
	StreetAddress = models.CharField(max_length=50)
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=30)