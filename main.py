import sys
import time
def valid_date(data):
    if data.isdigit():
        if int(data) >=0:
            return True
    return False
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLNode_keyAndValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def __left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def __right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.__right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.__left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.__left_rotate(root.left)
            return self.__right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.__right_rotate(root.right)
            return self.__left_rotate(root)

        return root

    def delete(self, root, key):
        if root is None:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.__min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.__right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.__left_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.__left_rotate(root.left)
            return self.__right_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.__right_rotate(root.right)
            return self.__left_rotate(root)

        return root

    def search(self, root, key):
        if not root:
            return None
        if root.key == key:
            return root
        if root.key < key:
            return self.search(root.right, key)
        return self.search(root.left, key)
    
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def inorder_traversal(self, root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.key)
            self.inorder_traversal(root.right, result)

class AVLTree_keyAndValue:
    def __init__(self):
        self.root = None
    def __left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def __right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key, value):
        if root is None:
            return AVLNode_keyAndValue(key, value)
        elif key < root.key:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.__right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.__left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.__left_rotate(root.left)
            return self.__right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.__right_rotate(root.right)
            return self.__left_rotate(root)

        return root

    def delete(self, root, key):
        if root is None:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.__min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root
        
    def search(self, root, key):
        if not root:
            return None
        if root.key == key:
            return root.value
        if root.key < key:
            return self.search(root.right, key)
        return self.search(root.left, key)
    
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def inorder_traversal(self, root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append((root.key, root.value))
            self.inorder_traversal(root.right, result)

def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        if func.__name__ == 'add_room':

            print(f"{func.__name__} takes {stop - start:.4f} seconds and add room {result}\n" )
            
        elif func.__name__ == 'remove_room':
            print(f"{func.__name__} takes {stop - start:.4f} seconds and remove room {args[1]}\n")
        else:
            print(f"{func.__name__} takes {stop - start:.4f} seconds\n")
        return result
    return wrapper
class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.table = [AVLTree_keyAndValue() for _ in range(size)]
    
    def __str__(self):
        pass
    def hash_function(self, key: int) -> int:
        return key % self.size
    
    def insert(self, key: int, value):
        index = self.hash_function(key)
        temp = self.table[index]
        temp.root = temp.insert(temp.root, key, value)

    def search(self, key: int): 
        index = self.hash_function(key)
        temp = self.table[index]

        if temp is None:
            return None
        return temp.search(temp.root, key)

    def remove(self, key: int):
        index = self.hash_function(key)
        temp = self.table[index]
        return temp.delete(temp.root, key)
class HilbertsHotel:
    def __init__(self, size: int = 50):
        self.avl_tree = AVLTree()
        self.root = None
        self.hash_table = HashTable(size)
        self.max_room_number = 0

    def calculate_room_number(self, fleet: int, ship: int, bus: int, guest: int):
        return ((fleet+1) ** 7) * ((ship+1)**5) * ((bus+1) ** 3) * ((guest+1) ** 2)
    
    
    @exec_time
    def add_room(self, fleet: int, ship: int, bus: int, guest: int):
        room_number = self.calculate_room_number(fleet, ship, bus, guest)

        if self.hash_table.search(room_number) is None:
            self.hash_table.insert(room_number, (fleet, ship, bus, guest))
            self.root = self.avl_tree.insert(self.root, room_number)
            self.max_room_number = max(self.max_room_number, room_number)
        else:
            i = 0
            new_room_number = room_number
            while self.hash_table.search(new_room_number) is not None:
                i += 1
                new_room_number = room_number + i**2
            self.hash_table.insert(new_room_number, (fleet, ship, bus, guest))
            self.root = self.avl_tree.insert(self.root, new_room_number)
            self.max_room_number = max(self.max_room_number, new_room_number)
            room_number = new_room_number
            
        return room_number
    @exec_time
    def add_room_manual(self, room_number: int):
        if self.hash_table.search(room_number) is None:
            self.hash_table.insert(room_number, "Manual")
            self.root = self.avl_tree.insert(self.root, room_number)
            self.max_room_number = max(self.max_room_number, room_number)
            return room_number   
        return None
    @exec_time
    def remove_room(self, room_number: int):
        if self.hash_table.search(room_number):
            self.hash_table.remove(room_number)
            self.root = self.avl_tree.delete(self.root, room_number)
            print(f"Room {room_number} removed successfully")

    @exec_time
    def sort_rooms(self):
        result = []
        self.avl_tree.inorder_traversal(self.root, result)
        return result

    @exec_time
    def find_room(self, room_number: int):
        result = self.hash_table.search(room_number)
        return result

    @exec_time
    def empty_rooms(self) -> int:
        total_rooms = self.max_room_number
        result = []
        self.avl_tree.inorder_traversal(self.root, result)
        # room_count = sum(1 for slot in self.hash_table.table if slot is not None)
        room_count = sum(1 for slot in result)
        return total_rooms - room_count

    @exec_time
    def save_to_file(self, file_name: str):
        result = []
        data = self.hash_table.table
        for slot in data:
            if slot is not None:
                slot.inorder_traversal(slot.root, result)
        # room_number_fleet_ship_bus_guest
        with open(file_name, 'w') as file:
            for room in result:
                if room[1] == "Manual":
                    file.write(f"{room[0]}_Manual\n")
                else:
                    file.write(f"{room[0]}_{room[1][0]}_{room[1][1]}_{room[1][2]}_{room[1][3]}\n")

                




    def memory_usage(self):
        hash_table_size = sys.getsizeof(self.hash_table)
        for bucket in self.hash_table.table:
            if bucket is not None:
                hash_table_size += sys.getsizeof(bucket)

        def calculate_tree_size(node):
            if node is None:
                return 0
            node_size = sys.getsizeof(node)
            node_size += sys.getsizeof(node.key) + sys.getsizeof(node.key)
            return node_size + calculate_tree_size(node.left) + calculate_tree_size(node.right)

        avl_tree_size = calculate_tree_size(self.root)

        total_size = hash_table_size + avl_tree_size
        return total_size


HilbertsHotel = HilbertsHotel(100)
while True:
    initialguest = input("Enter the guest number for begin: ")
    if valid_date(initialguest):
        initialguest = int(initialguest)
        break
    else:
        print("Invalid guest number")
    
start = time.time()
for i in range(initialguest):
    HilbertsHotel.add_room(0,0,0,i)

stop = time.time()
print(f"Add room all time takes {stop - start:.4f} seconds\n")

while True:
    print("====================================")
    print("1. Add Room")
    print("2. Remove Room")
    print("3. Sort Rooms")
    print("4. Find Room")
    print("5. Empty Rooms")
    print("6. Save to File")
    print("7. Memory Usage")
    print("8. Exit")
    while True:
        choice = input("Enter your choice: ")
        if valid_date(choice):
            choice = int(choice)
            break
    print("====================================")
    if choice == 1:
        print("1. add room n guest ")
        print("2. add room n guest, n bus")
        print("3. add room n guest, n bus, n ship")
        print("4. add room n guest, n bus, n ship, n fleet")
        print("5. add room number manualy")

        print("6. back")
        while True:
            choice = input("Enter your choice: ")
            if valid_date(choice):
                choice = int(choice)
                break   
            else:
                print("Invalid choice")
        print("====================================")
        if choice == 1:
            while True:
                guest = input("Enter the guest number: ")
                if valid_date(guest):
                    guest = int(guest)
                    break
            start = time.time()
            for i in range(guest):
                HilbertsHotel.add_room(0,0,0,i)
            stop = time.time()
            print(f"Add room all time takes {stop - start:.4f} seconds\n")

        elif choice == 2:
            while True:
                guest = input("Enter the guest number: ")
                if valid_date(guest):
                    guest = int(guest)
                    break
                else:
                    print("Invalid guest number")

            while True:
                bus = input("Enter the bus number: ")
                if valid_date(bus):
                    bus = int(bus)
                    break
                else:
                    print("Invalid bus number")

            start = time.time()
            for i in range(bus):
                for j in range(guest):
                    HilbertsHotel.add_room(0,0,i,j)
            stop = time.time()
            print(f"Add room all time takes {stop - start:.4f} seconds\n")

        elif choice == 3:
            while True:
                guest = input("Enter the guest number: ")
                if valid_date(guest):
                    guest = int(guest)
                    break
                else:
                    print("Invalid guest number")
            
            while True:
                bus = input("Enter the bus number: ")
                if valid_date(bus):
                    bus = int(bus)
                    break
                else:
                    print("Invalid bus number")
            
            while True:
                ship = input("Enter the ship number: ")
                if valid_date(ship):
                    ship = int(ship)
                    break
                else:
                    print("Invalid ship number")
            start = time.time()
            for i in range(ship):
                for j in range(bus):
                    for k in range(guest):
                        HilbertsHotel.add_room(0,i,j,k)
            stop = time.time()
            print(f"Add room all time takes {stop - start:.4f} seconds\n")
        elif choice == 4:
            while True: 
                guest = input("Enter the guest number: ")
                if valid_date(guest):
                    guest = int(guest)
                    break
                else:
                    print("Invalid guest number")
            
            while True:
                bus = input("Enter the bus number: ")
                if valid_date(bus):
                    bus = int(bus)
                    break
                else:
                    print("Invalid bus number")
            
            while True:
                ship = input("Enter the ship number: ")
                if valid_date(ship):
                    ship = int(ship)
                    break
                else:
                    print("Invalid ship number")
            
            while True:
                fleet = input("Enter the fleet number: ")
                if valid_date(fleet):
                    fleet = int(fleet)
                    break
                else:
                    print("Invalid fleet number")
            start = time.time()
            for i in range(fleet):
                for j in range(ship):
                    for k in range(bus):
                        for l in range(guest):
                            HilbertsHotel.add_room(i,j,k,l)
            stop = time.time()
        elif choice == 5:

            while True:
                room_number = input("Enter the room number: ")
                if valid_date(room_number):
                    room_number = int(room_number)
                    break
                else:
                    print("Invalid room number")
            

            if HilbertsHotel.add_room_manual(room_number) is not None:
                print(f"Room {room_number} added successfully")
            else:
                print(f"Room {room_number} already exists")
        elif choice == 6:
            continue
        else:
            print("Invalid choice")

    elif choice == 2:
        while True:
            room_number = input("Enter the room number you need remove: ")
            if valid_date(room_number):
                room_number = int(room_number)
                break
            else:
                print("Invalid room number")
        HilbertsHotel.remove_room(room_number)

    elif choice == 3:
        result = HilbertsHotel.sort_rooms()
        print("sorted rooms:")
        if result:
                for room in result[:-1]:
                    print(room, end=", ")   
                print(result[-1], end="")            
                print("\n")

    elif choice == 4:
        while True:
            room_number = input("Enter the room number you need find: ")
            if valid_date(room_number):
                room_number = int(room_number)
                break
            else:
                print("Invalid room number")

        result = HilbertsHotel.find_room(room_number)
        if result is not None:
            print(f"Room {room_number} details: {result}")
        else:
            print(f"Room {room_number} not found")

    elif choice == 5:
        print("1. all Empty Rooms count")
        print("2. Empty Rooms list")
        print("3. back")
        while True:
            choice = input("Enter your choice: ")
            if valid_date(choice):
                choice = int(choice)
                break
            else:
                print("Invalid choice")
        print("====================================")
        if choice == 1:
            print("Empty Room count :" + str(HilbertsHotel.empty_rooms()))
        elif choice == 2:
            print("Empty Rooms list:")
            start = time.time()
            result = []
            sorted_rooms = HilbertsHotel.sort_rooms()
        
            for i in range(HilbertsHotel.max_room_number):
                if i not in sorted_rooms:
                    result.append(i)
        
            if result:
                for room in result[:-1]:
                    print(room, end=", ")   
                print(result[-1], end="")            
                print("\n")
            else:
                print("No empty rooms available.")
            stop = time.time()
            print(f"Empty Rooms list takes {stop - start:.4f} seconds\n")

        elif choice == 3:
            continue
        else:
            print("Invalid choice")

    elif choice == 6:
        file_name = input("Enter the file name: ")
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        HilbertsHotel.save_to_file(file_name)

    elif choice == 7:
        print("Memory Usage: " + str(HilbertsHotel.memory_usage()) + " bytes")

    elif choice == 8:
        break
    else:
        print("Invalid choice")