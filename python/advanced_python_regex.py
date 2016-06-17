import pandas as pd
import re as re

# Importing the data
faculty_data = pd.read_csv('faculty.csv')

list_of_emails = list(faculty_data[' email'])

return (list_of_emails)

# Using regular expressions to find the answer

list_of_domains = []

for email in list_of_emails:
    match = re.search(r'([\w.]+)@([\w.]+)', email)
    list_of_domains.append(match.group(2))

domain_final_answer = {}
for domain in list_of_domains:
    if domain not in domain_final_answer:
        domain_final_answer[domain] = 1
    else:
        domain_final_answer[domain] += 1

return (pd.Series(domain_final_answer))
