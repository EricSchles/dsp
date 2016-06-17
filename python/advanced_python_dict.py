import pandas as pd
import re as re

# Importing the data
faculty_data = pd.read_csv('faculty.csv')

# Adding 'abriged_title'
changing_titles = {'Professor of Biostatistics': 'Professor',
                   'Associate Professor of Biostatistics': 'Associate Professor',
                   'Assistant Professor of Biostatistics': 'Assistant Professor',
                   'Assistant Professor is Biostatistics': 'Assistant Professor'}

faculty_data['abridged_title'] = faculty_data[' title'].map(changing_titles)

faculty_dict = {}
final_answer = []

for index, row in faculty_data.iterrows():

    last_name = re.search(r'([\w.]+\Z)', row['name'])
    first_name = re.search(r'^([\w.]+)', row['name'])

    faculty_dict[last_name.group() + ', ' + first_name.group()] = [row[' degree'], row['abridged_title'], row[' email']]

for key, value in faculty_dict.items():
    final_answer.append((key + ' : ' + str(value)))

return(sorted(final_answer))
