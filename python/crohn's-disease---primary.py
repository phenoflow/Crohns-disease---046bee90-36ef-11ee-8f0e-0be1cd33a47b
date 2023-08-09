# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"J08z900","system":"readv2"},{"code":"J401z11","system":"readv2"},{"code":"J40z.11","system":"readv2"},{"code":"Jyu4000","system":"readv2"},{"code":"N031100","system":"readv2"},{"code":"N045300","system":"readv2"},{"code":"11119.0","system":"med"},{"code":"11286.0","system":"med"},{"code":"11337.0","system":"med"},{"code":"12575.0","system":"med"},{"code":"15773.0","system":"med"},{"code":"20480.0","system":"med"},{"code":"20688.0","system":"med"},{"code":"28476.0","system":"med"},{"code":"29616.0","system":"med"},{"code":"36913.0","system":"med"},{"code":"39037.0","system":"med"},{"code":"39278.0","system":"med"},{"code":"44426.0","system":"med"},{"code":"51576.0","system":"med"},{"code":"51578.0","system":"med"},{"code":"52449.0","system":"med"},{"code":"593.0","system":"med"},{"code":"59994.0","system":"med"},{"code":"62628.0","system":"med"},{"code":"63036.0","system":"med"},{"code":"64773.0","system":"med"},{"code":"6538.0","system":"med"},{"code":"66238.0","system":"med"},{"code":"69959.0","system":"med"},{"code":"71945.0","system":"med"},{"code":"9359.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('crohn's-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["crohn's-disease---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["crohn's-disease---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["crohn's-disease---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
