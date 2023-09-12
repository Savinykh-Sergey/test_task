from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, DateTime, update
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class DBHelper:
    def __init__(self, data_base_name: str):
        self.__engine = create_engine(f'sqlite:///{data_base_name}')
        self.__Session = sessionmaker(bind=self.__engine)
        self.__session = self.__Session()
        Base.metadata.create_all(self.__engine)

    def insert_info_user(self, user_id: str, user_name: str, user_surname: str, time: DateTime):
        user_info_obj = User(user_id=user_id, user_name=user_name, user_surname=user_surname, time=time)
        self.__session.add(user_info_obj)
        self.__session.commit()
        return user_info_obj.id
    
    def save_message(self, message: str, flag: bool = False):
        pass
    
    def get_message(self, message: str, flag: bool = False):
        pass
    
        
class MessagesData(Base):
    __tablename__ = 'messages_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_message = Column(String)
    character_message = Column(String)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    user_name = Column(String)
    user_surname = Column(String)
    time = Column(DateTime)

