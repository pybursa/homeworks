__author__ = "rm_ponomarenko"
__email__ = "ponomarenko.roman@gmail.com"
__date__ = "2014-11-21"

from datetime import datetime, date


class Person(object):
    """This class implements an entry in a phonebook for a person.

    Attributes:
      surname (str): Surname of a person in the phonebook.
      first_name (str): First name of a person in the phonebook.
      birth_date (date): Date of birth of a person in the phonebook.
      [optional] nickname (str): Nickname of a person in the phonebook.
    """

    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        try:
            self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        except:
            raise ValueError('Date of birth {0} is invalid. \
                Date must be in format YYYY-MM-DD.'.format(birth_date))
        if nickname is not None:
            self.nickname = nickname

    def get_age(self):
        """
        Returns the age of a person (completed years) as string value.
        """
        return str((date.today() - self.birth_date).days / 365)

    def get_fullname(self):
        """
        Returns a string that reflects the full name
        of a person(surname + first name).
        """
        return "{0} {1}".format(self.surname, self.first_name)
