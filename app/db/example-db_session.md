# DB_SESSION EXAMPLE:

```
import db_session
from setup import *
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()

# Loading the env variables as a dict for easy parameter passing
    config = {
        "username": os.getenv("DB_USERNAME"),
        "password": os.getenv("DB_PASSWORD"),
        "host"    : os.getenv("DB_HOST"),
        "db"      : os.getenv("DB_NAME")
    };

    Session = db_session.session(setup,config)
    session = Session.create()
    
    john = Users(username="john",password="johnny",authLevel=1)
    print(john.id)
    
    session.add(john)
    session.commit()
    print(john.id)
    print(session.query(Users).filter_by(username="john").first().id)
    
    Session.close()
```

Output:
```
None  --> since instance john has not yet been committed to the db.
1     --> assuming this is the first to be committed.
1
```
