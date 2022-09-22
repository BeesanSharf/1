numbers = [12,75,150,180,145,525,50]
result_num = []
for item in list(numbers):
   if item > 500:
       break

   if item > 150:
       continue

   if item % 5 == 0 :
       result_num.append(item)
print(result_num)

















