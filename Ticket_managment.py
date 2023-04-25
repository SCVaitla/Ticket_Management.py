import re
import smtplib

# Define the local IT departments and their email addresses
local_it_departments = {
    'hardware': 'hardware@example.com',
    'software': 'software@example.com',
    'network': 'network@example.com',
    'other': 'other@example.com'
}

# Define a function to categorize IT tickets based on keywords
def categorize_ticket(ticket):
    if re.search(r'(?i)(hardware|device|laptop|computer|printer)', ticket):
        return 'hardware'
    elif re.search(r'(?i)(software|application|app|license)', ticket):
        return 'software'
    elif re.search(r'(?i)(network|internet|wifi|ethernet|connection)', ticket):
        return 'network'
    else:
        return 'other'

# Define a function to forward IT tickets to the appropriate local IT departments
def forward_ticket(ticket, department_email):
    from_email = "svaitla3@huskers.unl.edu"
    password = "Pokemon22033"

    try:
        server = smtplib.SMTP("smtp.example.com", 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, department_email, ticket)
        server.quit()
        print(f"Ticket has been forwarded to {department_email}")
    except Exception as e:
        print(f"Failed to forward ticket: {e}")

# Read IT tickets from a file (one ticket per line) or use an API
with open('it_tickets.txt', 'r') as file:
    tickets = file.readlines()

# Process the IT tickets
for ticket in tickets:
    ticket = ticket.strip()
    department_key = categorize_ticket(ticket)
    department_email = local_it_departments[department_key]
    forward_ticket(ticket, department_email)
