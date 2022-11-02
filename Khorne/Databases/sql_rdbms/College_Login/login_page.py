# INTERFACE FOR ACCOUNT LOGIN AND REGISTRATION
import time
import sqlite3  # import module

mydb=sqlite3.connect("main_db.db") # establish connection
curs=mydb.cursor() # create cursor for navigation through database


# MAIN PAGE FUNCTION
def home_page():
    print("-------------------------------------WELCOME TO BLUBOOK--------------------------------------")
    print("LOG IN  or SIGN UP")
    print('Press (1) -- log in \nPress (2) -- sign up')

# REDIRECTING to Login or Registration depending upon user input
    comm=input()    
    # A Login
    if comm == '1':
        # AA compare username with database, to check if it exists
        user_name=input('Enter username: ')
        curs.execute('SELECT * FROM MAIN_PAGE WHERE USER_NAME=?',(user_name,))
        u_name=curs.fetchone()
        #print(u_name) #Data from database if username exists
        p_word=input('Enter Password: ')

        # AAA if username doesnt exist
        if u_name == None:
            print('Invalid Username or Password')
            time.sleep(2)
            home_page()

        # AAB if username does exist
        else:
            # AAAA if password matches
            if p_word == u_name[3]:
                print("LOGGED IN SUCCESSFULLY")

                # AAAAA Change password request
                prompt1=input("change password ? (y/n) ")
                
                if prompt1 == 'y':
                    def p_word_change():
                        # AAAABA Check to see if new password matches
                        p_word_enter=input("Enter New password: ")
                        p_word_confirm=input("Confirm New password: ")
                        if p_word_enter == p_word_confirm:
                            p_word_exist=input("Enter Current password: ")
                            
                            if p_word_exist == u_name[3]:
                                curs.execute('UPDATE MAIN_PAGE SET PASSWORD = ? WHERE USER_NAME= ?',(p_word_confirm,user_name))
                                mydb.commit()
                                print('Password Successfully changed')
                                
                            elif p_word_exist != u_name[3]:
                                print('password incorrect ! you will be logged out...')
                                time.sleep(0.8)
                                print('eta: 3 sec..')
                                time.sleep(0.8)
                                print('eta: 2 sec..')
                                time.sleep(0.8)
                                print('eta: 1 sec..')
                                time.sleep(0.8)
                                print('....')
                                time.sleep(0.8)
                                home_page()
                                
                        elif p_word_enter != p_word_confirm:
                            print('Passwords not matched, Please try again')
                            p_word_change()
                    p_word_change()
                    
                elif prompt1 == 'n':
                    print('Thank you for Logging in')

            # @@@  if password mismatch     
            elif p_word != u_name[3]:
                print('Invalid Username or Password')
                time.sleep(2)
                home_page()

    # B Registration
    elif comm == '2':
        def new_reg():
            print('------------------------------------------------NEW REGISTRATION ---------------------------------------------------')
            new_name=input('Please Enter your Name: ')
            new_u_name=input("Enter the username for your account: ")
            curs.execute('SELECT * FROM MAIN_PAGE WHERE USER_NAME=?',(new_u_name,))
            
            if curs.fetchone() != None:
                print('Username already exists')
                time.sleep(2)
                new_reg()
                
            elif curs.fetchone() == None:
                new_p_word=input("Enter a password for your account: ")
                new_p_word_confirm=input("Please confirm the password: ")
                
                if new_p_word == new_p_word_confirm:
                    curs.execute('INSERT INTO MAIN_PAGE (NAME, USER_NAME, PASSWORD) VALUES (?,?,?)', (new_name,new_u_name,new_p_word))
                    mydb.commit()
                    print('NEW REGISTRATION SUCCESSFUL')
                    time.sleep(2)
                    home_page()
                    
                elif new_p_word != new_p_word_confirm:
                    print('Passwords not matched, Please try again')
                    time.sleep(2)
                    new_reg()
        new_reg()
        
    elif comm != '1' or comm != '2':
        print('Please choose from either (1) or (2)')
        time.sleep(2)
        home_page()

    # C Crash message
    else:
        print('MAIN PAGE CRASHED')



home_page()
