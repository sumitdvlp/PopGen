from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import Permission, User,UserManager

from django.core.urlresolvers import reverse, reverse_lazy
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}/{2}'.format(instance.user.username,instance.job_name,filename)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    job_priority = models.CharField(max_length=5)
    job_name = models.CharField(max_length=50)
    project_name = models.CharField(max_length=50)
    HouseEN = models.CharField(max_length=50)
    PersonEN = models.CharField(max_length=50)
    GrpQtrEn = models.CharField(max_length=50)
    AggSpUN = models.CharField(max_length=50)
    GeoAggSU = models.CharField(max_length=50)
    File = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.job_name


class JobFinal(models.Model):
    '''
      column_names:
       hid: hid  #Select Household ID Variable
       pid: pid	# Select Person ID Variable
       geo: geo #Select TAZ Variable
       region: region #Select County Variable
       sample_geo: sample_geo #Select Sample TAZ Variable
    '''
    ## to make COmposite Key
    class Meta:
        unique_together = (('user', 'job_name'),)

    document=user_directory_path

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    synthesize=models.BooleanField('Synthesize',help_text='',default=True)

    job_name = models.CharField(max_length=50,blank=False,null=False,help_text='e.g. Conneticut_Run',unique=True)
    project_name = models.CharField(max_length=50,help_text='e.g. Connecticut_Synthetic_Population')

    hid = models.CharField('Household Entity Name',max_length=50,help_text='e.g. hhld',default='hid')
    pid = models.CharField('Person Entity Name',max_length=50,help_text='e.g. person',default='pid')
    geo = models.CharField('Groupquaters Entity Name',max_length=50,help_text='',default='geo')
    region = models.CharField('Aggregate Spatial Unit',max_length=50,help_text='',default='region')
    sample_geo = models.CharField('Disaggregate Spatial Unit',max_length=50,help_text='',default='sample_geo')

    entities = models.CharField('Entities',max_length=500,help_text='e.g. [household, groupquarter, person]',default='[household, groupquarter, person]')
    housing_entities = models.CharField('Housing Entities', max_length=500, help_text='e.g. [household, groupquarter]',default='[household, groupquarter]')
    person_entities = models.CharField('Person Entity', max_length=500, help_text='e.g. [person]',default='[person]')

    #location

        #geo_corr_mapping
    geo_to_sample = models.FileField('geo to Sample',upload_to=document, blank=True, null=True,help_text='e.g. geo_sample_mapping.csv')
    region_to_sample = models.FileField('region to Sample',upload_to=document, blank=True, null=True,help_text='e.g. region_sample_mapping.csv')
    region_to_geo = models.FileField('region to Geo',upload_to=document, blank=True, null=True,help_text='e.g. region_geo_mapping.csv')
    #sample

    sample_household = models.FileField('Sample Household',upload_to=document, blank=True, null=True,help_text='e.g. household_sample.csv')
    sample_person = models.FileField('Sample Person',upload_to=document, blank=True, null=True,help_text='e.g. person_sample.csv')
    sample_groupquarter = models.FileField('Sample Groupquarter',upload_to=document, blank=True, null=True,help_text='e.g. groupquarters_sample.csv')

    geo_household_files = models.FileField('Geo Household Marginals', upload_to=document, blank=True, null=True,help_text='e.g. household_marginals.csv')
    geo_person_files = models.FileField('Geo Person Marginals', upload_to=document, blank=True, null=True,help_text='e.g. person_marginals.csv')
    geo_groupquarter_files = models.FileField('Geo Groupquarter Marginals', upload_to=document, blank=True, null=True,help_text='e.g. groupquarters_marginals.csv')

    region_household_files = models.FileField('Region Household Marginals', upload_to=document, blank=True, null=True,help_text='e.g. region_household_marginals.csv')
    region_person_files = models.FileField('Region Person Marginals', upload_to=document, blank=True, null=True,help_text='e.g. region_person_marginals.csv')
    region_groupquarter_files = models.FileField('Region Groupquarter Marginals', upload_to=document, blank=True, null=True,help_text='e.g. region_groupquarters_marginals.csv')
    #scenario

    desc= models.CharField('Scenario Description', max_length=50, help_text='e.g. Connecticut TAZ Scenario',default='Connecticut TAZ Scenario')
    arc=models.BooleanField('Scenario Apply Region Controls',default=True)
    #control_variables:
    #   region
    region_household= models.CharField('Control Variable Region Household', max_length=50, help_text='e.g.  [hhrtotals]',default='')
    region_groupquarter= models.CharField('Control Variable Region Groupquarter', max_length=50, help_text='e.g.  [gqrtotals]',default='')
    region_person= models.CharField('Control Variable Region Person', max_length=50, help_text='e.g.  [rpsex, rpage, rpworker, prtotals]',default='')
    #   geo
    geo_household= models.CharField('Control Variable Geo Household', max_length=50, help_text='e.g.  [hhtotals, hinc, hsize]',default='')
    geo_groupquarter= models.CharField('Control Variable Geo Groupquarter', max_length=50, help_text='e.g.  [gqtotals, gqtype]',default='')
    geo_person= models.CharField('Control Variable Geo Person', max_length=50, help_text='e.g.  [pworker, ptotals] ',default='')
    '''
        #Setting for IPF procedure, reweighting, and drawing household samples
        parameters:
         ipf:
          tolerance: 0.0001
          iterations: 250
          zero_marginal_correction: 0.00001
          rounding_procedure: bucket
          #What is the index '1' indicating? 1 hour or 1 min?
          archive_performance_frequency: 1 
        #Select either IPU or Entropy
         reweighting:
          procedure: ipu
          tolerance: 0.0001
          inner_iterations: 1
          outer_iterations: 50
          archive_performance_frequency: 1
         draws:
          pvalue_tolerance: 0.9999
          iterations: 25
          seed: 0
    '''
    ipf_tolerance=models.DecimalField('Parameters IPF Tolerance',max_digits=7,decimal_places=5,default=0.0001)
    iterations=models.IntegerField('Parameters IPF Iterations',default=1)
    zmc=models.DecimalField('Parameters IPF Zero Marginal Correction',max_digits=7,decimal_places=5,default=0.00001)
    RP_Opt = (
        ('bucket', 'Bucket'),)
    rp = models.CharField('Parameters IPF Rounding Procedure',max_length=50, choices=RP_Opt,  default='bucket')
    apf = models.IntegerField('Parameters IPF Archive Performance Frequency',default=1)

    #reweighting
    Proc_Opt = (
        ('ipu', 'IPU'),('entropy', 'Entropy'),)
    procedure = models.CharField('Parameters Reweighting Procedure',max_length=50, choices=Proc_Opt,  default='IPU')
    rew_tolerance=models.DecimalField('Parameters Reweighting Tolerance',max_digits=7,decimal_places=5,default= 0.0001)
    inner_iterations = models.IntegerField('Parameters Reweighting Inner Iterations',default=1)
    outer_iterations = models.IntegerField('Parameters Reweighting Outer Iterations',default=1000)
    rapf = models.IntegerField('Parameters Reweighting Archive Performance Frequency',default=1)
    # draws:
    pvalue_tolerance=models.DecimalField('Parameters Draws Pvalue Tolerance',max_digits=7,decimal_places=5,default=0.9999)
    draws_iterations = models.IntegerField('Parameters Draws Iterations',default=1)
    seed = models.IntegerField('Parameters Draws Seed',default=0)

    #geos_to_synthesize
        #region
    region_ids = models.CharField('Geos To Synthesize Region Ids',max_length=6000, help_text='e.g. [1,2,3,4,5,6,7,8,9,10,11,12,13,14]',default='[1,2,3]')
    region_all_ids=models.BooleanField('Geos To Synthesize Region All Ids',default=True)
        #geo
    geo_ids = models.CharField('Geos To Synthesize Geo Ids',max_length=6000, help_text='e.g. [1,2,3,4,5,6,7,8,9,10,11,12,13,14]',default='[1,2,3]')
    geo_all_ids=models.BooleanField('Geos To Synthesize Geo All Ids',default=True)

    performance= models.CharField('Output Performance',max_length=50, help_text='e.g. [ipf, reweighting, drawing]',default='[ipf, reweighting, drawing]')
    export=models.BooleanField('Output Weights Export',default=True)
    collate_across_geos=models.BooleanField('Output Weights Collate Across Geos',default=False)
    #multiway
    multiway_variables_one = models.CharField('Output Multiway Variables',max_length=50, help_text='e.g. [hsize, hinc]',default='[hsize, hinc]')
    filename_one = models.CharField('Output Filename',max_length=50, help_text='e.g. hhsize_income.csv',default='hhsize_income.csv')
    filetype_one = models.CharField('Output Filetype', max_length=50,help_text='e.g. csv',default='csv')
    entity_one = models.CharField('Output Entity',max_length=50, help_text='e.g. household or person',default='household')

    multiway_variables_two = models.CharField('Output Multiway Variables',max_length=50, help_text='e.g. [rpsex, rpage]',default='[rpsex, rpage]')
    filename_two = models.CharField('Output Filename',max_length=50, help_text='e.g. rpsex_rpage.csv',default='rpsex_rpage.csv')
    filetype_two = models.CharField('Output Filetype', max_length=50,help_text='e.g. csv',default='csv')
    entity_two = models.CharField('Output Entity',max_length=50, help_text='e.g. household or person',default='person')

    Job_Pushed=models.BooleanField('Submit/Save Job',help_text='Check this option if you want the system to run job now, If you just want to save the job keep it UnCheck',default=False)

    op_file_url=models.CharField(max_length=500,default='#')
    job_status_Opt = (
        ('Submitted', 'Submitted'),('Yaml-Error', 'Yaml-Error'), ('System-Error', 'System-Error'),('Completed', 'Completed'),('In-Progress', 'In-Progress'),)
    job_status=models.CharField('Job Status',max_length=30,choices=job_status_Opt,default='Submitted')
    job_create_time=models.DateField(auto_now_add=True)
    job_update_time=models.DateField(auto_now=True)


    def __str__(self):
        return self.job_name
