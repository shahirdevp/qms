from django.contrib import admin

from .models import hr, employe, experience, competency_Matrix, training_Request_Register, annual_trainnig, training_evalution_record
admin.site.register(hr)
admin.site.register(employe)
admin.site.register(experience)
admin.site.register(competency_Matrix)
admin.site.register(training_Request_Register)
admin.site.register(annual_trainnig)
admin.site.register(training_evalution_record)
