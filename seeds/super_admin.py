from flask_seeder import Seeder, Faker, generator
from users.auth_middleware import ADMIN_ROLE, USER_ROLE, roles_required,SUPERADMIN_ROLE,VENDOR, SALES
from database.database_models import Quote, QuoteInfo, UnitQuote, Enquiry,User
import bcrypt

class SuperAdminSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    # Create a new Faker and tell it how to create Category objects
    faker = Faker(
      cls=User,
      init={
        "first_name": 'Super',
        "last_name": 'admin',
        "email": 'superadmin3@3erp.com',
        "age": generator.Integer(start=20, end=100),
        "role_id":SUPERADMIN_ROLE,
        "password":'$2b$12$zMaf1M1t4VkonfP/AW8maOUSLoCqyGdam7JAbOgyadn5fzfEwkLpq',
        "status": 1,
      }
    )

    # Create 5 categories
    for user in faker.create(1):
      print("Adding superadmin: %s" % user)
      self.db.session.add(user)