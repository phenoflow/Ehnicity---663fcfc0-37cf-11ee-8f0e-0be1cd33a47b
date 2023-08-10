# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"9S3..00","system":"readv2"},{"code":"9S43.00","system":"readv2"},{"code":"9S43.11","system":"readv2"},{"code":"9S44.00","system":"readv2"},{"code":"9S45.11","system":"readv2"},{"code":"9SA4.00","system":"readv2"},{"code":"9SA4.11","system":"readv2"},{"code":"9SA5.00","system":"readv2"},{"code":"9SA6.11","system":"readv2"},{"code":"9SB6.00","system":"readv2"},{"code":"9i4..00","system":"readv2"},{"code":"9iA3.00","system":"readv2"},{"code":"9iC..00","system":"readv2"},{"code":"9iFA.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ehnicity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["afric-ehnicity---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["afric-ehnicity---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["afric-ehnicity---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
