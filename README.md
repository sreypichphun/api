## <span style='color:yellow'>API</span>


- .env   #confidential information
- core 
         - config.py  #setting, app_name, database url from .env
- db
         - base.py
         - session.py  #declaration base, ORM
- models
         - user.py    #create table user in database
- schemas
         - user.py    #CreateUser in BaseModel and UserResponse in API (localhost:8000)
- services
         - user_service.py    #Create table and insert user into db
- api/v1
         - users.py       #Router creater user
- requirements.txt
- Dockerfile
- docker-compose.yml
- main.py
- README.md
