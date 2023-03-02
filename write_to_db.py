from sqlalchemy import create_engine
from models import Book, Author, Publisher
from sqlalchemy.orm import Session
import random
import datetime

publishers = [Publisher(publisher_name="Macmillan"),
              Publisher(publisher_name="Simon & Schuster"),
              Publisher(publisher_name="Penguin"),
              Publisher(publisher_name="Harper Collins")]

authors = [Author(author_name="Jane Eyre"),
           Author(author_name="Sally Rooney"),
           Author(author_name="John Grey"),
           Author(author_name="Chris Pappel")]

books = [Book(title="Pride and Prejudice",
              isbn="".join([str(random.randint(0, 9)) for _ in range(13)]),
              num_pages=279,
              publication_date=datetime.date(1813, 2, 23),
              ),
         Book(title="Normal People",
              isbn="".join([str(random.randint(0, 9)) for _ in range(13)]),
              num_pages=266,
              publication_date=datetime.date(2018, 5, 12),
              ),
         Book(title="History of Concrete",
              isbn="".join([str(random.randint(0, 9)) for _ in range(13)]),
              num_pages=912,
              publication_date=datetime.date(1987, 10, 10),
              ),
         Book(title="The Man Who Was a Mango",
              isbn="".join([str(random.randint(0, 9)) for _ in range(13)]),
              num_pages=142,
              publication_date=datetime.date(2022, 2, 12),
              ),
         Book(title="The Woman Who Was a Pear",
              isbn="".join([str(random.randint(0, 9)) for _ in range(13)]),
              num_pages=143,
              publication_date=datetime.date(2022, 2, 13),
              publisher_id=2),
         ]

books[0].authors.append(authors[0])
books[0].publisher = publishers[0]
books[1].authors.append(authors[1])
books[1].publisher = publishers[1]
books[2].authors.append(authors[2])
books[2].authors.append(authors[3])
books[2].publisher = publishers[0]
books[3].authors.append(authors[3])
books[3].publisher = publishers[2]
books[4].authors.append(authors[3])
books[4].publisher = publishers[3]


books[0].publisher = publishers[0]

engine = create_engine('sqlite:///library.sqlite', echo=True)

with Session(engine) as sess:
    sess.add_all(books)
    sess.commit()
