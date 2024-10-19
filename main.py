import pandas as pd
import sys
import time
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
            room_number = result
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
            while self.hash_table.search(room_number + i**2) is not None:
                i += 1
            self.hash_table.insert(room_number + i**2, (fleet, ship, bus, guest))
            self.root = self.avl_tree.insert(self.root, room_number + i**2)
            self.max_room_number = max(self.max_room_number, room_number + i**2)
        return room_number

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
        room_count = sum(1 for slot in self.hash_table.table if slot is not None)
        return total_rooms - room_count

    @exec_time
    def save_to_file(self, file_name: str):
        result = []
        data = self.hash_table.table
        for slot in data:
            if slot is not None:
                slot.inorder_traversal(slot.root, result)


        df = pd.DataFrame(result, columns=['Room Number', 'Room Details'])

        try:
            df.to_csv(file_name, index=False)
            print(f"Data successfully saved to {file_name}")
        except Exception as e:
            print(f"Failed to save data: {e}")


    def memory_usage(self):
        return sys.getsizeof(self.hash_table) + sys.getsizeof(self.root)

HilbertsHotel = HilbertsHotel(100)

initialguest = int(input("Enter the guest number: "))
for i in range(initialguest):
    HilbertsHotel.add_room(0,0,0,i)
print(HilbertsHotel.sort_rooms())
HilbertsHotel.save_to_file("rooms.csv")