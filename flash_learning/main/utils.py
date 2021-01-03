import re

from wtforms.validators import ValidationError


def check_password(form, field) -> None:
    """
    Check entered password against minimum password requirements.

    :param form: The registration form.
    :param field: Data from the form.
    """

    # Password must be at least four characters long.
    if len(field.data) < 8:
        raise ValidationError('Password must greater than 4 character')

    # Password cannot have a sequence of increasing numbers.
    if re.search("[0-9]", field.data) is not None:
        length = len(field.data)
        index = 0
        count = 1

        while index < length - 1:
            num1 = field.data[index]

            # convert to int
            if 47 < ord(num1) < 58:
                num1 = int(num1)
            num2 = field.data[index + 1]

            if 47 < ord(num2) < 58:
                num2 = int(num2)
            index = index + 1

            # check if conversation successful
            if type(num1) != int or type(num2) != int:
                count = 1
                continue

            # check if incrementing
            if num1 + 1 == num2 or num1 == num2:
                count += count
            else:
                count = 1

            if count == 3:
                raise ValidationError("Password can't have 123;456 or other single-incrementing numbers")

    # TODO: What does this do?
    if re.search("password", field.data, re.IGNORECASE) is not None and \
            re.search("password", field.data, re.IGNORECASE).start() == 0:
        raise ValidationError('Password can not start with the word Password[case-insensitive]')

    # Password must contain at least one letter.
    if len(re.findall("[A-Z]", field.data, re.IGNORECASE)) == 0:
        raise ValidationError('Password must contain at least 1 letter')

    # Password must contain at least one number.
    if len(re.findall("[0-9]", field.data)) == 0:
        raise ValidationError('Password must contain at least 1 number')

    # Password must contain at least one symbol.
    if (len(re.findall("[A-Z]", field.data, re.IGNORECASE)) + len(re.findall("[0-9]", field.data))) == len(field.data):
        raise ValidationError('Password must contain at least 1 symbol')

    # Password cannot contain the user's username.
    if re.search(form.username.data, field.data, re.IGNORECASE) is not None:
        raise ValidationError("Password Can Not Contain User Name")

    # Password cannot contain the user's first name.
    if re.search(form.first_name.data, field.data, re.IGNORECASE) is not None:
        raise ValidationError("Password Can Not Contain First Name")

    # Password cannot contain the user's last name.
    if re.search(form.last_name.data, field.data, re.IGNORECASE) is not None:
        raise ValidationError("Password Can Not Last Name")
    #Password should be confirmed
    if form.check_password.data!=field.data:
        raise ValidationError("Confirm Password Field Does Not Match")
