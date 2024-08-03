from bs4 import BeautifulSoup

GPA_GRADE_VALUE = {'HD': 4.0, 'D': 3.0, 'C': 2.0}
CGPA_GRADE_VALUE = {'HD': 4.0, 'D': 3.67, 'C': 2.85}


with open("result_table.txt", 'r') as textfile:

  html = textfile.read()
  soup = BeautifulSoup(html, 'html5lib')
  
  # Find all <tr> elements
  rows = soup.find_all('tr')

  # Filter <tr> elements based on the condition
  filtered_rows = []
  for row in rows:
      cells = row.find_all('td')
      for cell in cells:
          try:
              value = int(cell.get_text().strip())
              if 1900 <= value <= 2030:
                  filtered_rows.append(row)
                  break  # If any cell meets the condition, add the row and break the loop
          except ValueError:
              pass  # Ignore non-integer values 

  credit_points_sum = 0
  weighted_marks_sum = 0
  weighted_gpa_sum = 0
  weighted_cgpa_sum = 0

  # iterate all marks, get their sums
  for row in filtered_rows:
      tds = row.find_all('td')
      if len(tds) == 7:
          credit_points = int(tds[4].text)
          marks = int(tds[5].text)
          grade = tds[6].text
          gpa_grade_value = GPA_GRADE_VALUE[grade]
          cgpa_grade_value = CGPA_GRADE_VALUE[grade]

          credit_points_sum += credit_points
          weighted_marks_sum += marks*credit_points
          weighted_gpa_sum += gpa_grade_value*credit_points
          weighted_cgpa_sum += cgpa_grade_value*credit_points

  # get the averages
  average_wam = weighted_marks_sum/credit_points_sum
  average_gpa = weighted_gpa_sum/credit_points_sum
  average_cgpa = weighted_cgpa_sum/credit_points_sum

  print("WAM: ", average_wam)
  print("GPA: ", average_gpa)
  print("CGPA: ", average_cgpa)





          


