import numpy as np

def print_students():
    """
    Print dtype students to console.

    Parameters: None

    Returns: Null
    """

    students = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
    print(f"students type: {students}")
    a = np.array([('Smith', 21, 50),('John', 18, 75)], dtype = students) 
    print(f"students array shape: {a.shape}")
    print(f"students array data: {a}")
    print(f"first students data: {a[0]}")
    print(f"all students name: {a['name']}")
    print(f"last students name: {a[-1]['name']}")
    print(f"data of student has marks<50: {a[a['marks']<=50]}")
    print(f"name of student has age<20: {a[a['age']<20]['name']}")

    pass

print_students()


