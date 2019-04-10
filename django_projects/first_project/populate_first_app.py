import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

##Fake information generating script
import random
from first_app.models import AccessRecord,Webpage,Topic,Users
from faker import Faker

fakegen = Faker()

topics =['Search','Social','Markertplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top =add_topic()
        #create the fake date for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()


        #create the new webpasge entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name =fake_name)[0]
        #create the new AccessRecord entry
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

def populate_name(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email =fakegen.email()
        user = Users.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]


if __name__=='__main__':
    print("populating database!")
    populate_name(20)
    #populate(20)
    print("populating complete")
