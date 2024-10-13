class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)


class Room:
    def __init__(self, number, channel, car=None, boat=None):
        self.number = number
        self.channel = channel  
        self.car = car         
        self.boat = boat   


class HilbertsHotel:
    def __init__(self):
        self.rooms = {} 
        self.guests_by_walk = Queue()   
        self.guests_by_car = Queue() 
        self.guests_by_boat = Queue()  
        self.next_room_number = 1  
    
    def add_guests_by_walk(self, people_count):
        for person in range(people_count):
            room_number = self.next_room_number
            self.guests_by_walk.enqueue((person + 1, room_number))
            self.next_room_number += 1

    def add_guests_by_car(self, car_count, people_per_car):
        for car in range(car_count):
            for person in range(people_per_car):
                room_number = self.next_room_number
                self.guests_by_car.enqueue((car + 1, person + 1, room_number))
                self.next_room_number += 1 

    def add_guests_by_boat(self, boat_count, car_count_per_boat, people_per_car):
        for boat in range(boat_count):
            for car in range(car_count_per_boat):
                for person in range(people_per_car):
                    room_number = self.next_room_number
                    self.guests_by_boat.enqueue((boat + 1, car + 1, person + 1, room_number))
                    self.next_room_number += 1 
    

    def check_in_guests(self):
        while not self.guests_by_car.is_empty() or not self.guests_by_boat.is_empty() or not self.guests_by_walk.is_empty():
            if not self.guests_by_walk.is_empty():
                person, room_number = self.guests_by_walk.dequeue()
                self.rooms[room_number] = Room(room_number, 'Walk')
                print(f"Person {person} (walk-in) Room :{room_number}")

            if not self.guests_by_car.is_empty():
                car, person, room_number = self.guests_by_car.dequeue()
                self.rooms[room_number] = Room(room_number, 'Car', car=car)
                print(f"Car {car}, Person {person}, Room :{room_number}")

            if not self.guests_by_boat.is_empty():
                boat, car, person, room_number = self.guests_by_boat.dequeue()
                self.rooms[room_number] = Room(room_number, 'Boat', car=car, boat=boat)
                print(f"Boat {boat}, Car {car}, Person {person}, Room : {room_number}")

    def display_rooms(self):
        print(f"Total rooms: {len(self.rooms)}")
        sorted_rooms = self.quick_sort_rooms()
        for room_number, room in sorted_rooms:
            if room.channel == 'Car':
                print(f"Room {room_number}: by {room.channel}, Car {room.car}")
            elif room.channel == 'Boat':
                print(f"Room {room_number}: by {room.channel}, Boat {room.boat}, Car {room.car}")
            elif room.channel == 'Walk':
                print(f"Room {room_number}: walk-in")
    
    def quick_sort_rooms(self):
        room_items = list(self.rooms.items())
        
        def quick_sort(items):
            if len(items) <= 1:
                return items
            pivot = items[len(items) // 2]
            left = [x for x in items if x[0] < pivot[0]]
            middle = [x for x in items if x[0] == pivot[0]]
            right = [x for x in items if x[0] > pivot[0]]
            return quick_sort(left) + middle + quick_sort(right)
        
        return quick_sort(room_items)
    
    def binary_search(self, room_number):
        sorted_rooms = self.quick_sort_rooms()
        low = 0
        high = len(sorted_rooms) - 1
        
        while low <= high:
            mid = (low + high) // 2
            mid_room_number = sorted_rooms[mid][0]
            if mid_room_number == room_number:
                return sorted_rooms[mid][1]  
            elif mid_room_number < room_number:
                low = mid + 1
            else:
                high = mid - 1
        return None  

    def find_room(self, room_number):
        result = self.binary_search(room_number)
        if result:
            print(f"Room {room_number} found: Channel {result.channel}, Car {result.car}, Boat {result.boat}")
        else:
            print(f"Room {room_number} not found")

hotel = HilbertsHotel()

hotel.add_guests_by_walk(5)
hotel.add_guests_by_car(3, 4)
hotel.add_guests_by_boat(2, 2, 3)

hotel.check_in_guests()

hotel.display_rooms()

hotel.find_room(5)
hotel.find_room(10)
hotel.find_room(100)
