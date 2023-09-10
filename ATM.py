p = float(input("Enter PKR: "))
print("User Inputs: ", p)

fiveTho = p / 5000  # get hundred
print("5000 :", int(fiveTho))

fiveTho = p % 5000  # left

oneT = fiveTho / 1000  # get hundred
print("1000 :", int(oneT))

oneT = p % 1000  # left

fiveT = oneT / 500  # get hundred
print("500 :", int(fiveT))

th5 = p % 500  # left

hund = th5 / 100  # get hundred
print("100 :", int(hund))

lefth = p % 100  # left

fifty = lefth / 50  # get 50
print("50", int(fifty))

fiftyl = lefth % 50  # left

ten = fiftyl / 10  # 10
print("10 :", int(ten))

fiftyl = fiftyl % 10  # left
print(fiftyl)
