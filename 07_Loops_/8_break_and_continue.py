
print("Break Statement Example:")

for i in range(100):
    if(i == 45):
        break  # Exit the loop right now.
    print(i)

print("Continue Statement Example:")

for i in range(100):
    if(i == 45):
        continue  # Skip this interation only and continue with next.
    print(i)

# In the first loop, when the value of 'i' reaches 45, the 'break' statement is executed, causing the loop to terminate immediately. As a result, no. from 0 to 44 are printed, and the loop stops before reaching 45.

# In the second loop, when 'i' is 45, the 'continue' statement is executed. This causes the loop to skip the current iteration (i.e., it does not print 45) and move on to the next iteration. Therefore, all numbers from 0 to 99 are printed except for 45.
