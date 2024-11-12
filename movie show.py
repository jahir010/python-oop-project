class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.seats[id] = [[f'{chr(i+65)}{j}' for  j in range(self.cols)] for i in range(self.rows)]
    
    def book_seats(self, c_name, c_phone_number, id, seat_list):
        if id in self.seats:
            check = False
            f = False
            booked_list = []
            for seat in seat_list:
                for st in self.seats[id]:
                    if seat in st:
                        check = True
                if check == False:
                    print(f'Invalid seat number {seat}')
                    continue
                check = False
                row = ord(seat[0]) - 65
                col = int(seat[1])
                if self.seats[id][row][col] != 'x':
                    self.seats[id][row][col] = 'x'
                    booked_list.append(seat)
                    f = True
                else:
                    print(f'{seat} already booked')
            if f == True:
                print('Ticket booked successfully\n')
                print('************ Ticket infos *************')
                print(f'Name : {c_name}       Mobile : {c_phone_number}')
                print(f'Show Id : {id}       Hall no : {self.hall_no}')
                for show in self.__show_list:
                    if id in show:
                        print(f'Movie : {show[1]}       time : {show[2]}')
                        break
                print('Seat(s) :', end=" ")
                for i in booked_list:
                    print(i, end=" ") 
                print('\n_________________________________________')
            else:
                print('No seat for you')
        else:
            print('Invalid show ID')
    
    def view_show_list(self):
        print(f'************* SHOW LIST ************')
        for show in self.__show_list:
            print(f'Show id: {show[0]}    Movie: {show[1]}    Time: {show[2]}')
        print('-------------------------------------')
    
    def view_available_seats(self, id):
        if id not in self.seats:
            print("Invalid Id information")
            return
        print('************* AVAILABLE SEATS ***************')
        for show in self.__show_list:
            if id in show:
                print(f'Movie : {show[1]}       Time : {show[2]}')
        print('x for booked')
        for seat in self.seats[id]:
            for s in seat:
                print(s, end="    ")
            print()

        

if __name__ == "__main__":
    Sony = Hall(4, 5, 'H-2')
    Sony.entry_show('abc', 'avatar', '20:30')
    Sony.entry_show('abd', 'Outlander', '07:00')

    while True:
        print('1. View shows ')
        print('2. View available seats')
        print('3. Book seats')
        print('0. For exit')
        option = int(input('Enter option: '))
        if option == 1:
            print('\n\n')
            Sony.view_show_list()
        elif option == 2:
            print('\n\n')
            id = input('Enter show id :')
            Sony.view_available_seats(id)
        elif option == 3:
            print('\n\n')
            name = input('Customer Name : ')
            mobile_no = input('Mobile no : ')
            id = input('Show id : ')
            list = []
            print('How many seat you want to book? ')
            seat_no = int(input())
            for i in range(seat_no):
                seat = input('Enter seat : ')
                list.append(seat)
            Sony.book_seats(name, mobile_no, id, list)
        elif option == 0:
            break
        print('\n\n')
            
    
