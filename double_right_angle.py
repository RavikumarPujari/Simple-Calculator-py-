# Double Right Angle 
No_of_rows = int(input())      #reading the number of rows from user

#by using While loop
counter = 0                          #initialization
while counter  <= No_of_rows:        #condition
    print("* " * counter)            #printing the pattern
    counter += 1                     #increment 
    if counter == No_of_rows + 1:
        counter = 0 
        while counter  <= No_of_rows: #condition
         print("* " * counter)        #printing the pattern
        counter += 1                  #increment
        