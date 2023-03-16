from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import EmailAddress

class Controller:
    def __init__(self):
        self.engine = create_engine('sqlite:///emails.sqlite', echo=True)

    def save(self, type, addition):
        """
        Save the email
        :param email:
        :return:
        """
        if type == "name":
            try:
                with Session(self.engine) as sess:
                    name = EmailAddress(name=addition)
                    sess.add(name)
                    sess.commit()

            except ValueError as error:
                # show an error message
                raise ValueError(error)

        elif type == "email":
            try:
                with Session(self.engine) as sess:
                    email_address = EmailAddress(email=addition)
                    sess.add(email_address)
                    sess.commit()

            except ValueError as error:
                # show an error message
                raise ValueError(error)
        elif type == "password":
            try:
                with Session(self.engine) as sess:
                    password = EmailAddress(password=addition)
                    sess.add(password)
                    sess.commit()

            except ValueError as error:
                # show an error message
                raise ValueError(error)

    def delete(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:
            with Session(self.engine) as sess:
                sess.query(EmailAddress).filter(EmailAddress.email==email).delete()
                sess.commit()

        except ValueError as error:
            # show an error message
            raise ValueError(error)
