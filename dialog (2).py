from Tkinter import *
import tkSimpleDialog
import tkMessageBox

root = Tk()
label1 = Label(root,text='MMService!!',bg='blue',fg='yellow')
label1.pack(fill=X)
down = Frame(root)
down.pack(side=BOTTOM)

answer = tkSimpleDialog.askinteger('MMservices', '1.buy Airtime \n2.buy Data Bundle \n3.buy Voice Bundle \n4.send money \n5.change PIN \n6.check balance ',
                                parent=root)
if answer == 1:
    amount = tkSimpleDialog.askinteger('buy Airtime','enter amount:',parent=root)
    if amount is not None:
        pin = tkSimpleDialog.askinteger("buy Airtime", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
        if len(str(pin)) > 4:
            invalid = tkSimpleDialog.askinteger('invalid pin!!', parent=root)
        else:
            tkMessageBox.showinfo('buy Airtime','Transaction successul ')

    else:
         tkMessageBox.showinfo('buy Airtime','no amount entered!')
        
    
elif answer == 2:
    answer = tkSimpleDialog.askinteger('buy Data Bundles', '1.Daily \n2.Weekly \n3.Monthly ',
                             parent=root)

    if answer == 1:
        answer = tkSimpleDialog.askinteger('Daily',"1.50mbs@500UGX \n2.120mbs@1000UGX \n3.200mbs@1500UGX",parent=root)
    
        if answer == 1:
            pin = tkSimpleDialog.askinteger("buy 50mbs@500UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 50mbs@500UGX','Transaction successul ')

        elif answer == 2:
            pin = tkSimpleDialog.askinteger("buy 120mbs@1000UGX ", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 120mbs@1000UGX ','Transaction successul ')

        elif answer == 3:
            pin = tkSimpleDialog.askinteger("buy 200mbs@1500UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 200mbs@1500UGX ','Transaction successul ')

        else:
            tkMessageBox.showinfo('Daily','invalid input!')




    elif answer == 2:
        answer = tkSimpleDialog.askinteger('Weekly',"1.1GB@3500UGX \n2.2GB@5500UGX \n3.5GB@8000UGX \n4.12GB@13000UGX",parent=root)

        if answer == 1:
            pin = tkSimpleDialog.askinteger("buy 1GB@3500UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 1GB@3500UGX','Transaction successul ')

        elif answer == 2:
            pin = tkSimpleDialog.askinteger("buy 2GB@5500UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 2GB@5500UGX','Transaction successul ')

        elif answer == 3:
            pin = tkSimpleDialog.askinteger("buy 5GB@8000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 5GB@8000UGX ','Transaction successul ')

        elif answer == 4:
            pin = tkSimpleDialog.askinteger("buy 12GB@13000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 12GB@13000UGX ','Transaction successul ')

        else:
            tkMessageBox.showinfo('Daily','invalid input!')
         
        

    elif answer == 3:
        answer = tkSimpleDialog.askinteger('Monthly',"1.10GB@15000UGX \n2.15GB@20000UGX \n3.20GB@22000UGX \n4.30GB@28000UGX",parent=root)

        if answer == 1:
            pin = tkSimpleDialog.askinteger("buy 10GB@15000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 10GB@15000UGX','Transaction successul ')

        elif answer == 2:
            pin = tkSimpleDialog.askinteger("buy 15GB@20000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 15GB@20000UGX','Transaction successul ')

        elif answer == 3:
            pin = tkSimpleDialog.askinteger("buy 20GB@22000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 20GB@22000UGX ','Transaction successul ')

        elif answer == 4:
            pin = tkSimpleDialog.askinteger("buy 30GB@28000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 30GB@28000UGX ','Transaction successul ')

        else:
            tkMessageBox.showinfo('Daily','invalid input!')

    else:
         tkMessageBox.showinfo('Data Bundles','invalid input!')

elif answer == 3:
    answer = tkSimpleDialog.askinteger('buy Voice Bundles', '1.Daily \n2.Weekly \n3.Monthly ',
                             parent=root)

    if answer == 1:
        answer = tkSimpleDialog.askinteger('Daily',"1.30mins@1000UGX \n 2.60mins@2000UGX \n 3.120mins@3000UGX",parent=root)

        if answer == 1:
            pin = tkSimpleDialog.askinteger("buy 30mins@1000UGX ", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 30mins@1000UGX ','Transaction successul ')

        elif answer == 2:
            pin = tkSimpleDialog.askinteger("buy 60mins@2000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 60mins@2000UGX','Transaction successul ')

        elif answer == 3:
            pin = tkSimpleDialog.askinteger("buy 120mins@3000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 120mins@3000UGX ','Transaction successul ')

        else:
            tkMessageBox.showinfo('Daily','invalid input!')

    
    elif answer == 2:
        answer = tkSimpleDialog.askinteger('Weekly',"1.200mins@3000UGX \n 2.300mins@4000UGX",parent=root)

        if answer == 1:
            pin = tkSimpleDialog.askinteger("buy 200mins@3000UGX ", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 200mins@3000UGX ','Transaction successul ')

        elif answer == 2:
            pin = tkSimpleDialog.askinteger("buy 300mins@4000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 300mins@4000UGX','Transaction successul ')

        else:
            tkMessageBox.showinfo('Weekly','invalid input!')


    elif answer == 3:
        answer = tkSimpleDialog.askinteger('Monthly',"1.4hrs@9000UGX \n 2.6hrs@12000UGX \n 3.10hrs@15000UGX",parent=root)

        if answer == 1:
            pin = tkSimpleDialog.askinteger("buy 4hrs@9000UGX ", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 4hrs@9000UGX ','Transaction successul ')

        elif answer == 2:
            pin = tkSimpleDialog.askinteger("buy 6hrs@12000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 6hrs@12000UGX','Transaction successul ')

        elif answer == 3:
            pin = tkSimpleDialog.askinteger("buy 10hrs@15000UGX", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('buy 10hrs@15000UGX ','Transaction successul ')

        else:
            tkMessageBox.showinfo('Monthly','invalid input!')

            
    else:
        tkMessageBox.showinfo('Monthly','invalid input!')


elif answer == 4:
    answer = tkSimpleDialog.askinteger('send money', '1.Network No. \n2.Other Network No. ',
                             parent=root)
    if answer == 1:
        no_ = tkSimpleDialog.askinteger("Network No. ", "Enter No.:",
                                 parent=root,
                                 minvalue=0, maxvalue=99999999999)
        
        if no_ is not None:
            amount = tkSimpleDialog.askinteger("Network No. ", "Enter amount:",
                                 parent=root)
            
            pin = tkSimpleDialog.askinteger("Network No.", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('Transaction successul ',str(amount) +'UGX transffered to '+ str(no_))

        else:
            tkMessageBox.showinfo('Network No.','invalid input!')

    elif answer == 2:
        no_ = tkSimpleDialog.askinteger("Other Network No. ", "Enter No.:",
                                 parent=root,
                                 minvalue=0, maxvalue=99999999999)
        
        if no_ is not None:
            amount = tkSimpleDialog.askinteger("Other Network No. ", "Enter amount:",
                                 parent=root)
            
            pin = tkSimpleDialog.askinteger("Other Network No.", "Enter pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            tkMessageBox.showinfo('Transaction successul ',str(amount) +'UGX transffered to '+ str(no_))

        else:
            tkMessageBox.showinfo('Other Network No.','invalid input!')

        
        
    else:
        tkMessageBox.showinfo('Send Money','invalid input!')


elif answer == 5:
    pin = tkSimpleDialog.askinteger("change pin ", "Enter current pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
    
    newpin = tkSimpleDialog.askinteger("change pin ", "Enter new pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
            
       
    confpin = tkSimpleDialog.askinteger("change pin ", "confirm new pin:",
                                 parent=root,
                                 minvalue=0, maxvalue=9999)
    
    if confpin == newpin:
        tkMessageBox.showinfo('change pin','PIN successfully changed!')
        
         

    


