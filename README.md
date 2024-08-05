
            elif (e=="5"):
                f=int(input("How many pieces? "))
                self.lb=self.lb+8*f
                self.a=1000
            elif (e=="6"):
                break;
            else:

                print ("Please select an option from 1 to 6 only :(")
                continue


        print ("Total Laundary Cost=Rs",self.lb,"\n")


    def gamebill(self):
        print ("\n******WELCOME TO THE GAMING WORLD*******")
        print("\nSelect an option from the menu below:")
        print (" 1.Table tennis-->Rs.60/-\n","2.Bowling-->Rs.80/- \n","3.Snooker-->Rs.70/-\n","4.Video games-->Rs.90/-\n","5.Pool-->Rs.50/- \n","6.Exit\n")



        while (1):

            print("\nEnter a number to play a game or 6 to exit from the gaming world..!")
            g=input("Enter your choice:")


            if (g=="1"):
                h=int(input("No. of hours:"))
                self.gb=self.gb+60*h
                self.a=1000

            elif (g=="2"):
                h=int(input("No. of hours:"))
                self.gb=self.gb+80*h
                self.a=1000

            elif (g=="3"):
                h=int(input("No. of hours:"))
                self.gb=self.gb+70*h
                self.a=1000

            elif (g=="4"):
                h=int(input("No. of hours:"))
                self.gb=self.gb+90*h
                self.a=1000

            elif (g=="5"):
                h=int(input("No. of hours:"))
                self.gb=self.gb+50*h
                self.a=1000
                
            elif (g=="6"):
                break;

            else:

                print ("Please select an option from 1 to 6 only :(")
                continue



        print ("Total Gaming Bill = Rs.",self.gb,"/-\n")

    def display(self):
        print ("\n******HOTEL BILL******")
        print ("CUSTOMER DETAILS:-")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.rr)
        print ("Your Food bill is:",self.fb)
        print ("Your laundary bill is:",self.lb)
        print ("Your Game bill is:",self.gb)

        self.tb=self.rr+self.fb+self.lb+self.gb+self.rb

        print ("Your sub total bill is Rs.",self.tb,"/-")
        print ("Additional Service Charges are Rs.",self.a,"/-")
        print ("Your grandtotal bill is Rs.",self.tb+self.a,"/-\n")

            

        

        

def main():

    a=hotelfarecal()
    a.inputdata()
    while(1):
        print("\nEnter a digit as per the menu below -->")
        
        print("1.Book a room :)")

        print("2.Lets eat something..!")

        print("3.Laundry here..!")

        print("4.Wanna play some games? ")

        print("5.Total bill here..!")

        print("6.EXIT here..!")

        b=input("\nEnter your choice:") 

        if (b=="1"):

            a.room()

        elif (b=="2"):

            a.restaurentbill()

        elif (b=="3"):

            a.laundrybill()

        elif (b=="4"):

            a.gamebill()

        elif (b=="5"):

            a.display()

        elif (b=="6"):
            print("Thank You..! Visit again :-)")
            quit()
            
        else:
            print("Please select an option from 1 to 6 only :(")
            continue



main()
