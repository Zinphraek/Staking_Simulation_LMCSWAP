import sys

import random

from pyinputplus import *

from Core import P_list


class Package:
    """This is a representation of a package."""

    def __init__(self, pack_nbr, pack_name, pack_value, pack_roi, pack_monthly_roi, pack_weekly_roi, pack_life):
        # self.pack_id = pack_id
        self.pack_nbr = pack_nbr
        self.pack_name = pack_name
        self.pack_value = pack_value
        self.pack_roi = pack_roi
        self.pack_monthly_roi = pack_monthly_roi
        self.pack_weekly_roi = pack_weekly_roi
        self.pack_life = pack_life

    def get_pack_information(self):
        package = f"Pack number: {self.pack_nbr}, Pack name: {self.pack_name}, Pack value: ${self.pack_value}," \
                  f" Pack yearly ROI: ${self.pack_roi}, Pack monthly ROI: ${self.pack_monthly_roi}," \
                  f" Pack weekly ROI: ${self.pack_weekly_roi}, Pack life: {self.pack_life} weeks."
        return package

    def get_p_nbr(self):
        pack_number = self.pack_nbr
        return pack_number

    def get_p_name(self):
        pack_name = self.pack_name
        return pack_name

    def get_p_value(self):
        p_value = self.pack_value
        return float(p_value)

    def get_p_roi(self):
        p_roi = self.pack_roi
        return float(p_roi)

    def get_p_m_roi(self):
        p_m_roi = self.pack_monthly_roi
        return float(p_m_roi)

    def get_p_w_roi(self):
        p_w_roi = self.pack_weekly_roi
        return float(p_w_roi)

    def get_p_life(self):
        p_life = self.pack_life
        return int(p_life)

    def p_life_remaining(self, life):
        self.pack_life -= life
        print(f'The remaining life for this pack is: {self.pack_life} weeks.')


packs = []
for nbr, (n, v, y, m, w, t) in P_list.items():
    z = Package(nbr, n, v, y, m, w, t)
    packs.append(z)
my_packs = []
cash = 0
total_payments = 0
total_withdraw = 0
capital_invested = 0
withdraw_count = 0
funding_decision = True


def cash_adjustment(b):
    """This function take in the value of a pack and subtract it from the cash balance when a pack is bought"""
    global cash
    cash -= b
    print(f'Your new balance is: ${cash}')


def congratulation(a, p):
    print(f" Congratulation!!! You just bought {a}.")
    print(f"Here is the list of the packs you possess so far: {p}")


def buy_packs(value):
    """This function buy the highest pack with the available cash = value"""
    if value < 200:
        pass
    else:
        while value >= 200:
            if value >= 100000:
                pack10 = Package('pack_10', 'OUAGA', 100000, 225000, 17307, 4326, 52)
                my_packs.append(pack10)
                congratulation(pack10.get_pack_information(), my_packs)
                cash_adjustment(pack10.get_p_value())
                value -= pack10.get_p_value()
                print(f"You now have {len(my_packs)} active packs!")
                continue

            elif 100000 > value >= 51200:
                pack09 = Package('pack_09', 'Dubai', 51200, 114688, 8822, 2205.5, 52)
                my_packs.append(pack09)
                congratulation(pack09.get_pack_information(), my_packs)
                cash_adjustment(pack09.get_p_value())
                value -= pack09.get_p_value()
                print(f"You now have {len(my_packs)} active packs!")
                continue

            elif 51200 > value >= 25600:
                pack08 = Package('pack_08', 'Abuja', 25600, 56320, 4332, 1083.07, 52)
                my_packs.append(pack08)
                congratulation(pack08.get_pack_information(), my_packs)
                cash_adjustment(pack08.get_p_value())
                value -= pack08.get_p_value()
                print(f"You now have {len(my_packs)} active packs!")
                continue

            elif 25600 > value >= 12800:
                pack07 = Package('pack_07', 'Le Caire', 12800, 27520, 2116.92, 529.23, 52)
                my_packs.append(pack07)
                congratulation(pack07.get_pack_information(), my_packs)
                cash_adjustment(pack07.get_p_value())
                value -= pack07.get_p_value()
                print(f"You now have {len(my_packs)} active packs!")
                continue

            elif 12800 > value >= 6400:
                pack06 = Package('pack_06', 'Pretoria', 6400, 13440, 1033.84, 258.46, 52)
                my_packs.append(pack06)
                congratulation(pack06.get_pack_information(), my_packs)
                cash_adjustment(pack06.get_p_value())
                value -= pack06.get_p_value()
                print(f"You now have {len(my_packs)} active packs!")
                continue

            elif 6400 > value >= 3200:
                pack05 = Package('pack_05', 'Yaounde', 3200, 6560, 504.6, 126.15, 52)
                my_packs.append(pack05)
                congratulation(pack05.get_pack_information(), my_packs)
                cash_adjustment(pack05.get_p_value())
                value -= pack05.get_p_value()
                print(f"You now have {len(my_packs)} active packs!")
                continue

            elif 3200 > value >= 1600:
                pack04 = Package('pack_04', 'Malabo', 1600, 3200, 246.12, 61.53, 52)
                my_packs.append(pack04)
                congratulation(pack04.get_pack_information(), my_packs)
                cash_adjustment(pack04.get_p_value())
                value -= pack04.get_p_value()
                print(f"You now have {len(my_packs)} active packs!")
                continue

            elif 1600 > value >= 800:
                pack03 = Package('pack_03', 'Ndjamena', 800, 1520, 116.92, 29.23, 52)
                my_packs.append(pack03)
                congratulation(pack03.get_pack_information(), my_packs)
                cash_adjustment(pack03.get_p_value())
                value -= pack03.get_p_value()
                print(f"You now have {len(my_packs)} active packs!")
                continue

            elif 800 > value >= 400:
                pack02 = Package('pack_02', 'Libreville', 400, 720, 55.36, 13.84, 52)
                my_packs.append(pack02)
                congratulation(pack02.get_pack_information(), my_packs)
                cash_adjustment(pack02.get_p_value())
                value -= pack02.get_p_value()
                print(f"You now have {len(my_packs)} active packs!")
                continue

            else:
                pack01 = Package('pack_01', 'Porto Novo', 200, 340, 26.12, 6.53, 52)
                my_packs.append(pack01)
                congratulation(pack01.get_pack_information(), my_packs)
                cash_adjustment(pack01.get_p_value())
                value -= pack01.get_p_value()
                print(f"You now have {len(my_packs)} active packs!")


