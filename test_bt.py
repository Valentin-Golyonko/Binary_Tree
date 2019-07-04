from binary_tree import Student, Tree


def test():
    """
    >>> students = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Elijah", "Sophia", "Oliver", \
    "Isabella", "Lucas", "Amelia", "Mason", "Mia", "Logan", "Charlotte", \
    "Ethan", "Harper", "Aiden", "Aria", "James"]

    >>> test_root = Student(students[0], 5)
    >>> test_tree = Tree(test_root)

    >>> test_tree.add(Student(students[1], 6.0))

    >>> test_tree.find(6, test_root)
    ('Liam', 6.0)

    >>> test_tree.add(Student(students[2], 5.5))
    >>> test_tree.add(Student(students[3], 4.1))
    >>> test_tree.add(Student(students[4], 3.7))
    >>> test_tree.add(Student(students[5], 6.6))
    >>> test_tree.add(Student(students[6], 6.1))
    >>> test_tree.add(Student(students[7], 7.3))
    >>> test_tree.add(Student(students[8], 4.9))
    >>> test_tree.add(Student(students[9], 8.2))
    >>> test_tree.add(Student(students[10], 5.2))
    >>> test_tree.add(Student(students[11], 1.5))
    >>> test_tree.add(Student(students[12], 2.0))
    >>> test_tree.add(Student(students[13], 5.0))
    >>> test_tree.add(Student(students[14], 6.0))
    >>> test_tree.add(Student(students[14], 6.0))
    >>> test_tree.add(Student(students[15], 4.8))
    >>> test_tree.add(Student(students[16], 4.0))
    >>> test_tree.add(Student(students[17], 8.0))
    >>> test_tree.add(Student(students[18], 7.3))

    >>> test_tree.__root_saved__ = test_root
    >>> test_tree.print_tree(test_root)
    >>> for i in test_tree.__names__: print(i)
    ['Olivia', 5, 0, 0, 0, '']
    ['Liam', 6.0, 1, -1, 0, 'r']
    ['Elijah', 6.6, 2, -2, 1, 'r']
    ['Oliver', 7.3, 3, -3, 2, 'r']
    ['Lucas', 8.2, 4, -4, 3, 'r']
    ['Aiden', 8.0, 3, -5, 4, 'r']
    ['Aria', 7.3, 2, -4, 3, 'r']
    ['Sophia', 6.1, 1, -3, 2, 'r']
    ['Emma', 5.5, 0, -2, 1, 'r']
    ['Charlotte', 6.0, 1, -3, 0, 'r']
    ['Charlotte', 6.0, 0, -4, 1, 'r']
    ['Amelia', 5.2, -1, -3, 0, 'r']
    ['Noah', 4.1, -1, -1, 0, 'l']
    ['Isabella', 4.9, 0, -2, -1, 'l']
    ['Logan', 5.0, 1, -3, 0, 'l']
    ['Ethan', 4.8, -1, -3, 0, 'l']
    ['Ava', 3.7, -2, -2, -1, 'l']
    ['Harper', 4.0, -1, -3, -2, 'l']
    ['Mason', 1.5, -3, -3, -2, 'l']
    ['Mia', 2.0, -2, -4, -3, 'l']
    >>> test_tree.__names__.clear()
    >>> test_tree.__root_saved__ = 0

    >>> test_tree.find(7.3, test_root)
    ('Oliver', 7.3)

    >>> test_tree.find(1.5, test_root)
    ('Mason', 1.5)

    >>> test_tree.find_all(6, test_root)
    >>> for i in test_tree.arr_find_all: print(i)
    ['Liam', 6.0]
    ['Charlotte', 6.0]
    ['Charlotte', 6.0]
    >>> test_tree.arr_find_all.clear()

    >>> test_tree.dell(6.6, test_root)
    (None, 0)
    >>> test_tree.arr_dell[0]
    ['Elijah', 6.6]
    >>> test_tree.arr_dell.clear()

    >>> test_tree.dell(1.5, test_root)
    (None, 0)
    >>> test_tree.arr_dell[0]
    ['Mason', 1.5]
    >>> test_tree.arr_dell.clear()

    >>> test_tree.dell(2, test_root)
    (None, 0)
    >>> test_tree.arr_dell[0]
    ['Mia', 2.0]
    >>> test_tree.arr_dell.clear()

    >>> test_tree.dell(1, test_root)
    (None, 0)
    >>> test_tree.arr_dell
    []
    >>> test_tree.arr_dell.clear()

    >>> test_tree.dell(6.0, test_root, True)
    (None, 0)
    >>> for i in test_tree.arr_dell: print(i)
    ['Charlotte', 6.0]
    ['Charlotte', 6.0]
    ['Liam', 6.0]
    >>> test_tree.arr_dell.clear()

    >>> test_tree.__root_saved__ = test_root
    >>> test_tree.print_tree(test_root)
    >>> for i in test_tree.__names__: print(i)
    ['Olivia', 5, 0, 0, 0, 'l']
    ['Emma', 5.5, 1, -1, 0, 'r']
    ['Sophia', 6.1, 2, -2, 1, 'r']
    ['Oliver', 7.3, 3, -3, 2, 'r']
    ['Lucas', 8.2, 4, -4, 3, 'r']
    ['Aiden', 8.0, 3, -5, 4, 'r']
    ['Aria', 7.3, 2, -4, 3, 'r']
    ['Amelia', 5.2, 0, -2, 1, 'r']
    ['Noah', 4.1, -1, -1, 0, 'l']
    ['Isabella', 4.9, 0, -2, -1, 'l']
    ['Logan', 5.0, 1, -3, 0, 'l']
    ['Ethan', 4.8, -1, -3, 0, 'l']
    ['Ava', 3.7, -2, -2, -1, 'l']
    ['Harper', 4.0, -1, -3, -2, 'l']
    >>> test_tree.__names__.clear()

    >>> test_tree.print_empty_leaves(test_root)
    >>> for i in test_tree.__empty_leaves__: print(i)
    ['Aiden', 8.0]
    ['Aria', 7.3]
    ['Amelia', 5.2]
    ['Logan', 5.0]
    ['Ethan', 4.8]
    ['Harper', 4.0]
    >>> test_tree.__empty_leaves__.clear()

    # TEST ERRORS
    >>> test_tree.dell(-1, test_root, True)
    (None, 0)
    >>> bool(test_tree.arr_dell)
    False

    >>> test_tree.dell(-1, test_root, True)
    (None, 0)
    >>> test_tree.arr_dell[0]
    Traceback (most recent call last):
        ...
    IndexError: list index out of range

    >>> test_tree.find_all(-1, test_root)
    >>> bool(test_tree.arr_find_all)
    False

    >>> test_tree.find_all(-1, test_root)
    >>> test_tree.arr_find_all[0]
    Traceback (most recent call last):
        ...
    IndexError: list index out of range

    >>> test_tree.find(-1, test_root)

    >>> bool(test_tree.__names__)
    False
    """


if __name__ == "__main__":
    test()
