 #Finds phone numbers and email address 
import pyperclip,re
#create phone regex
phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?  
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
 )''',re.VERBOSE)
#create email regex
emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+      #username
    @
    [a-zA-Z0-9.-]+         #domain name
    (\.[a-zA-Z]{2,4})      
 )''',re.VERBOSE)
#find matches in given text
text=str(pyperclip.paste())

matches= []
for phonenum in phoneRegex.findall(text):
    phoneNumber = '-'.join([phonenum[0]])
    matches.append(phoneNumber)

for emails in emailRegex.findall(text):
    matches.append(emails[0])
# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

