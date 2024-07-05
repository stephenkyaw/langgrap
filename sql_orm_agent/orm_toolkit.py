from typing import List
from sqlalchemy.orm import sessionmaker
from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import BaseToolkit
from langchain_community.tools import BaseTool

class SQLORMToolkit(BaseToolkit):
    """Toolkit for interacting with SQL databases using SQLAlchemy ORM dynamically.

    Parameters:
        session_factory: A session factory for SQLAlchemy ORM.
        llm: BaseLanguageModel. The language model.
    """

    session_factory: sessionmaker
    llm: BaseLanguageModel

    class Config:
        arbitrary_types_allowed = True

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        # Define your ORM tools here, such as CRUD operations dynamically
        return []
