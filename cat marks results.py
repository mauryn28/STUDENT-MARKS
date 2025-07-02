import csv

# Open the input file
with open('STUDENT OUTPUT.CSV', mode='r', newline='', encoding='utf-8-sig') as infile:
    reader = csv.DictReader(infile)
    students = []

    # Process each student
    for row in reader:
        adm = row['Admission Number']
        name = row['Name']
        cat = int(row['CAT'])
        final = int(row['Final'])
        total = cat + final
        status = "Passed" if total > 40 else "Failed"

        # Store results
        students.append({
            'Admission Number': adm,
            'Name': name,
            'CAT': cat,
            'Final': final,
            'Total': total,
            'Status': status
        })

# Write to output CSV
with open('STUDENT OUTPUT.CSV', mode='w', newline='') as outfile:
    fieldnames = ['Admission Number', 'Name', 'CAT', 'Final', 'Total', 'Status']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("Done! Results saved in 'students_output.csv'")