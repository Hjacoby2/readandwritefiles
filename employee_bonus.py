import csv
def main():
    infile = open('employee_data.csv', 'r')
    csv_obj = csv.reader(infile)
    header = next(csv_obj)
    
    for rec in csv_obj:
        name = rec[1]
        salary = float(rec[3]) 
        bonus_dec = float(rec[7])

        bonus = salary * bonus_dec
        pay = salary + bonus

        print(f"Name: {name}")
        print(f"Salary: $ {salary:.2f}")
        print(f"Bonus: $ {bonus:.2f}")
        print(f"Pay: $ {pay:.2f}")
        print()
    



    infile.close()
main()

