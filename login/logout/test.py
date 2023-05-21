#asta merge
# from validate_email_address import validate_email
# isExists = validate_email('alexandruduca29@yaho', verify=True)
# print(isExists)

# from validate_email import validate_email
# is_valid = validate_email('example@example.com',verify=True)
# print(is_valid)
# import re
# def check_if_valid_password(password):
#     while True:
#         if (len(password)<=8):
#             print("Minimum 8 characters.")
#             return False
#         elif not re.search("[a-z]", password):
#             print("The alphabet must be between [a-z].")
#             return False
#         elif not re.search("[A-Z]", password):
#             print("At least one alphabet should be of Upper Case [A-Z].")
#             return False
#         elif not re.search("[0-9]", password):
#             print("At least 1 number or digit between [0-9].")
#             return False
#         elif not re.search("[_@$#]" , password):
#             print("At least 1 character from [ # _ or @ or $ ].")
#             return False
#         elif re.search("\s" , password):
#             return False
#         else:
#             break
#     return True

# print(check_if_valid_password("S2#ajasjjd"))



# from pyisemail import is_email

# email = "mamadsad@gmail.com"
# if is_email(email, allow_gtld=False):
#         raise ValueError("Invalid email address.")

import psycopg2

con = psycopg2.connect(
    database="EMOF",
    user="postgres",
    password="s2receptor",
    host="localhost",
    port= '5432'
)
def check_if_email_match_password(email,password):
    cur = con.cursor()
    sql = "SELECT password FROM users WHERE email = %s"
    cur.execute(sql, (email,))
    account_password = cur.fetchone()[0]
    cur.close()
    if account_password == password:
        return True
    else:
        return False
    
print(check_if_email_match_password("mama@acasa.rot","dsffsdffds"))