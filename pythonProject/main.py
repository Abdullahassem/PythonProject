import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # after you run the script this will make a new file that only contains the emails
    with open('emails.csv','w',newline='') as outfile:

        csv_writer=csv.DictWriter(outfile,fieldnames=['email'],delimiter='\t')

        for line in csv_reader:
            del line['first_name']
            del line['last_name']
            csv_writer.writerow(line)
            # if you want to just print the emails directly:
            print(line['email'])


