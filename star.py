#star printing N rows and N Columns using while

no_of_row = int(input("Enter The Number Of Rows : "))   # no of rows input from user
no_of_col = int(input("Enter The Number Of Columns : "))# no of columns input from user

counter = 0                    # Initialization
while counter < no_of_row :    # Checking the row condition
    while counter < no_of_col: # Checking the col condition 
        print("* " * no_of_col) # printing the no of columns
        break                   # after priting the code will out of the loop
    counter = counter + 1       #Updation


