# Showtime-
# Movie Booking using OOP in python

# Youtube Brief Link:
# Movie/ Seat Booking by Rameez Ur Rehman


class showtime:                                                                        # main class
    title = "Welcome to Showtime"
    title1 = "Experience Reality!"
    print(title.center(150))
    print(title1.center(150))


#       function to show menu to the user

    def menu(self):
        ans = True
        while ans:
            print("\nSelect you choice from the ,menu :")
            self.select = int(input(
                "\n1. Show the seats\n2. Buy a Ticket\n3. Statistics\n4. Show booked ticket & user info\n0. Exit\n"))

            if self.select == 1:
                self.seats()
            elif self.select == 2:
                self.buy()
            elif self.select == 3:
                self.stats()
            elif self.select == 4:
                self.info()
            elif self.select == 0:
                ans = False
                self.ex()
            else:
                print("\nInvalid selected. Try again")


        #Initiated here

    def __init__(self):
        self.row = int(input("Enter the number of rows in theater\n"))
        self.col = int(input("Enter the number of seats in each row\n"))
        self.num_seats = self.row * self.col
        self.matrix = []
        self.seat_count = 0
        self.current_income = 0
        self.total_income = 0
        self.u_details = {}
        for i in range(self.row):
            a = []
            for j in range(self.col):
                a.append("S")
            self.matrix.append(a)
        print(end="  ")

    # if user input=1:
    def seats(self):                                                                 #function to show matrix
        print("\nCinema :\n")
        a = 0
        b = 0
        print(end="  ")
        for j in range(1, self.col + 1):
            b = b + 1
            print(b, end=" ")
        print()
        for i in self.matrix:
            a = a + 1
            print(a, end=" ")
            print(" ".join(i), sep=",")

    #     if user input=2:
    def buy(self):                                                                  #function to buy a ticket
        a = int(input("Enter the row you want to book\n"))
        b = int(input("Enter the column you want to book\n"))
        if self.matrix[a - 1][b - 1] == "B":
            print("This seat is already booked")
            self.menu()
        elif self.num_seats < 60:
            self.price = 10
            print("The ticket price is $10 Press Y/y to proceed")
        elif a < self.row / 2:
            self.price = 10
            print("The ticket price is $10 Press Y/y to proceed")
        elif a > self.row / 2:
            self.price = 8
            print("Ticket per person is $8, do you wish to continue? Press Y/y")
        self.pr = input()



        if self.pr == 'Y' or self.pr == 'y':                                        #stores user info in dict
            u_dict = {}
            Uname = input("Thanks for booking,n Enter your name\n")
            Ugen = input("Enter your gender\n")
            UAge = input("Enter your age\n")
            Ucn = input("Enter your Contact Number\n")
            self.row1 = a - 1
            self.col1 = b - 1
            self.matrix[self.row1][self.col1] = "B"
            self.seat_count = self.seat_count + 1
            self.current_income = self.current_income + self.price
            u_dict[(self.row1 + 1), (self.col1 + 1)] = list((Uname, Ugen, UAge, Ucn, self.price))
            self.u_details.update(u_dict)
            print("Booked successfully !!\n")
        else:
            print("Booking couldn't be processed!\n")




    def total_revenue(self):                                                         #called in statistics for total revenue
        if self.num_seats < 60:                                                      #for upper half
            self.total_income = self.num_seats * 10                                  #
        elif self.num_seats >= 60:
            for i in range(0, int(self.row / 2)):
                c = int(self.row / 2) * self.col * 10
            for j in range(int(self.row / 2), self.row):
                d = int(self.row / 2) * self.col * 8
            self.total_income = c + d
        return self.total_income

    #     if user input=3
    def stats(self):                                                                 #function for the statistics
        print("Number of purchased tickets : ", self.seat_count)
        self.percentage = (self.seat_count / self.num_seats) * 100
        print("Percentage of Tickets Booked : ", "{:.2f}".format(self.percentage), "%")
        print("Current Income : $", self.current_income)
        k = self.total_revenue()
        print("Total Income : $", k)





    #     if user input=4
    def info(self):                                                                  #function to display info
        self.check_a = int(input("Enter your row number\n"))
        self.check_b = int(input("Enter your seat number \n"))
        if self.matrix[self.check_a - 1][self.check_b - 1] == 'B':
            c = self.u_details[(self.check_a, self.check_b)]
            print('Name:', c[0])
            print('Gender:', c[1])
            print('Age:', c[2])
            print('Mobile:', c[3])
        else:
            print("This seat is not booked yet!")

    def ex(self):
        return None


bmm_obj = showtime()
bmm_obj.menu()
