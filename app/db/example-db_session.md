# DB_SESSION EXAMPLE:

```
import db_session
from setup import *

if __name__ == "__main__":

    Session = db_session.session(setup)
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
