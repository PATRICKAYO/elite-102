import mysql.connector
import os
def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')



#Empty VARs
account_info = []
userID = 0
username = input()
withdraw = False
balance = 0
place_var = None
place_var2 = ""
password = ""

connection = mysql.connector.connect(user = "root",database = "sysbanking", password = "Bankai$150")
cursor = connection.cursor(buffered= True)








"""
cursor.execute("SELECT * FROM accounts")

result = cursor.fetchall()

print(result)

"""

while True:
    try:    
        print("Hello! Welcome to our banking system. What do you need? (Input the Number)")
        print("1. Create an Account")
        print("2. Delete a Previous Account")
        print("3. Sign In")
        initial_choice = int(input(""))
        if initial_choice == 1:
            clear_console()
            username = input("What is your name?")
            balance = input("What will be your initial balance?")
            password = input("What will be your password?")
            query = f"INSERT INTO accounts (USER_ID, USER_NAME, USER_BALANCE, PASS) VALUES (%s, %s, %s, %s)"
            vals = (f'{userID}', f'{username}', f'{balance}', f'{password}')     
            cursor.execute(query, vals)     
            connection.commit()

            print("Account Created!")
        elif initial_choice == 2:
            try:
                placehold_var = input("What is the password?")
                cursor.execute(f"SELECT * FROM accounts WHERE PASS = '{placehold_var}'")
                place_var = cursor.fetchall()
                print(place_var)
                if place_var:
                    query = f"DELETE FROM accounts WHERE PASS = '{placehold_var}'"
                    cursor.execute(query)
                    connection.commit()
                    print("Successful interaction!")
                else:
                    print("Invalid password, try again.")
            except Exception as e:
                print("Invalid password, (except ver)")
                print(e)
                pass


        elif initial_choice == 3:
            try:
                placehold_var = input("What is the password of your account?")
                cursor.execute(f"SELECT * FROM accounts WHERE PASS = '{placehold_var}'")
                place_var = cursor.fetchall()
                if place_var:
                    clear_console()
                    place_var2 = " ".join(map(str, place_var[0]))
                    place_var = place_var2.split()
                    username = place_var[1]
                    balance = place_var[2]
                    print(f"You are signed in to {username} with {balance} dollars in your account.")
                    print(f'What would you like to do, {username}? (Input the Numbers).')
                    print('1. Deposit')
                    print('2. Withdraw')
                    print('3. Update Account')
                    next_input = int(input(""))
                    if next_input == 1:
                        clear_console()
                        try:
                            balance = float(balance)
                            print(type(balance))
                            print("How much would you like to add?")
                            amount = int(input("Amount:"))
                            amount += balance
                            query = f"UPDATE accounts SET USER_BALANCE = '{amount}' WHERE USER_BALANCE = '{balance}'"
                            cursor.execute(query)
                            connection.commit()
                            print(f"You now have {amount} in your account!")
                            query = f"INSERT INTO transaction_history (USER_ID, USER_NAME, TRANS_TYPE, AMOUNT) VALUES (%s, %s, %s, %s)"
                            vals = (f'{place_var[0]}', f'{place_var[1]}', 'deposit', f'{amount}')
                            cursor.execute(query,vals)
                            connection.commit()
                        except Exception as e:
                            print("Invalid input, please try again. (Valve Error)")
                            print(e)
                    elif next_input == 2:
                        clear_console()
                        try:
                            balance = float(balance)
                            print("How much would you like to withdraw?")
                            amount = int(input("Amount:"))
                            if amount <= balance:
                                amount = balance - amount
                                query = f"UPDATE accounts SET USER_BALANCE = '{amount}' WHERE USER_BALANCE = '{balance}'"
                                cursor.execute(query)
                                connection.commit()
                                print(f"You now have {amount} in your account!")
                                query = f"INSERT INTO transaction_history (USER_ID, USER_NAME, TRANS_TYPE, AMOUNT) VALUES (%s, %s, %s, %s)"
                         import mysql.connector
import os
def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')



#Empty VARs
account_info = []
userID = 0
username = input()
withdraw = False
balance = 0
place_var = None
place_var2 = ""
password = ""

connection = mysql.connector.connect(user = "root",database = "sysbanking", password = "Bankai$150")
cursor = connection.cursor(buffered= True)








"""
cursor.execute("SELECT * FROM accounts")

result = cursor.fetchall()

print(result)

"""

