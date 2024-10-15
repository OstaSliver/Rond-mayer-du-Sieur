import pandas as pd
import sys
import time

class AVLNode:
    def __init__(self, key):
        self.key = key
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

def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        if func.__name__ == 'add_room':
            room_number = result
            print(f"{func.__name__} takes {stop - start:.4f} seconds and {args[0].collisions} collisions add room {result}\n" )
            
        elif func.__name__ == 'remove_room':
            print(f"{func.__name__} takes {stop - start:.4f} seconds and remove room {args[1]}\n")
        else:
            print(f"{func.__name__} takes {stop - start:.4f} seconds")
        return result
    return wrapper

class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.count = 0  # To track the number of elements
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key: int) -> int:
        return key % self.size
    
    def hash_function2(self, key: int) -> int:
        return 7 - (key % 7)
    
    def insert(self, key: int, value):
        if self.count / self.size >= 0.7:  # Check load factor (e.g., 70% full)
            self.resize()  # Expand table if needed
        
        # old version
        # index = self.hash_function(key)
        # self.table[index].append((key, value))
        # self.count += 1 

        # new version
        i = 0
        while i < self.size:
            index = (self.hash_function(key) + i * self.hash_function_2(key)) % self.size
            if self.table[index] is None:
                self.table[index] = (key, value)
                self.count += 1
                return
            i += 1
    
    def search(self, key: int):
        # old version
        # index = self.hash_function(key)
        # for room_number, value in self.table[index]:
        #     if room_number == key:
        #         return value
        # return None
        
        # new version
        i = 0
        while i < self.size:
            index = (self.hash_function(key) + i * self.hash_function_2(key)) % self.size
            if self.table[index] and self.table[index][0] == key:
                return self.table[index][1]
            i += 1
        return None

    def remove(self, key: int):
        # old version
        # index = self.hash_function(key)
        # for i, (room_number, value) in enumerate(self.table[index]):
        #     if room_number == key:
        #         del self.table[index][i]
        #         self.count -= 1  
        #         break

        # new version
        i = 0
        while i < self.size:
            index = (self.hash_function(key) + i * self.hash_function_2(key)) % self.size
            if self.table[index] and self.table[index][0] == key:
                self.table[index] = None  # Mark as deleted
                self.count -= 1
                break
            i += 1
    
    def resize(self):
        # old version
        # new_size = self.size * 2  # Double the size
        # new_table = [[] for i in range(new_size)]  # Create a new table

        # # Rehash all items into the new table
        # for bucket in self.table:
        #     for key, value in bucket:
        #         new_index = key % new_size
        #         new_table[new_index].append((key, value))
        
        # self.size = new_size  
        # self.table = new_table 
        # print(f"Resized hash table to new size: {self.size}")

        # new version
        new_size = self.size * 2  # Double the size
        new_table = [[] for i in range(new_size)]

        # Rehash all items into the new table
        for item in self.table:
            if item:
                key, value = item
                i = 0
                while i < new_size:
                    new_index = (key + i * (7 - (key % 7))) % new_size
                    if new_table[new_index] is None:
                        new_table[new_index] = (key, value)
                        break
                    i += 1
        
        self.size = new_size  
        self.table = new_table 
        print(f"Resized hash table to new size: {self.size}")
class HilbertsHotel:
    def __init__(self, size: int = 50):
        self.avl_tree = AVLTree()
        self.root = None
        self.hash_table = HashTable(size)
        self.max_room_number = 0
        self.collisions = 0

    def calculate_room_number(self, fleet: int, ship: int, bus: int, guest: int):
        return ((fleet+1) ** 7) * ((ship+1)**5) * ((bus+1) ** 3) * ((guest+1) ** 2)
    
    
    @exec_time
    def add_room(self, fleet: int, ship: int, bus: int, guest: int):
        room_number = self.calculate_room_number(fleet, ship, bus, guest)
        
        # print("Room Number:", room_number)
        # if self.hash_table.search(room_number) is None:
        #     self.hash_table.insert(room_number, (fleet, ship, bus, guest))
        #     self.root = self.avl_tree.insert(self.root,room_number)
        #     self.max_room_number = max(self.max_room_number, room_number)

        if self.hash_table.search(room_number) is None:
            self.hash_table.insert(room_number, (fleet, ship, bus, guest))
            self.root = self.avl_tree.insert(self.root, room_number)
            self.max_room_number = max(self.max_room_number, room_number)
        else:
            self.collisions += 1
            for i in range(1,self.hash_table.size):
                new_room_number = (room_number + (i**2))%self.hash_table.size
                if self.hash_table.search(new_room_number) is None:
                    self.hash_table.insert(new_room_number, (fleet, ship, bus, guest))
                    self.root = self.avl_tree.insert(self.root, new_room_number)
                    self.max_room_number = max(self.max_room_number, new_room_number)
                    room_number = new_room_number
                    break
            if self.collisions >= 10:
                self.collisions = 0
                self.hash_table.resize()

        return room_number

    @exec_time
    def remove_room(self, room_number: int):
        if self.hash_table.search(room_number):
            self.hash_table.remove(room_number)

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
        room_count = sum(len(bucket) for bucket in self.hash_table.table)
        return total_rooms - room_count

    @exec_time
    def save_to_file(self, file_name: str):
        result = []
        for bucket in self.hash_table.table:
            for room_number, value in bucket:
                result.append((room_number, *value))
        df = pd.DataFrame(result, columns=['Room Number', 'Fleet', 'Ship', 'Bus', 'Guest'])
        try:
            df.to_csv(file_name, index=False)
            print(f"Data successfully saved to {file_name}")
        except Exception as e:
            print(f"Failed to save data: {e}")


    
    def memory_usage(self):
        tree_size = self.calculate_tree_size(self.root)
        return sys.getsizeof(self.hash_table) + tree_size

HilbertsHotel = HilbertsHotel(100)

for i in range(10) :
    for j in range(3):
        HilbertsHotel.add_room(0,0,j,i)

sorted_rooms = HilbertsHotel.sort_rooms()
print("Sorted Rooms:", sorted_rooms)

sorted_rooms = HilbertsHotel.sort_rooms()

print("Sorted Rooms:", sorted_rooms)

# HilbertsHotel.add_room(2, 1, 1, 1)

print("sorted_rooms:", HilbertsHotel.sort_rooms())

print("number of empty room:", HilbertsHotel.empty_rooms())

print("Find room 32:", HilbertsHotel.find_room(32))

HilbertsHotel.save_to_file("./data_hotel_rooms.csv")

print("Memory Usage:", HilbertsHotel.memory_usage())