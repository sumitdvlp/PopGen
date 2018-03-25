from django.contrib.auth.models import User
from .models import Job,JobFinal
from django import forms
from django import forms
from django.core.urlresolvers import reverse_lazy, reverse

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field,ButtonHolder
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from crispy_forms.bootstrap import FormActions
from crispy_forms import layout, bootstrap
from crispy_forms.layout import (
    Layout, Div, BaseInput, Field, HTML, Submit, TEMPLATE_PACK,
)

from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset,Button


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.CharField(widget=forms.EmailInput)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

class JobForm(forms.ModelForm):


    class Meta:
        model=Job
        exclude=['user']

class JobFormFinalUpdate(forms.ModelForm):

    class Meta:
        model=JobFinal
        exclude=['user','job_name','job_status','op_file_url']

class JobFormFinal(forms.ModelForm):

    class Meta:
        model=JobFinal
        exclude=['user','op_file_url','job_status']
    '''
    def __init__(self, *args, **kwargs):
        super(JobFormFinal, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = True
        self.helper.form_method="POST"
        self.helper.add_input(Submit('submit', 'Save Data',css_class="btn-sucess"))

        self.helper.template_pack=TEMPLATE_PACK
    
        self.helper.layout = layout.Layout(
            TabHolder(
                Tab('1. Job/Project Details',
                    'synthesize',
                    'job_name','project_name',
                ),
                Tab('2. Entities',
                    'entities','housing_entities','person_entities',
                ),
                Tab('3. Column Names',
                'hid', 'pid', 'geo','region','sample_geo',
                ),
                Tab('4. Input Files',
                    'geo_to_sample', 'region_to_sample', 'region_to_geo', 'sample_household', 'sample_person',
                    'sample_groupquarter',
                    'geo_household_files','geo_person_files','geo_groupquarter_files','region_household_files',
                    'region_person_files',
                    'region_groupquarter_files',
                ),
                Tab('5. Control Variables',
                    'desc','arc','region_household','region_groupquarter','region_person',
                    'geo_household','geo_groupquarter','geo_person',
                    ),
                Tab('6. Parameters',
                    'ipf_tolerance',
                    'iterations', 'zmc', 'rp', 'apf',
                    ),
                Tab('7. Reweighting',
                    'procedure',
                    'rew_tolerance', 'inner_iterations', 'outer_iterations', 'rapf',
                    ),
                Tab('8. Draws',
                    'procedure',
                    'draws_iterations', 'seed',
                    ),
                Tab('9. Geos To Synthesize',
                    'region_ids',
                    'region_all_ids', 'geo_ids', 'geo_all_ids',
                    ),
                Tab('10. Outputs',
                    'performance',
                    'export', 'collate_across_geos',
                    ),
                Tab('11. Multiway One',
                    'multiway_variables_one',
                    'filename_one', 'filetype_one', 'entity_one',
                    ),
                Tab('11. Multiway Two',
                    'multiway_variables_two',
                    'filename_two', 'filetype_two', 'entity_two',
                    ),

            ),
            Field('Job_Pushed', css_class="extra"),
        )
    '''

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','password']


