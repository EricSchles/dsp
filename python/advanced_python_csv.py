# I chose to just switch back to a series
# instead of using the csv library to convert
import pandas as pd

faculty_data = pd.read_csv('faculty.csv')

list_of_emails = list(faculty_data[' email'])

series_of_emails = pd.Series(list_of_emails)
series_of_emails.to_csv('emails.csv',index=False)