def get_pack(value):

    if value < 200:
        global funding_decision, cash, capital_invested
        while funding_decision:
            print("You don't have enough money yet to buy a pack!\n"
                  " Fund your account, or continue without additional funds. ")
            print("(1) Add fund to my account.\n"
                  "(2) Continue without funding.\n"
                  "(3) Do not ask again.\n"
                  "(4) Exit simulation")
            decision = inputNum('> ')
            if decision == 4:
                sys.exit()
            elif decision == 3:
                funding_decision = False
            elif decision == 2:
                break
            elif decision == 1:
                print("How much do you want to fund?")
                print(f"The minimum amount needed to buy a pack right now is ${200-cash}.")
                while True:
                    fund = inputNum()
                    if fund <= 0:
                        print("Enter a value greater than 0.")
                        continue
                    else:
                        cash += fund
                        buy_packs(cash)
                        capital_invested += fund
                        break

            else:
                print(f"{decision} is not a valid entry. Chose from 1 to 3.")
                continue
    else:
        buy_packs(value)


def get_paid(balance):
    """This function pays the user the corresponding amount
    of any pack bough """
    if not my_packs:
        sys.exit()
    else:
        global cash, total_payments
        for pack in my_packs:
            balance += pack.get_p_w_roi()
            cash = balance
            total_payments += pack.get_p_w_roi()
            print(f"HooHaa!!! You just got paid the amount of: ${pack.get_p_w_roi()}"
                  f"\nYour new Balance is: ${balance}.")
            pack.p_life_remaining(1)
            if pack.get_p_life() >= 1:
                pass
            else:
                my_packs.remove(pack)
                print(f" The life span of the pack {pack} has expired; "
                      f"therefore, it is no longer active, and has been removed from your pack list.")
                print(f"You now have {len(my_packs)} active packs remaining!")


def make_withdraw(frequency, withdraw_amount, w_e):
    """This function operates withdraws according to the frequency, and the amount provided by the user;
    w_e represent the number of weeks elapsed. The function also count the number of withdrawals made"""

    global cash, total_withdraw, withdraw_count
    if frequency != 0 and w_e % frequency == 0 and cash >= withdraw_amount:
        cash -= withdraw_amount
        total_withdraw += withdraw_amount
        withdraw_count += 1

        print(f"Great news!!! A withdraw of ${withdraw_amount} has been made!"
              f" You made {withdraw_count} withdraws so far, totaling ${total_withdraw}.")
        print(f"Your new balance is ${cash}.")
    else:
        pass


