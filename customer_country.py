import csv
def main():
    infile = open('customers.csv', 'r')
    outfile = open('customer_country.csv', 'w')
    csv_obj = csv.reader(infile)
    header = next(csv_obj)
    print(header)


    for rec in csv_obj:
        name = f"{rec[1]} {rec[2]}"
        country = rec[4]
        outfile.write(f"{name},{country}\n")
        print(f"{name, country}")
        
    infile.close()
    outfile.close() 
main()



        
    