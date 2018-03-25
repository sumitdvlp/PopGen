#!/usr/bin/env python

import sys, os, django
sys.path.append("/path/to/store/home/sumit/Dropbox/PopGen") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PopGen.settings")
django.setup()
import yaml
import ruamel.yaml


from JobSchd.models import JobFinal,User
import yamlordereddictloader
from collections import OrderedDict

## we will extract the data from the submitted job and create Yaml configuration file , also make a package to serve to
## the backend

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


for j in AJ:
    #print j.Household_Sample_File
    Usv=str(j.user)
    #print Usv
    Usr=User.objects.filter(username=Usv)
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

    marginals_household=str(j.marginals_household).split("/")
    marginals_household=marginals_household[len(marginals_household) - 1]

    marginals_person=str(j.marginals_person).split("/")
    marginals_person=marginals_person[len(marginals_person) - 1]

    marginals_groupquarter=str(j.marginals_groupquarter).split("/")
    marginals_groupquarter=marginals_groupquarter[len(marginals_groupquarter) - 1]

    region_household=str(j.region_household).split("/")
    region_household=region_household[len(region_household) - 1]

    region_person=str(j.region_person).split("/")
    region_person=region_person[len(region_person) - 1]

    region_groupquarter=str(j.region_groupquarter).split("/")
    region_groupquarter=region_groupquarter[len(region_groupquarter) - 1]

    '''
    data=dict(
            project=dict(
                synthesize='True',
                name=j.job_name,
                location=loc,
                inputs=dict(
                    entities=j.entities,
                    housing_entities=j.housing_entities,
                    person_entities=j.person_entities,
                    column_names=dict(
                        hid=j.HouseEN,
                        pid=j.PersonEN,
                        geo=j.GeoAggSU,
                        region=j.AggSpUN,
                        sample_geo=j.SmplSpatialUn
                    ),
                    location=dict(
                        geo_corr_mapping=dict(
                            geo_to_sample=geo_to_sample,

                        )
                    )
                )
            )
    )
    '''

    code = ruamel.yaml.load(inp, ruamel.yaml.RoundTripLoader)
    code['project']['synthesize'] = 'True'
    code['project']['name'] = j.job_name
    code['project']['location'] = loc
    code['project']['inputs']['entities'] = j.entities
    code['project']['inputs']['housing_entities'] = j.housing_entities
    code['project']['inputs']['person_entities'] = j.housing_entities
    code['project']['inputs']['column_names']['sample_geo'] = j.SmplSpatialUn
    code['project']['inputs']['column_names']['hid'] = j.HouseEN
    code['project']['inputs']['column_names']['pid'] = j.PersonEN
    code['project']['inputs']['column_names']['geo'] = j.GeoAggSU
    code['project']['inputs']['column_names']['region'] = j.AggSpUN
    code['project']['inputs']['column_names']['sample_geo'] = j.SmplSpatialUn
    code['project']['inputs']['location']['geo_corr_mapping']['geo_to_sample'] = geo_to_sample
    code['project']['inputs']['location']['geo_corr_mapping']['region_to_sample'] = region_to_sample
    code['project']['inputs']['location']['geo_corr_mapping']['region_to_geo'] = region_to_geo
    code['project']['inputs']['location']['sample']['household'] = sample_household
    code['project']['inputs']['location']['sample']['person'] = sample_person
    code['project']['inputs']['location']['sample']['groupquarter'] = sample_groupquarter
    '''
    code['project']['inputs']['location']['marginals']['geo'] =
    code['project']['inputs']['location']['geo_corr_mapping']
    code['project']['inputs']['location']['geo_corr_mapping']
    code['project']['inputs']['location']['geo_corr_mapping']
    code['project']['inputs']['location']['geo_corr_mapping']
    '''

    file_name='configuration'+str(j.job_name)+'.yml'
    file_object  = open(file_name,"w")
    ruamel.yaml.dump(code, file_object, Dumper=ruamel.yaml.RoundTripDumper)

    file_object.close()



