returned_day, returned_month, returned_year = map(int, input().split())
due_day, due_month, due_year = map(int, input().split())

if returned_year > due_year:
    print(10000)
elif returned_year == due_year and returned_month > due_month:
    print(500 * (returned_month - due_month))
elif returned_year == due_year and returned_month == due_month and returned_day > due_day:
    print(15 * (returned_day - due_day))
else:
    print(0)