from random import choice, sample, shuffle
from string import  ascii_uppercase, ascii_lowercase, punctuation, digits
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('length', metavar='N', nargs='?', default=8, type=int,
                    help='Specifies the length of the password')
parser.add_argument('upper_case', metavar='N', nargs='?', default=1, type=int,
                    help='pecifies the number of upper case letters in password')
parser.add_argument('punctuations', metavar='N', nargs='?', default=1, type=int,
                    help='Specifies the number of punctuations in password')
parser.add_argument('digit_number', metavar='N', nargs='?', default=1, type=int,
                    help='Specifies the number of digits in password')
parser.add_argument('exclude', nargs='?', default='', help='Filters out specific characters')

def generate_password(length, 
                      upper_case_letters,
                      punctuations,
                      digit_number,
                      exclude):
    """Generates a random password for specific criteria
       
        Parameters
        ----------
        length : int
            The length of the password
        upper_case_letters : int
            The number of upper case letters in the password
        punctuations: int
            The number of punctuations in the password
        digit_number : int
            The number of digits in the password
        exclude: str
            Filter out spcific characters
        
        Raises
        ------
        ValueError:
            Raised when the specifications characters are greater than the password's length

        Returns
        ------
        str
            a str of the password
    """
    lower_case_letters = (length - (upper_case_letters + punctuations + digit_number))
    password = ''

    try:
        if lower_case_letters < 0:
            raise ValueError("Specification cannot be greater than the password's length.")
        
        filtered_punctuation = punctuation.translate({ord(i): None for i in exclude})
            
        password_list = [choice(ascii_uppercase) for i in range(upper_case_letters)]
        password_list += [choice(filtered_punctuation) for i in range(punctuations)]
        password_list += [choice(digits) for i in range(digit_number)]
        password_list += [choice(ascii_lowercase) for i in range(lower_case_letters)]
        
        shuffle(password_list)
        password = ''.join(password_list)

    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e.args)

    finally:
        return password
        

args = parser.parse_args()
print(generate_password(args.length, args.upper_case, args.punctuations, args.digit_number, args.exclude))






