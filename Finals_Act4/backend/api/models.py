from django.db import models

# Create your models here.


class Item(models.Model):
    # PERSONAL INFORMATION
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    name_ext = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    civil_status = models.CharField(max_length=20, blank=True, null=True)
    height_m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_type = models.CharField(max_length=10, blank=True, null=True)
    citizenship = models.CharField(max_length=50, blank=True, null=True)
    permanent_house_no = models.CharField(max_length=10, blank=True, null=True)
    permanent_street = models.CharField(max_length=100, blank=True, null=True)
    permanent_subd = models.CharField(max_length=100, blank=True, null=True)
    permanent_brgy = models.CharField(max_length=100, blank=True, null=True)
    permanent_city = models.CharField(max_length=100, blank=True, null=True)
    permanent_province = models.CharField(max_length=100, blank=True, null=True)
    permanent_zipcode = models.CharField(max_length=10, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    father_surname = models.CharField(max_length=100, blank=True, null=True)
    father_first_name = models.CharField(max_length=100, blank=True, null=True)
    father_middle_name = models.CharField(max_length=100, blank=True, null=True)
    father_name_ext = models.CharField(max_length=10, blank=True, null=True)
    mother_surname = models.CharField(max_length=100, blank=True, null=True)
    mother_first_name = models.CharField(max_length=100, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return (
            f"{self.first_name} {self.middle_name} {self.last_name} {self.email} {self.name_ext}"
            f"{self.gender} {self.date_of_birth} {self.place_of_birth} {self.civil_status}"
            f"{self.permanent_house_no} {self.permanent_street} {self.permanent_subd} {self.permanent_brgy} {self.permanent_city} {self.permanent_province} {self.permanent_zipcode} "
            f"{self.citizenship} {self.blood_type} {self.height_m} {self.weight_kg} {self.civil_status} "
            f"{self.father_surname} {self.father_first_name} {self.father_middle_name} {self.father_name_ext}"
            f"{self.mother_surname} {self.mother_first_name} {self.mother_middle_name} " 
          
        )