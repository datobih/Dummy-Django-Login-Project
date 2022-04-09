import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_login_project.settings')

import django
django.setup()

from django.contrib.auth.models import User
from my_login_app.models import UserProfile

def migrate_user(pos):
    user=User.objects.all()[pos]


    userProfile=UserProfile()
    userProfile.user=user
    userProfile.save()


if __name__=='__main__':
    print("Migrating")
    migrate_user(1)
    print("Migrated")