from django.db import models

class hr(models.Model):
     hr_required_deg = models.CharField(max_length=100)
     requestedby = models.CharField(max_length=50)
     reson_new_hire = models.CharField(max_length=500)
     remarks = models.CharField(max_length=250)
     preparedBy = models.CharField(max_length=50)
     arrovedBy = models.CharField(max_length=50)
     createdOn = models.DateTimeField(auto_now=True)

     # def __str__(self):
     #    return self.hr_text

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

     # def __str__(self):
     #    return self.employe_text

class experience(models.Model):
     employe_id = models.CharField(max_length=25)
     organization = models.CharField(max_length=75)
     no_of_years_served = models.IntegerField()
     work_experience = models.IntegerField()
     created_On = models.DateTimeField(auto_now=True)

     # def __str__(self):
     #    return self.experience_text

class competency_Matrix(models.Model):
     position = models.CharField(max_length=75)
     education_Background = models.CharField(max_length=150)
     experience = models.IntegerField()
     competency_Requirement = models.CharField(max_length=250)
     created_On = models.DateTimeField(auto_now=True)

     # def __str__(self):
     #    return self.competency_Matrix_text

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

     # def __str__(self):
     #    return self.training_Request_Register_text

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
     jan = models.CharField(max_length=20)
     feb = models.CharField(max_length=20)
     mar = models.CharField(max_length=20)
     apr = models.CharField(max_length=20)
     may = models.CharField(max_length=20)
     jun = models.CharField(max_length=20)
     jul = models.CharField(max_length=20)
     aug = models.CharField(max_length=20)
     sep = models.CharField(max_length=20)
     Oct = models.CharField(max_length=20)
     nov = models.CharField(max_length=20)
     dec = models.CharField(max_length=20)
     remarks = models.CharField(max_length=250)
     legend = models.CharField(max_length=250)
     prepard_By = models.CharField(max_length=250)
     approved_By = models.CharField(max_length=250)
     created_On = models.DateTimeField(auto_now=True)

     # def __str__(self):
     #    return self.annual_trainnig_text

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

     # def __str__(self):
     #    return self.training_evalution_record_text














