from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

"""
When using the ORM, the configurational process starts by describing the database tables 
we’ll be dealing with, and then by defining our own classes which will be mapped to those 
tables. In modern SQLAlchemy, these two tasks are usually performed together, using 
a system known as Declarative, which allows us to create classes that include directives 
to describe the actual database table they will be mapped to.
"""
Base = declarative_base()

class Puppy(Base):
	#table name is definitely required
    __tablename__ = 'puppy'
    #te other fields of the object
    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    #Add add a decorator property to serialize data from the database
    @property
    def serialize(self):
    	#serialize the object
    	return {
    	'id':self.id,
    	'name':self.name,
    	'description':self.description
    	}


#in memory sqlite db
#to connect we use create_engine()

engine = create_engine('sqlite:///puppies.db')

#now this will create the all the schemas in the DB
#i think
"""
The Table object is a member of a larger collection known as MetaData. When using Declarative, 
this object is available using the .metadata attribute of our declarative base class.

The MetaData is a registry which includes the ability to emit a limited set of schema 
generation commands to the database. As our SQLite database does not actually have a 
users table present, we can use MetaData to issue CREATE TABLE statements to the database for
all tables that don’t yet exist. Below, we call the MetaData.create_all() method, passing in 
our Engine as a source of database connectivity. 
"""
Base.metadata.create_all(engine)
