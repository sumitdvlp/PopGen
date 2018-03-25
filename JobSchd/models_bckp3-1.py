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

    job_name = models.CharField(max_length=50,blank=False,null=False,help_text='Eg. Connecticut_Run',unique=True)
    project_name = models.CharField(max_length=50,help_text='Eg. Connecticut_Synthetic_Population')

    hid = models.CharField('Household Entity Name',max_length=50,help_text='Eg. hhld',default='hid')
    pid = models.CharField('Person Entity Name',max_length=50,help_text='Eg. person',default='pid')
    geo = models.CharField('Groupquarter Entity Name',max_length=50,help_text='For TAZ Eg. geo',default='geo')
    region = models.CharField('Aggregate Spatial Unit',max_length=50,help_text='For County Eg. region',default='region')
    sample_geo = models.CharField('Disaggregate Spatial Unit',max_length=50,help_text='For TAZ Eg. sample_geo',default='sample_geo')

    '''
     inputs:
      entities: [household, groupquarter, person] ## Add as a list
      housing_entities: [household, groupquarter] # Add as a list
      person_entities: [person] # Add as a list
    '''
    entities = models.CharField('Entities',max_length=500,help_text='Eg. [household, groupquarter, person]',default='[household, groupquarter, person]')
    housing_entities = models.CharField('Housing Entities', max_length=500, help_text='Eg. [household, groupquarter]',default='[household, groupquarter]')
    person_entities = models.CharField('Person Entities', max_length=500, help_text='Eg. [person]',default='[person]')

    #location

        #geo_corr_mapping
    geo_to_sample = models.FileField('geo to Sample File',upload_to=document, blank=True, null=True,help_text='geo_sample_mapping.csv')
    region_to_sample = models.FileField('region to Sample File',upload_to=document, blank=True, null=True,help_text='region_sample_mapping.csv')
    region_to_geo = models.FileField('region to Geo File',upload_to=document, blank=True, null=True,help_text='region_geo_mapping.csv')
    #sample

    sample_household = models.FileField('Sample Household File',upload_to=document, blank=True, null=True,help_text='household_sample.csv')
    sample_person = models.FileField('Sample Person File',upload_to=document, blank=True, null=True,help_text='person_sample.csv')
    sample_groupquarter = models.FileField('Sample Groupquarter File',upload_to=document, blank=True, null=True,help_text='groupquarters_sample.csv')

    geo_household_files = models.FileField('Geo Household File', upload_to=document, blank=True, null=True,help_text='household_marginals.csv')
    geo_person_files = models.FileField('Geo Person File', upload_to=document, blank=True, null=True,help_text='person_marginals.csv')
    geo_groupquarter_files = models.FileField('Geo Groupquarter File', upload_to=document, blank=True, null=True,help_text='groupquarters_marginals.csv')

    region_household_files = models.FileField('Region Household File', upload_to=document, blank=True, null=True,help_text='region_household_marginals.csv')
    region_person_files = models.FileField('Region Person File', upload_to=document, blank=True, null=True,help_text='region_person_marginals.csv')
    region_groupquarter_files = models.FileField('Region Groupquarter File', upload_to=document, blank=True, null=True,help_text='region_groupquarters_marginals.csv')
    #scenario

    desc= models.CharField('Scenario Description', max_length=50, help_text='For Eg. Connecticut TAZ Scenario',default='Connecticut TAZ Scenario')
    arc=models.BooleanField('Apply Region Controls',default=True)
    #control_variables:
    #   region
    region_household= models.CharField('Region Household', max_length=50, help_text='For eg. [hhrtotals]',default='')
    region_groupquarter= models.CharField('Region Groupquarter', max_length=50, help_text='For eg. [gqrtotals]',default='')
    region_person= models.CharField('Region Person', max_length=50, help_text='For eg. [rpsex, rpage, rpworker, prtotals]',default='')
    #   geo
    geo_household= models.CharField('Geo Household', max_length=50, help_text='For eg. [hhtotals, hinc, hsize]',default='')
    geo_groupquarter= models.CharField('Geo Groupquarter', max_length=50, help_text='For eg. [gqtotals, gqtype]',default='')
    geo_person= models.CharField('Geo Person', max_length=50, help_text='For eg. [pworker, ptotals] ',default='')
    '''
    '''
    ipf_tolerance=models.DecimalField('Tolerance',max_digits=7,decimal_places=5,default=0.0001)
    iterations=models.IntegerField('Iterations',default=1)
    zmc=models.DecimalField('Zero Marginal Correction',max_digits=7,decimal_places=5,default=0.00001)
    RP_Opt = (
        ('bucket', 'Bucket'),)
    rp = models.CharField('Rounding Procedure',max_length=50, choices=RP_Opt,  default='bucket')
    apf = models.IntegerField('Archive Performance Frequency',default=1)

    #reweighting
    Proc_Opt = (
        ('ipu', 'IPU'),('entropy', 'Entropy'),)
    procedure = models.CharField('Procedure',max_length=50, choices=Proc_Opt,  default='ipu')
    rew_tolerance=models.DecimalField('Tolerance',max_digits=7,decimal_places=5,default= 0.0001)
    inner_iterations = models.IntegerField('Inner Iterations',default=1)
    outer_iterations = models.IntegerField('Outer Iterations',default=1000)
    rapf = models.IntegerField('Archive Performance Frequency',default=1)
    # draws:
    pvalue_tolerance=models.DecimalField('Pvalue Tolerance',max_digits=7,decimal_places=5,default=0.9999)
    draws_iterations = models.IntegerField('Iterations',default=1)
    seed = models.IntegerField('Seed',default=0)

    #geos_to_synthesize
        #region
    region_ids = models.CharField('Region Ids',max_length=6000, help_text='For Eg. [1,2,3,4,5,6,7,8,9,10,11,12,13,14]',default='[1,2,3]')
    region_all_ids=models.BooleanField('Region All Ids',default=True)
        #geo
    geo_ids = models.CharField('Geo Ids',max_length=6000, help_text='For Eg. [1,2,3,4,5,6,7,8,9,10,11,12,13,14]',default='[1,2,3]')
    geo_all_ids=models.BooleanField('Geo All Ids',default=True)

    performance= models.CharField('Performance',max_length=50, help_text='For Eg.[ipf, reweighting, drawing]',default='[ipf, reweighting, drawing]')
    export=models.BooleanField('Export',default=True)
    collate_across_geos=models.BooleanField('Collate Across Geos',default=False)
    #multiway
    multiway_variables_one = models.CharField('Multiway Variables',max_length=50, help_text='For Eg. [hsize, hinc]',default='[hsize, hinc]')
    filename_one = models.CharField('Filename',max_length=50, help_text='Eg. hhsize_income.csv',default='hhsize_income.csv')
    filetype_one = models.CharField('Filetype', max_length=50,help_text='Eg. csv',default='csv')
    entity_one = models.CharField('Entity',max_length=50, help_text='Eg. household or person',default='household')

    multiway_variables_two = models.CharField('Multiway Variables',max_length=50, help_text='For Eg. [hsize, hinc]',default='[hsize, hinc]')
    filename_two = models.CharField('Filename',max_length=50, help_text='For Eg. hhsize_income.csv',default='hhsize_income.csv')
    filetype_two = models.CharField('Filetype', max_length=50,help_text='For Eg. csv',default='csv')
    entity_two = models.CharField('Entity',max_length=50, help_text='For Eg. household or person',default='person')

    #Job_Pushed = models.CharField('Multiway Variables',max_length=50, help_text='[hsize, hinc]',default='[hsize, hinc]')
    #filename_three = models.CharField('Filename',max_length=50, help_text='hhsize_income.csv',default='hhsize_income.csv')
    #filetype_three = models.CharField('Filetype', max_length=50,help_text='csv',default='csv')
    #entity_three = models.CharField('Entity',max_length=50, help_text='household or person',default='person')

    Job_Pushed=models.BooleanField(' Check this option If you want to Process this New/Updated Job Now or Uncheck if you want save the data and want to run it later',help_text='Your updated/submited Job will be Processed by our system only if you check this option',default=True)

    def __str__(self):
        return self.job_name
