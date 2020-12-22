from tabulate import tabulate

headers = ["Bet", "Minimum"]

assos = float(input("1: "))
xi = float(input("X: "))
diplo = float(input("2: "))

total_bet = float(input("Total bet: "))

print("\n")

assos_bet = total_bet/assos
xi_bet = total_bet/xi
diplo_bet = total_bet/diplo

sum_pred = assos_bet + xi_bet + diplo_bet

if sum_pred > total_bet:
    print("Total bet:", sum_pred, "- Need to ban a choice \n")

    remove = input("Remove (1, x, 2): ")

    if remove == "1":
        assos_bet = 0
        xi_bet = total_bet/xi
        diplo_bet = total_bet/diplo
    elif remove == "x":
        xi_bet = 0
        assos_bet = total_bet/assos
        diplo_bet = total_bet/diplo
    elif remove == "2":
        diplo_bet = 0
        assos_bet = total_bet/assos
        xi_bet = total_bet/xi

    sum_pred = assos_bet + xi_bet + diplo_bet

if (assos_bet == 0 or xi_bet == 0 or diplo_bet == 0) and (sum_pred > total_bet):
    print("\n")
    print("This game is not worthy")
else:
    print("\n")
    data = [("1", assos_bet), ("X", xi_bet), ("2", diplo_bet)]
    print(tabulate(data, headers=headers))
