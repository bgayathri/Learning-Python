#Python code to analyze teradata tables and classify them based on NPI/NON-NPI.
#It will print the roles for every table 

########Teradata Connectivity#############
import teradata
import csv
 
udaExec = teradata.UdaExec (appName="HelloWorld", version="1.0",
        logConsole=False)
 
session = udaExec.connect(method="odbc", system="oneview",
        username="vro173", password="Geethu30");
 
c = session.cursor()
########Input Variables####################
fname = input("Enter file name: ")
count = 0
columnname = []
npi_flag = False
npilist = ["plstc_srgt_id", "social_security_number", "ssn", "bin", "bin_num", "tin", "plastic_num"]
my_data = {}
role="Role"
job_flag="Y"
#outfile = open("out.csv", "w")

# my_data = {'database_name' : 100, 'table_name' : 101, 'column_name' : 102, 'NPI_FLAG' : 103, 'JOB_FLAG' : 104, 'Role' : 105}
###########Gathering details from table######
with open(fname) as csvfile:
	my_reader = csv.reader(csvfile, delimiter='|')
	#my_writer = csv.writer(outfile, delimiter=',')
	for row in my_reader:
		c.execute("SELECT DATABASENAME, TABLENAME, COLUMNNAME FROM DBC.COLUMNS where DATABASENAME='{0}' AND TABLENAME = '{1}';".format(row[0], row[1]))
		output = c.fetchall()

		# If the table doesn't have any columns in DBC.COLUMNS, continue
		if not output:
			databasename = row[0]
			tablename = row[1]
			continue

		for x in output:
			columnname.append(x['COLUMNNAME'].strip())
		else:
			databasename = x['DATABASENAME']
			tablename = x['TABLENAME']	
		

		cmp_str = " ".join(columnname)

		for x in npilist:
			if x in cmp_str:
				npi_flag = True

		
		my_data = {"DATABASENAME":databasename , "TABLENAME":tablename, "COLUMNNAME":columnname, "NPI_FLAG":npi_flag, "JOB_FLAG":job_flag, "role":role}
		
	#	my_writer.writerow(columnname)
    
		columnname = []
		count += 1
		print(row)	
		npi_flag = False
		print(my_data)
		
		if count == 5:
				break

