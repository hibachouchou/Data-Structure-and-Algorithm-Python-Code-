#Array Algorithms
print("Array Algorithms")

class MyArray:
    def __init__(self):
        self.array = []

    # Accessing a value at a specific index
    def access_value(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            return "Index out of bounds"

    # Insertion  
    # Insertion at any index
    def insert_at_index(self, index, value):
        if 0 <= index <= len(self.array):
            self.array.insert(index, value)
        else:
            print("Index out of bounds")

    # Insertion at the start
    def insert_at_start(self, value):
        self.array.insert(0, value)

    # Insertion at the end
    def insert_at_end(self, value):
        self.array.append(value)

    # Deleting an element at a specific index
    def delete_at_index(self, index):
        if 0 <= index < len(self.array):
            del self.array[index]
        else:
            print("Index out of bounds")
# Deleting an element at the start
    def delete_at_start(self):
        if len(self.array) > 0:
            del self.array[0]
        else:
            print("Array is empty. Cannot delete from the beginning.")
# Deleting an element at the end
    def delete_at_end(self):
        if len(self.array) > 0:
            del self.array[-1]
        else:
            print("Array is empty. Cannot delete from the end.")


# Example usage:

