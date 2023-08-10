# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"9i...00","system":"readv2"},{"code":"9i00.00","system":"readv2"},{"code":"9i1..00","system":"readv2"},{"code":"9i10.00","system":"readv2"},{"code":"9i2..00","system":"readv2"},{"code":"9i20.00","system":"readv2"},{"code":"9i22.00","system":"readv2"},{"code":"9i23.00","system":"readv2"},{"code":"9i26.00","system":"readv2"},{"code":"9i27.00","system":"readv2"},{"code":"9i28.00","system":"readv2"},{"code":"9i29.00","system":"readv2"},{"code":"9i2A.00","system":"readv2"},{"code":"9i2B.00","system":"readv2"},{"code":"9i2E.00","system":"readv2"},{"code":"9i2F.00","system":"readv2"},{"code":"9i2G.00","system":"readv2"},{"code":"9i2H.00","system":"readv2"},{"code":"9i2J.00","system":"readv2"},{"code":"9i2K.00","system":"readv2"},{"code":"9i2L.00","system":"readv2"},{"code":"9i2M.00","system":"readv2"},{"code":"9i2N.00","system":"readv2"},{"code":"9i2P.00","system":"readv2"},{"code":"9i5..00","system":"readv2"},{"code":"9i60.00","system":"readv2"},{"code":"9i61.00","system":"readv2"},{"code":"9i62.00","system":"readv2"},{"code":"9i63.00","system":"readv2"},{"code":"9i64.00","system":"readv2"},{"code":"9i7..00","system":"readv2"},{"code":"9iA..00","system":"readv2"},{"code":"9iA1.00","system":"readv2"},{"code":"9iA2.00","system":"readv2"},{"code":"9iA4.00","system":"readv2"},{"code":"9iA5.00","system":"readv2"},{"code":"9iA6.00","system":"readv2"},{"code":"9iA8.00","system":"readv2"},{"code":"9iD..00","system":"readv2"},{"code":"9iD0.00","system":"readv2"},{"code":"9iD1.00","system":"readv2"},{"code":"9iD2.00","system":"readv2"},{"code":"9iE..00","system":"readv2"},{"code":"9iF..00","system":"readv2"},{"code":"9iF1.00","system":"readv2"},{"code":"9iF2.00","system":"readv2"},{"code":"9iF3.00","system":"readv2"},{"code":"9iF4.00","system":"readv2"},{"code":"9iF5.00","system":"readv2"},{"code":"9iF6.00","system":"readv2"},{"code":"9iF7.00","system":"readv2"},{"code":"9iF8.00","system":"readv2"},{"code":"9iF9.00","system":"readv2"},{"code":"9iFB.00","system":"readv2"},{"code":"9iFC.00","system":"readv2"},{"code":"9iFD.00","system":"readv2"},{"code":"9iFE.00","system":"readv2"},{"code":"9iFF.00","system":"readv2"},{"code":"9iFJ.00","system":"readv2"},{"code":"9iFK.00","system":"readv2"},{"code":"9iG..00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ehnicity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ehnicity-categ---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ehnicity-categ---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ehnicity-categ---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
