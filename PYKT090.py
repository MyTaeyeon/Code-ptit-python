with open('CONTACT.in') as file:
    emails = set()
    for mail in file:
        emails.add(mail.strip().lower())
emails = sorted(emails)
print(*emails, sep='\n')
