
  # <span style='color:yellow'>SIMPLE API</span>📝  
  
  ## Get Started 🚀  
  It's a simple API that create a username and email and then insert it into PostgreSQL database.

  
  ## Prebuilt Components/Templates 🔥  
 This API uses FastAPI and Docker.
      
  ## Save Readme ✨  

  - **.env**   #confidential information
  - **core**  
          - *config.py*  #setting, app_name, database url from .env
  - **db**  
          - *base.py*  
          - *session.py*  #declaration base, ORM
  - **models**  
          - *user.py*    #create table user in database
  - **schemas**  
          - *user.py*    #CreateUser in BaseModel and UserResponse in API (localhost:8000)
  - **services**  
          - *user_service.py*    #Create table and insert user into db
  - **api/v1**  
          - *users.py*       #Router creater user
  - **requirements.txt**
  - **Dockerfile**
  - **docker-compose.yml**
  - **main.py**
  - **README.md**
