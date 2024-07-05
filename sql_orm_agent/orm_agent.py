from sqlalchemy.orm import Session
from sqlalchemy import Table, MetaData
from orm_toolkit import SQLORMToolkit
from langchain.llms import OpenAI

class SQLORMAgent:
    def __init__(self, toolkit: SQLORMToolkit):
        self.toolkit = toolkit
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.toolkit.session_factory().bind)

    def run(self, command: str):
        session: Session = self.toolkit.session_factory()
        try:
            exec(command, globals(), locals())
            session.commit()
            return "Command executed successfully"
        except Exception as e:
            session.rollback()
            return str(e)
        finally:
            session.close()

# Initialize the SQL ORM toolkit and agent
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

llm = OpenAI(model="text-davinci-003")
orm_toolkit = SQLORMToolkit(session_factory=SessionLocal, llm=llm)
orm_agent = SQLORMAgent(toolkit=orm_toolkit)

# Example usage
result = orm_agent.run("""
from sqlalchemy import Table

# Reflect the table
employees_table = Table('employees', orm_agent.metadata, autoload_with=orm_agent.toolkit.session_factory().bind)

# Perform ORM operation
new_employee = {'name': 'mg mg', 'email': 'mgmg@gmail.com'}
insert = employees_table.insert().values(**new_employee)
session.execute(insert)
""")
print(result)