def main():
    print("""--Liyeplimal investment simulation--

    Purpose:
        This program helps the user simulate different investment strategies
        and displays the result. This part is the automated version.
        A manual version will be added to this program latter.""")

    print('\n')
    print("Select what you want to do:\n"
          "(1) Run a simulation.\n"
          "(2) Trade.\n"
          "(3) Exit.")
    while True:
        choice = inputNum('> ')
        if choice == 3:
            print('Thank you!')
            sys.exit()
        elif choice == 2:
            print("Do you want to Buy or Sell?\n"
                  "(1) Buy.\n"
                  "(2) Sell.\n"
                  "(3) Exit.")
            while True:
                action = inputNum('> ')
                if action == 1:
                    while True:
                        quantity = inputNum('Entre the quantity you would like to purchase: ')
                        if quantity <= 0:
                            print('The quantity must be greater than 0.')
                            continue
                        else:
                            while True:
                                max_price = inputNum('Enter the maximum price you are willing to pay per unit: ')
                                if max_price <= 0:
                                    print("The price must be greater than 0.")
                                    continue
                                else:
                                    print("Your order has been placed; you will be notified when it is completed.")
                                    break
                            break
                    break
                elif action == 2:
                    while True:
                        quantity = inputNum('Entre the quantity you would like to sell: ')
                        if quantity <= 0:
                            print('The quantity must be greater than 0.')
                            continue
                        else:
                            while True:
                                min_price = inputNum('Enter the minimum price you are willing to accept per unit: ')
                                if min_price <= 0:
                                    print("The price must be greater than 0.")
                                    continue
                                else:
                                    print("Your order has been placed; you will be notified when it is completed.")
                                    break
                            break
                    break
                elif action == 3:
                    print('Thank you!')
                    sys.exit()
                else:
                    print(f"{action} is not a valid entry. Enter 1, 2, or 3.")
                    continue
        elif choice == 1:
            freq = 0  # freq is the frequency of the withdraw.
            withdraw_value = 0
            for pack in packs:
                print(pack.get_pack_information())
            print('\n')
            print("Enter the cash amount or the value of the pack you would like to start with!")
            global cash
            while True:  # Making sure the user enter a value greater or equal to 200.
                cash = inputNum()
                if cash < 200:
                    print("The minimum amount is $200.")
                    continue
                else:
                    break
            print('\n')

            print("Enter the length (IN YEARS) of the investment simulation you would like to run.")
            while True:  # Making sure the user enter a value greater or equal to 1.
                length_in_years = inputNum()
                if length_in_years < 1:
                    print("The minimum investment year is 1.")
                    continue
                else:
                    break

            invest_length = int(length_in_years) * 52

            while True:
                print("Would you be making withdrawals? Y/N")
                response = input('> ')
                if response.lower() == 'n' or response.lower() == 'no':
                    freq = 0
                    break
                elif response.lower() == 'y' or response.lower() == 'yes':
                    print("Enter the amount you would like to periodically withdraw.")
                    while True:  # Making sure the user enter a negative value.
                        withdraw_value = inputNum()
                        if withdraw_value < 0:
                            print("The withdraw amount must be greater than 0!")
                            continue
                        else:
                            break

                    while True:
                        print("Enter the frequency of your withdraw.\n"
                              "(1) Weekly.\n"
                              "(2) Biweekly.\n"
                              "(3) Monthly.\n"
                              "(4) Quarterly.\n"
                              "(5) Semi annually.\n"
                              "(6) Annually.\n"
                              "(7) Randomly.")

                        message = inputNum('> ')  # Setup the withdrawal frequency.
                        if message == 1:
                            freq = 1
                            break
                        elif message == 2:
                            freq = 2
                            break
                        elif message == 3:
                            freq = 4
                            break
                        elif message == 4:
                            freq = 12
                            break
                        elif message == 5:
                            freq = 24
                            break
                        elif message == 6:
                            freq = 52
                            break
                        elif message == 7:
                            freq = random.randint(1, 52)
                            break
                        else:
                            print(
                                f"{message} is not a valid option. Chose from the following: 'W', 'B', 'M', 'Q', 'S', 'A'.")
                            continue
                    break

                else:
                    print(f"{response} is not a valid entry. Enter Y/N")
                    continue

            while True:  # This is the main loop.
                # Buys packs with the cash provided:
                get_pack(cash)
                for k in range(invest_length):
                    print(f'Week {k + 1}:')
                    get_paid(cash)
                    make_withdraw(freq, withdraw_value, k + 1)
                    get_pack(cash)
                    print(f"Your Balance is: ${cash}\n")

                o = invest_length + 1
                while my_packs:
                    print(f" Week {o}:")
                    get_paid(cash)
                    print(f"Your total payments is: {total_payments}")
                    make_withdraw(freq, withdraw_value, o)
                    o += 1
                    print('\n')
                sys.exit()
        else:
            print(f"{choice} is not a valid entry; chose from 1 to 3.")
            continue


# Let's run the program:
if __name__ == '__main__':
    main()