for num in range(2,10):
    if num % 2 == 0:
        print(f"even : {num}")
        continue
    print(f"odd : {num}")   
# even : 2
# odd : 3
# even : 4
# odd : 5
# even : 6
# odd : 7
# even : 8
# odd : 9
# if no 'continue'  -> cannot distinguish even and odd -> it will print each number is even and odd like : 
# even : 2
# odd : 2
# odd : 3
# even : 4
# odd : 4
# odd : 5
# even : 6
# odd : 6
# odd : 7
# even : 8
# odd : 8
# odd : 9