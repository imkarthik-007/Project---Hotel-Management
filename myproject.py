class hotelfarecal:

    def __init__(self,tb=0,rr=0,rb=0,fb=0,lb=0,a=0,gb=0,name='',address='',cindate='',rno="-"):

        print ("\n\n*****WELCOME TO PARADISE HOTEL*****\n")

        self.tb=tb

        self.rb=rb

        self.fb=fb
        self.lb=lb
        self.gb=gb
        self.rr=rr
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        print("\nGlad to have you here respected",self.name,"...!:)")
        
    def room(self):
      while(1):
        print ("We have the following rooms for you:-")
        print("Enter a number to select the room or 5 to exit..!")

        print ("1.Type A---->rs 6000 PN/-")

        print ("2.Type B---->rs 5000 PN/-")

        print ("3.Type C---->rs 4000 PN/-")

        print ("4.Type D---->rs 3000 PN/-")
        print ("5.Exit")
        x=input("\nEnter your choice please:\n")

        if(x=="1"):

            print ("Thank you for opting room type A")
            n=int(input("For how many days do You wanna stay?"))


            self.rr=6000*n

        elif (x=="2"):

            print ("Thank you for opting room type B")
            n=int(input("For how many days do you wanna stay?"))

            self.rr=5000*n

        elif (x=="3"):

            print ("Thank you for opting room type C")
            n=int(input("For how many days do you wanna stay?"))

            self.rr=4000*n

        elif (x=="4"):
            print ("Thank you for opting room type D")
            n=int(input("For how many days do you wanna stay:"))

            self.rr=3000*n
        elif (x=="5"):
            break
        else:

            print ("Please choose a room. Enter 1 to 5 only :(")
            continue
        self.rno=102
        self.a=1000
        print ("your room rent is =",self.rr,"\nAnd ",self.rno,"is your room, you can stay there...! :)\n")

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print(" 1.water-->Rs.20/- \n","2.tea-->Rs.10/-\n","3.breakfast combo-->Rs.90/-\n","4.lunch-->Rs.110/-\n","5.snacks-->Rs.35/-\n","6.dinner-->Rs.150/-\n","7.Exit\n")


        while (1):

            print("\nEnter a number to eat anything or 7 to exit..!")
            c=input("Enter your choice: ")


            if (c=="1"):
                d=int(input("Enter the quantity:"))
                self.rb=self.rb+20*d
                self.a=1000

            elif (c=="2"):
                 d=int(input("Enter the quantity:"))
                 self.rb=self.rb+10*d
                 self.a=1000

            elif (c=="3"):
                 d=int(input("Enter the quantity:"))
                 self.rb=self.rb+90*d
                 self.a=1000

            elif (c=="4"):
                 d=int(input("Enter the quantity:"))
                 self.rb=self.rb+110*d
                 self.a=1000
                 
            elif (c=="5"):
                d=int(input("Enter the quantity:"))
                self.rb=self.rb+35*d
                self.a=1000
        
            elif (c=="6"):
                 d=int(input("Enter the quantity:"))
                 self.rb=self.rb+150*d
                 self.a=1000

            elif (c=="7"):
                break
            else:
                print("Please select an option from 1 to 7 only :(")
                continue

        print ("Total food Cost=Rs",self.rb,"\n")


    def	laundrybill(self):
        print ("*****LAUNDRY MENU*****")

        print (" 1.Shorts-->Rs.3/-\n","2.Trousers-->Rs.4/-\n","3.Shirt-->Rs.5/-\n","4.Jeans-->Rs.6/-\n","5.Girlsuit-->Rs.8/-\n","6.Exit\n")

        while (1):

            print("\nEnter a number as per the dress item or enter 6 to exit..!")
            e=input("Enter your choice: ")

            if (e=="1"):
                f=int(input("How many pieces? "))
                self.lb=self.lb+3*f
                self.a=1000

            elif (e=="2"):
                f=int(input("How many pieces? "))
                self.lb=self.lb+4*f
                self.a=1000

            elif (e=="3"):
                f=int(input("How many pieces? "))
                self.lb=self.lb+5*f
                self.a=1000

            elif (e=="4"):
                f=int(input("How many pieces? "))
                self.lb=self.lb+6*f
                self.a=1000

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