import csv

def CSV_Reader():
    with open('apy.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print ', '.join(row)
            
def main():
    CSV_Reader()
    
main()