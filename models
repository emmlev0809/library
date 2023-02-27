from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# Base is called an Abstract Base Class - our SQL Alchemy models will inherit from this class
Base = declarative_base()

# Sets up a link table with activity_id and person_id as foreign keys
# Base.metadata is a container object that keeps together many different features of the database
book_author = Table('book_author',
                        Base.metadata,
                        Column('id', Integer, primary_key=True),
                        Column('author_id', ForeignKey('author.id')),
                        Column('publisher_id', ForeignKey('publisher.id')),
                        UniqueConstraint('author_id', 'publisher_id')
                        )


# Sets up an Activity table, this references "attendees" via the person_activities table
class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    ISBN_number = Column(Integer, unique=True, nullable=False)
    num_pages = Column(Integer, nullable=False)
    publication_date = Column(Integer, nullable=False)
    publication_id = Column(Integer, ForeignKey("publisher.id"), default=None)

    author = relationship("Author",
                             secondary=book_author,
                             order_by='(Author.name)',
                             back_populates="books")

    # Gives a representation of an Activity (for printing out)
    def __repr__(self):
        return f"<Book({self.name})>"


# Sets up a Person table, this references "activities" via the person_activities table
class Author(Base):
    __tablename__ = 'author'
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String, nullable=False)
    book = relationship("Book",
                              secondary=book_author,
                              order_by='Book.title',
                              back_populates="book")

    # Gives a representation of a Person (for printing out)
    def __repr__(self):
        return f"<Author({self.author_name})>"




# Sets up a Location table, this references "activities" via the person_activities table
class Publisher(Base):
    __tablename__ = 'publisher'
    publisher_id = Column(Integer, primary_key=True, autoincrement=True)
    publisher_name = Column(String, nullable=False)


    # Gives a representation of a Person (for printing out)
    def __repr__(self):
        return f"<Publisher({self.name})>"
