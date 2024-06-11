from flask_seeder import Seeder, Faker, generator
from database.database_models import Quote, QuoteInfo, UnitQuote, Enquiry,User,Department


class DepartmentSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    # Create a new Faker and tell it how to create Category objects
    faker = Faker(
      cls=Department,
      init=
            {
                "name": 'sales',
            }
        
    )

    # Create 5 categories
    for department in faker.create(1):
      print("Adding department: %s" % department)
      self.db.session.add(department)