while True:
    try:    
        print("Hello! Welcome to our banking system. What do you need? (Input the Number)")
        print("1. Create an Account")
        print("2. Delete a Previous Account")
        print("3. Sign In")
        initial_choice = int(input(""))
        if initial_choice == 1:
            clear_console()
            username = input("What is your name?")
            balance = input("What will be your initial balance?")
            password = input("What will be your password?")
            query = f"INSERT INTO accounts (USER_ID, USER_NAME, USER_BALANCE, PASS) VALUES (%s, %s, %s, %s)"
            vals = (f'{userID}', f'{username}', f'{balance}', f'{password}')     
            cursor.execute(query, vals)     
            connection.commit()
            
            print("Account Created!")
        elif initial_choice == 2:
            try:
                placehold_var = input("What is the password?")
                cursor.execute(f"SELECT * FROM accounts WHERE PASS = '{placehold_var}'")
                place_var = cursor.fetchall()
                print(place_var)
                if place_var:
                    query = f"DELETE FROM accounts WHERE PASS = '{placehold_var}'"
                    cursor.execute(query)
                    connection.commit()
                    print("Successful interaction!")
                else:
                    print("Invalid password, try again.")
            except Exception as e:
                print("Invalid password, (except ver)")
                print(e)
                pass


        elif initial_choice == 3:
            try:
                placehold_var = input("What is the password of your account?")
                cursor.execute(f"SELECT * FROM accounts WHERE PASS = '{placehold_var}'")
                place_var = cursor.fetchall()
                if place_var:
                    clear_console()
                    place_var2 = " ".join(map(str, place_var[0]))
                    place_var = place_var2.split()
                    username = place_var[1]
                    balance = place_var[2]
                    print(f"You are signed in to {username} with {balance} dollars in your account.")
                    print(f'What would you like to do, {username}? (Input the Numbers).')
                    print('1. Deposit')
                    print('2. Withdraw')
                    print('3. Update Account')
                    next_input = int(input(""))
                    if next_input == 1:
                        clear_console()
                        try:
                            balance = float(balance)
                            print(type(balance))
                            print("How much would you like to add?")
                            amount = int(input("Amount:"))
                            amount += balance
                            query = f"UPDATE accounts SET USER_BALANCE = '{amount}' WHERE USER_BALANCE = '{balance}'"
                            cursor.execute(query)
                            connection.commit()
                            print(f"You now have {amount} in your account!")
                            query = f"INSERT INTO transaction_history (USER_ID, USER_NAME, TRANS_TYPE, AMOUNT) VALUES (%s, %s, %s, %s)"
                            vals = (f'{place_var[0]}', f'{place_var[1]}', 'deposit', f'{amount}')
                            cursor.execute(query,vals)
                            connection.commit()
                        except Exception as e:
                            print("Invalid input, please try again. (Valve Error)")
                            print(e)
                    elif next_input == 2:
                        clear_console()
                        try:
                            balance = float(balance)
                            print("How much would you like to withdraw?")
                            amount = int(input("Amount:"))
                            if amount <= balance:
                                amount = balance - amount
                                query = f"UPDATE accounts SET USER_BALANCE = '{amount}' WHERE USER_BALANCE = '{balance}'"
                                cursor.execute(query)
                                connection.commit()
                                print(f"You now have {amount} in your account!")
                                query = f"INSERT INTO transaction_history (USER_ID, USER_NAME, TRANS_TYPE, AMOUNT) VALUES (%s, %s, %s, %s)"
                                vals = (f'{place_var[0]}', f'{place_var[1]}', 'withdraw', f'{amount}')
                                cursor.execute(query,vals)
                                connection.commit()
                            else:
                                print("Too high, please try again.")
                        except Exception as e:
                            print('Invalid input, please try again. (Valve Error)')
                            print (e)
                    elif next_input == 3:
                        try:
                            new_user = str(input("What do you want your new username to be?"))
                            query = f"UPDATE accounts SET USER_NAME = '{new_user}' WHERE USER_NAME = '{username}'"
                            cursor.execute(query)
                            connection.commit()
                            username = new_user
                            print(f'Your account is now named {username}!')
                        except Exception as e:
                            print('Error, please try again.')
                            print(e)
                    else:
                        print("Invalid input, please try again.")

                else:
                    print("Invalid password, try again.")
            except Exception as e:
                print("Invalid password, (except ver)")
                print(e)
                pass
            
        else:
            print('Invalid option, please try again.')
    except:
        print("Invalid input, please try again.")


                                cursor.execute(query,vals)
                                connection.commit()
                            else:
                                print("Too high, please try again.")
                        except Exception as e:
                            print('Invalid input, please try again. (Valve Error)')
                            print (e)
                    elif next_input == 3:
                        try:
                            new_user = str(input("What do you want your new username to be?"))
                            query = f"UPDATE accounts SET USER_NAME = '{new_user}' WHERE USER_NAME = '{username}'"
                            cursor.execute(query)
                            connection.commit()
                            username = new_user
                            print(f'Your account is now named {username}!')
                        except Exception as e:
                            print('Error, please try again.')
                            print(e)
                    else:
                        print("Invalid input, please try again.")

                else:
                    print("Invalid password, try again.")
            except Exception as e:
                print("Invalid password, (except ver)")
                print(e)
                pass

        else:
            print('Invalid option, please try again.')
    except:
        print("Invalid input, please try again.")

