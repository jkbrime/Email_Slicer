'''
EMAIL SLICER: This project is to enable us distinguish between the user name and the domain name of any email address,
it will also help to indicate if an email addres is valid and/or invalid.
in other words, it will seperate the user name from the domain name for any email address that is entered. 

'''

while True:
  email = input('Enter an email to slice: ')

  if email.count('@') == 1 and len(email[:email.index('@')])>0 and len(email[email.index('@')+1:])>3:
   print("your username is :" + email[:email.index('@')])
   print("youy domain is : " + email[email.index('@')+1:])

  else:
   print('inavlid email!')


