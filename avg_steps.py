import csv

def main():

    steps_total = [0] * 12
    number_of_days = [0] * 12

    infile= open('steps.csv','r')
    csv_obj = csv.reader(infile)
    header = next(csv_obj) 
    
    for rec in csv_obj:
        month = int(rec[0])  
        steps = int(rec[1])  
        
        if 1 <= month <= 12:
            index = month - 1  
            steps_total[index] += steps
            number_of_days[index] += 1

    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    for i in range(12):
        avg_steps = steps_total[i] / number_of_days[i]
        print(f"{month_names[i]:} - {avg_steps:,.2f}")


main()
