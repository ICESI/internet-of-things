import os

DEBUG=True

environment = os.getenv("OPENSHIFT_APP_NAME")
print(environment)

if environment != None:
	DB_HOST=os.getenv("OPENSHIFT_POSTGRESQL_DB_HOST"),
	DB_PORT=os.getenv("OPENSHIFT_POSTGRESQL_DB_PORT"),
	SQLALCHEMY_DATABASE_URI='postgresql://'+DB_HOST[0]+':'+DB_PORT[0]
	print(SQLALCHEMY_DATABASE_URI)
else:
	SQLALCHEMY_DATABASE_URI='sqlite:///app/database/lightcontrol.db'
	#SQLALCHEMY_DATABASE_URI='sqlite:///lightcontrol.db' 
	print(SQLALCHEMY_DATABASE_URI)

#C:\Users\DANIEL~1\Desktop\Git\