
#for  code part  ofstudent management system 
students={}      

while True:
   print("add student\ndelete student\nupdate marks\nsearch student\nexit")
   option = input("Enter your option:")

  # add feature to add the name and marks 
   if option == "add":
    name =str(input("Enter name:"))

    if name in students:
     print("already exist")
     
    
    else:
     students[name]=int(input("Enter marks:"))
     print("student added sucessfully")
    with open ("studentdetails.txt","a+") as f:
     f.write(name+"="+str(students[name])+"\n")
     
    
# to delete the student from the file
   elif option == "delete":
    name =str(input("Enter name:"))

    if name in students:
     del students[name]
     print("student deleted sucessfully")
     with open ("studentdetails.txt","r") as f:
        lines = f.readlines()
        with open ("studentdetails.txt","w") as f:
            for line in lines:
               if name not in line:
                f.write(line)
                print("student deleted sucessfully")
    else:
     print("student not found")
# to update the marks of students 
   elif option == "update":
    name =str(input("Enter name:"))

    if name in students:
     students[name]=int(input("Enter marks:"))  
     print("student marks updated sucessfully")
     with open ("studentdetails.txt","r") as f:
        lines = f.readlines()
        with open ("studentdetails.txt","w") as f:
            for line in lines:
               if name not in line:
                f.write(line)
            f.write(name+"="+str(students[name])+"\n")
    else:
     print("student not found")
# to search the student in linear search
   elif option == "search":
     name=str(input("Enter name to search:"))
     with open("studentdetails.txt","r") as f:
       lines=f.read()
       if name in lines:
         print("Found the student in list")
       else:
         print("not found the student")
    #exit from the code 
   elif option == "exit":
      break       

        

