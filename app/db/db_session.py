from sqlalchemy.orm import sessionmaker

class session:

    def __init__(self,setup,config):
        Setup = setup(config["username"], config["password"], config["host"],config["db"])
        self.engine = Setup.create()

    def create(self):
        session = sessionmaker(bind=self.engine)
        self.Session = session()
        return session()
    
    def close(self):
        self.Session.close()
