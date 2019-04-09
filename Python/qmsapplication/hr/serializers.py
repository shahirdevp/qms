from rest_framework import serializers
from hr.models import *

class HrlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = hr
        fields = ('id', 'hr_required_deg', 'requestedby', 'reson_new_hire', 'remarks', 'preparedBy', 'arrovedBy', 'createdOn')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employe
        fields = ('id', 'name_of_the_Employee', 'address', 'employee_ID', 'fathers_name', 'date_of_birth', 'qualification', 'date_of_join', 'languages_known', 'position', 'created_On')

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = experience
        fields = ('id', 'employe_id', 'organization', 'no_of_years_served', 'work_experience', 'created_On', )

class CompetencySerializer(serializers.ModelSerializer):
    class Meta:
        model = competency_Matrix
        fields = ('id', 'position', 'education_Background', 'experience', 'competency_Requirement', 'created_On', )

class TrainingReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_Request_Register
        fields = ('id', 'training_Required', 'training_to', 'training_Suggested_by', 'reason_for_Training', 'date', 'remarks', 'prepared_By', 'approved_By', 'created_On', )

class AnualTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = annual_trainnig
        fields = ('id', 'year', 'topic', 'department_or_person', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'Oct', 'nov', 'dec', 'remarks', 'legend', 'prepard_By', 'approved_By', 'created_On', )

class TeEvRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = training_evalution_record
        fields = ('id', 'trg_no', 'training_topic', 'date_of_trainig', 'date_of_join', 'faculty', 'venue', 'name_of_participant', 'score', 'evaluation_criteria', 'Effectiveness_of_Training', 'evaluated_By', 'created_On', )


class SkillMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = skillmatrix
        fields = ('id', 'depaertment', 'designation', 'empId', 'empName', 'drawing_studying_skills', 'usage_of_general_gauges', 'usage_of_general_instruments', 'usage_of_product_specific_gauges', 'quality_documentation', 'cmm_operating', 'pp_operating', 'operating_surface_roughness_tester', 'basic_machining_knowledge', 'microscope_handeling', 'internal_verification_skills', 'inspection_skill', 'visual_inspection_skill', 'd_height_gauge_operating', 'scoring_crieteria', 'prepredBy', 'approvedBy', 'created_On', )