#act1.4-done
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the thrid number: "))

if first_num >= second_num and first_num >= third_num :
    print("\n" + str(first_num), " is the biggest number.")

elif second_num >= third_num :
    print("\n" + str(second_num), " is the biggest number.")

else :
    print("\n" + str(third_num), " is the biggest number.")