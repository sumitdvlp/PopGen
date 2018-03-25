#!/usr/bin/env python

import PopGen

import sys, os, django
#sys.path.append("/path/to/store/home/sumit/Dropbox/PopGen") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PopGen.settings")
django.setup()
#import yaml
import ruamel.yaml
from subprocess import call

import move_package
from JobSchd.models import JobFinal
from django.contrib.auth.models import User
#import yamlordereddictloader
from collections import OrderedDict
#from decimal import *
from ruamel.yaml.error import *  # NOQA
from ruamel.yaml.representer import RoundTripRepresenter, SafeRepresenter
import os,datetime


## we will extract the data from the submitted job and create Yaml configuration file , also make a package to serve to
## the backend

def run():
    count = JobFinal.objects.all().count()

    #AJ=JobFinal.objects.filter(job_name__contains='Vishal')
    AJ=JobFinal.objects.all()



    inp="""\
    project:
    #To generate a synthetic population
     synthesize: True 
     name: NewJersey_Synthetic_Population
    #File location
     location: New_Jersey/
    #Setup input data with given forms
     inputs:
      entities: [household, groupquarter, person]
      housing_entities: [household, groupquarter]
      person_entities: [person]
      column_names:
       hid: hid
       pid: pid
       geo: geo
       region: region
       sample_geo: sample_geo
      location:
       geo_corr_mapping:
        geo_to_sample: geo_sample_mapping.csv
        region_to_sample: region_sample_mapping.csv
        region_to_geo: region_geo_mapping.csv
       sample:
        household: household_sample.csv
        person: person_sample.csv
        groupquarter: groupquarters_sample.csv
       marginals:
        geo:
         household: household_marginals.csv
         person: person_marginals.csv
         groupquarter: groupquarters_marginals.csv
        region:
         household: region_household_marginals.csv
         person: region_person_marginals.csv
         groupquarter: region_groupquarters_marginals.csv
    #Start to provide scenario
     scenario:
    #Brief description
      - description: NewJersey TAZ Scenario
    #If control variables are applied in multi-environment (geo and region), true
        apply_region_controls: True
    #Based on input setting, write down header name for each value
        control_variables:
         region:
          household: [hhrtotals]
          groupquarter: [gqrtotals]
          person: [rpsex, rpage, rpworker, prtotals]
         geo:
          household: [hhtotals, hinc, hsize]
          groupquarter: [gqtotals, gqtype]
          person: [pworker, ptotals]
    #Setting for IPF procedure, reweighting, and drawing household samples
        parameters:
         ipf:
          tolerance: 0.0001
          iterations: 250
          zero_marginal_correction: 0.00001
          rounding_procedure: bucket
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
    
        geos_to_synthesize:
         region:
         #Leave empty blank if we synthesize specific region, then use ID
          ids: [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
          all_ids: True
         geo:
          ids: []
          all_ids: True
    
        outputs:
         performance: [ipf, reweighting, drawing]
         weights:
          export: True
          collate_across_geos: False
         multiway:
          - variables: [hsize, hinc]
            filename: hhsize_income.csv
            filetype: csv
            entity: household
          - variables: [rpsex, rpage]
            filename: rpsex_rpage.csv
            filetype: csv
            entity: person
    
         summary:
          region:
           filename: summary_region.csv
           filetype: csv
          geo:
           filename: summary_geo.csv
           filetype: csv
         synthetic_population:
          housing:
           filename: housing_synthetic.csv
           filetype: csv
          person:
           filename: person_synthetic.csv
           filetype: csv
    """

    #fileOb = open('configuration.yaml', 'r')
	
    #inp = file.read(fileOb)


    for j in AJ:
        if(j.Job_Pushed==True):
            #print j.Household_Sample_File
            Usv=str(j.user)
            #print Usv
            Usr=User.objects.filter(username=Usv)
            email=Usr[0].email
            #print email
            loc = 'home/sumit/Desktop/Popgen-processing/ready/'+str(j.job_name)

            geo_to_sample=str(j.geo_to_sample).split("/")
            geo_to_sample=geo_to_sample[len(geo_to_sample) - 1]

            region_to_sample=str(j.region_to_sample).split("/")
            region_to_sample=region_to_sample[len(region_to_sample) - 1]

            region_to_geo=str(j.region_to_geo).split("/")
            region_to_geo=region_to_geo[len(region_to_geo) - 1]

            sample_household=str(j.sample_household).split("/")
            sample_household=sample_household[len(sample_household) - 1]

            sample_person=str(j.sample_person).split("/")
            sample_person=sample_person[len(sample_person) - 1]

            sample_groupquarter=str(j.sample_groupquarter).split("/")
            sample_groupquarter=sample_groupquarter[len(sample_groupquarter) - 1]

            geo_household_files=str(j.geo_household_files).split("/")
            geo_household_files=geo_household_files[len(geo_household_files) - 1]

            geo_person_files=str(j.geo_person_files).split("/")
            geo_person_files=geo_person_files[len(geo_person_files) - 1]

            geo_groupquarter_files=str(j.geo_groupquarter_files).split("/")
            geo_groupquarter_files=geo_groupquarter_files[len(geo_groupquarter_files) - 1]

            region_household_files=str(j.region_household_files).split("/")
            region_household_files=region_household_files[len(region_household_files) - 1]

            region_person_files=str(j.region_person_files).split("/")
            region_person_files=region_person_files[len(region_person_files) - 1]

            region_groupquarter_files=str(j.region_groupquarter_files).split("/")
            region_groupquarter_files=region_groupquarter_files[len(region_groupquarter_files) - 1]

            code = ruamel.yaml.load(inp, ruamel.yaml.RoundTripLoader)


            code['project']['synthesize'] = True
            code['project']['name'] = j.job_name
            code['project']['location'] = loc
            code['project']['inputs']['entities'] = j.entities
            code['project']['inputs']['housing_entities'] = j.housing_entities
            code['project']['inputs']['person_entities'] = j.person_entities

            code['project']['inputs']['column_names']['hid'] = j.hid
            code['project']['inputs']['column_names']['pid'] = j.pid
            code['project']['inputs']['column_names']['geo'] = j.geo
            code['project']['inputs']['column_names']['region'] = j.region
            code['project']['inputs']['column_names']['sample_geo'] = j.sample_geo

            code['project']['inputs']['location']['geo_corr_mapping']['geo_to_sample'] = geo_to_sample
            code['project']['inputs']['location']['geo_corr_mapping']['region_to_sample'] = region_to_sample
            code['project']['inputs']['location']['geo_corr_mapping']['region_to_geo'] = region_to_geo
            code['project']['inputs']['location']['sample']['household'] = sample_household
            code['project']['inputs']['location']['sample']['person'] = sample_person
            code['project']['inputs']['location']['sample']['groupquarter'] = sample_groupquarter

            code['project']['inputs']['location']['marginals']['geo']['household'] = geo_household_files
            code['project']['inputs']['location']['marginals']['geo']['person'] = geo_person_files
            code['project']['inputs']['location']['marginals']['geo']['groupquarter'] = geo_groupquarter_files

            code['project']['inputs']['location']['marginals']['region']['household'] = region_household_files
            code['project']['inputs']['location']['marginals']['region']['person'] = region_person_files
            code['project']['inputs']['location']['marginals']['region']['groupquarter'] = region_groupquarter_files

            code['project']['scenario'][0]['description'] = j.desc
            code['project']['scenario'][0]['apply_region_controls'] = j.arc
            code['project']['scenario'][0]['control_variables']['region']['household'] =j.region_household
            code['project']['scenario'][0]['control_variables']['region']['groupquarter'] = j.region_groupquarter
            code['project']['scenario'][0]['control_variables']['region']['person'] = j.region_person

            code['project']['scenario'][0]['control_variables']['geo']['household'] =j.geo_household
            code['project']['scenario'][0]['control_variables']['geo']['groupquarter'] = j.geo_groupquarter
            code['project']['scenario'][0]['control_variables']['geo']['person'] = j.geo_person


            # we have to convert decimal to float
	    ## for all float we have to convert them using format as by default it was converting 0.00001 to 1e-05
            #print type(float(j.ipf_tolerance))
	    f=float(j.ipf_tolerance)
	   
            code['project']['scenario'][0]['parameters']['ipf']['tolerance'] = '{:f}'.format(f).rstrip('0')
            code['project']['scenario'][0]['parameters']['ipf']['iterations'] = j.iterations

            #print type(j.zmc)
	    f=float(j.zmc)
            code['project']['scenario'][0]['parameters']['ipf']['zero_marginal_correction'] = '{:f}'.format(f).rstrip('0')
            code['project']['scenario'][0]['parameters']['ipf']['rounding_procedure'] = j.rp
            code['project']['scenario'][0]['parameters']['ipf']['archive_performance_frequency'] = j.apf

            code['project']['scenario'][0]['parameters']['reweighting']['procedure'] = j.procedure
            #print type(j.rew_tolerance)
	    # '{:f}'.format(f).rstrip('0')
	    f = float(j.rew_tolerance)
            code['project']['scenario'][0]['parameters']['reweighting']['tolerance'] = '{:f}'.format(f).rstrip('0')
            code['project']['scenario'][0]['parameters']['reweighting']['inner_iterations'] = j.inner_iterations
            code['project']['scenario'][0]['parameters']['reweighting']['outer_iterations'] = j.outer_iterations
            code['project']['scenario'][0]['parameters']['reweighting']['archive_performance_frequency'] = j.rapf

            #print type(j.pvalue_tolerance)
	    f = float(j.pvalue_tolerance)
            code['project']['scenario'][0]['parameters']['draws']['pvalue_tolerance'] = '{:f}'.format(f).rstrip('0')
            code['project']['scenario'][0]['parameters']['draws']['iterations'] = j.draws_iterations
            code['project']['scenario'][0]['parameters']['draws']['seed'] = j.seed

            code['project']['scenario'][0]['geos_to_synthesize']['region']['ids'] = j.region_ids
            code['project']['scenario'][0]['geos_to_synthesize']['region']['all_ids'] = j.region_all_ids

            code['project']['scenario'][0]['geos_to_synthesize']['geo']['ids'] = j.geo_ids
            code['project']['scenario'][0]['geos_to_synthesize']['geo']['all_ids'] = j.geo_all_ids

            code['project']['scenario'][0]['outputs']['performance'] = j.performance

            code['project']['scenario'][0]['outputs']['weights']['export'] = j.export
            code['project']['scenario'][0]['outputs']['weights']['collate_across_geos'] = j.collate_across_geos
            ## had to add index for the ' - ' in the file, kind of how dictionary works here
            code['project']['scenario'][0]['outputs']['multiway'][0]['variables'] = j.multiway_variables_one
            code['project']['scenario'][0]['outputs']['multiway'][0]['filename'] = j.filename_one
            code['project']['scenario'][0]['outputs']['multiway'][0]['filetype'] = j.filetype_one
            code['project']['scenario'][0]['outputs']['multiway'][0]['entity'] = j.entity_one

            code['project']['scenario'][0]['outputs']['multiway'][1]['variables'] = j.multiway_variables_two
            code['project']['scenario'][0]['outputs']['multiway'][1]['filename'] = j.filename_two
            code['project']['scenario'][0]['outputs']['multiway'][1]['filetype'] = j.filetype_two
            code['project']['scenario'][0]['outputs']['multiway'][1]['entity'] = j.entity_two

            j.Job_Pushed = False
            j.save()

            #print code
            #print code['project']['scenario']['description']
            #print code['project']['scenario']['outputs']['performance']

            #print code['project']['scenario'][0]['outputs']['multiway'][1]['variables']
            #print code['project']['scenario'][0]['description']

            #SafeRepresenter.add_representer(float)

            #RoundTripRepresenter.add_representer(float,RoundTripRepresenter.represent_none)
            ## get the name of the user and job-name for/from the directory structures
            geo_to_sample = str(j.geo_to_sample).split("/")
            usname = geo_to_sample[0]
            jbname=geo_to_sample[1]
            ## getting current working directory of the current directory ,as the file ares stored in the files folder
            ## we need to get to do something awesome

            #print os.getcwd()
            #abs_path=os.getcwd()
            ##abs_path=abs_path.replace('scripts','file')
            #print 'abs_path',abs_path
            #print 'j.geo_to_sample',j.geo_to_sample

            ## :( i am hardcoding the path for now
            file_name='/home/ubuntu/django_env/PopGen/file'+'/'+str(usname)+'/'+str(jbname)+'/'+'#'+email+'#'+str(j.id)+'#'+'configuration_'+str(j.job_name)+'.yaml'
            package_dir='/home/ubuntu/django_env/PopGen/file'+'/'+str(usname)+'/'+str(jbname)

            #print 'package_dir',package_dir,'\n'
            #print 'file_name',file_name
            file_object  = open(file_name,"w")
            r=ruamel.yaml.RoundTripRepresenter
            ruamel.yaml.dump(code, file_object, Dumper=ruamel.yaml.RoundTripDumper)
            #print file_name
            file_object.close()
	    fmt = '%Y-%m-%d-%H-%M-%S'
            timestamp= datetime.datetime.now().strftime(fmt)


            cmnd='sed -i \'s/\'\\\'\'/\'\'/g\' '+str(file_name)
            print 'cmnd',cmnd,' at Time ',timestamp
            call(cmnd,shell=True)

            move_package.zip(package_dir)


