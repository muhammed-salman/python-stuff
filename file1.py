students={
    'stud1':{'name':'bano', 'rollno':'68'},
    'stud2':{'name':'zeeshan', 'rollno':'61'}
}
with open('myfile.txt','w') as myfile:
    myfile.write(str(students))
