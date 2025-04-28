# an object will provide the dependencies for another object
from abc import ABC, abstractmethod

class Database(ABC):            #define method save()
    @abstractmethod
    def save(self, data):
        pass
    
class MySQLDatabase(ABC):       #deploying 
    def save(self, data):
        print(f"Saving {data} to MySQL database")
        
class PostgreSQLDatabase(Database):        #deploying
    def save(self, data):
        print(f"Saving {data} to PostgreSQL database")
        
class UserService:      #get 1 object Database through contructor
    def __init__(self, database: Database):
        self.database = database
        
    def creat_user(self, user):
        self.database.save(user)
        
mysql_db = MySQLDatabase()
postgres_db = PostgreSQLDatabase()

user_service_mysql = UserService(mysql_db)
user_service_postgres = UserService(postgres_db)

user_service_mysql.creat_user("Alice")      #Saving Alice to MySQL database
user_service_postgres.creat_user("Bob")     #Saving Bob to PostgreSQL database