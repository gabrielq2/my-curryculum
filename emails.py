import re

def validar_email(s):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, s) is not None

def filtrar_emails(emails):
    return list(filter(validar_email, emails))

n = int(input("Quantos e-mails você deseja verificar? "))

emails = []
for _ in range(n):
    email = input("Digite um e-mail: ")
    emails.append(email)

emails_validos = filtrar_emails(emails)
print("E-mails válidos:")
print(sorted(emails_validos))
