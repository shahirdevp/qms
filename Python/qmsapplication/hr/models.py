from django.db import models

class hr(models.Model):
     hr_required_deg = models.CharField(max_length=100)
     requestedby = models.CharField(max_length=50)
     reson_new_hire = models.CharField(max_length=500)
     remarks = models.CharField(max_length=250)
     preparedBy = models.CharField(max_length=50)
     arrovedBy = models.CharField(max_length=50)
     createdOn = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.hr_required_deg

class employe(models.Model):
     name_of_the_Employee = models.CharField(max_length=50)
     address = models.TextField(max_length=500)
     employee_ID = models.CharField(max_length=25)
     fathers_name = models.CharField(max_length=50)
     date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
     qualification = models.CharField(max_length=75)
     date_of_join = models.DateField(auto_now=False, auto_now_add=False)
     languages_known = models.CharField(max_length=250)
     position = models.CharField(max_length=50)
     created_On = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.name_of_the_Employee

class experience(models.Model):
     employe_id = models.CharField(max_length=25)
     organization = models.CharField(max_length=75)
     no_of_years_served = models.IntegerField()
     work_experience = models.IntegerField()
     created_On = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.employe_id

class competency_Matrix(models.Model):
     position = models.CharField(max_length=75)
     education_Background = models.CharField(max_length=150)
     experience = models.IntegerField()
     competency_Requirement = models.CharField(max_length=250)
     created_On = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.position

class training_Request_Register(models.Model):
     training_Required = models.CharField(max_length=150)
     training_to = 	models.CharField(max_length=50)
     training_Suggested_by = 	models.CharField(max_length=150)
     reason_for_Training	= models.CharField(max_length=250)
     date	= models.DateField(auto_now=False, auto_now_add=False)
     remarks = models.CharField(max_length=250)
     prepared_By = 	models.CharField(max_length=50)
     approved_By = 	models.CharField(max_length=50)
     created_On = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.training_Required

class annual_trainnig(models.Model):
     years = (
          ('2018','2018'),
          ('2019','2019'),
          ('2020','2020'),
          ('2021','2021'),
          ('2022','2022'),
          ('2023','2023'),
          ('2024','2024'),
          ('2025','2025'),
          ('2026','2026'),
     )
     year = models.CharField(max_length=1, choices=years)
     topic = models.CharField(max_length = 10)
     department_or_person = models.CharField(max_length= 50)
     jan = models.CharField(max_length=20, blank=True)
     feb = models.CharField(max_length=20, blank=True)
     mar = models.CharField(max_length=20, blank=True)
     apr = models.CharField(max_length=20, blank=True)
     may = models.CharField(max_length=20, blank=True)
     jun = models.CharField(max_length=20, blank=True)
     jul = models.CharField(max_length=20, blank=True)
     aug = models.CharField(max_length=20, blank=True)
     sep = models.CharField(max_length=20, blank=True)
     Oct = models.CharField(max_length=20, blank=True)
     nov = models.CharField(max_length=20, blank=True)
     dec = models.CharField(max_length=20, blank=True)
     remarks = models.CharField(max_length=250)
     legend = models.CharField(max_length=250, blank=True)
     prepard_By = models.CharField(max_length=250)
     approved_By = models.CharField(max_length=250, blank=True)
     created_On = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.topic

# training evalution record
class training_evalution_record(models.Model):
     scores = (
          ('3','understood , Implemented , can train  others '),
          ('2','Undestood implemented '),
          ('1','undrestood'),
          ('0','Not Understood Require retraining .'),
     )
     trg_no = models.IntegerField()
     training_topic = models.CharField(max_length=50)
     date_of_trainig = models.DateField(auto_now=False, auto_now_add=True)
     date_of_join = models.DateField(auto_now=False, auto_now_add=True)
     faculty = models.CharField(max_length=50)
     venue = models.CharField(max_length=50)
     name_of_participant = models.CharField(max_length=50)
     score = models.CharField(max_length=1, choices=scores)
     evaluation_criteria = models.TextField(max_length=300)
     Effectiveness_of_Training = models.TextField(max_length=300)
     evaluated_By = models.CharField(max_length=50)
     created_On = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.training_evalution_record_text














