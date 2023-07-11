def calculate_class_allocation(num_students):
    # Determine the number of classes required
    num_classes = (num_students // 30) + 1 if num_students % 30 != 0 else num_students // 30
    # Determine the approximate number of students per class
    students_per_class = num_students // num_classes
    # Determine the remaining students to be allocated
    remaining_students = num_students % num_classes

    # Create the class allocation dictionary
    class_allocation = {}
    for i in range(1, num_classes + 1):
        if i <= remaining_students:
            class_allocation[f"Class_{i}"] = students_per_class + 1
        else:
            class_allocation[f"Class_{i}"] = students_per_class

    # Print the proposed allocation and the class allocation dictionary
    print(f"Proposed Allocation: {num_classes} classes")
    print(class_allocation)

#trying out the function
print(calculate_class_allocation(31))
print(calculate_class_allocation(59))
print(calculate_class_allocation(87))


# The calculate_class_allocation function takes the number of students as input.
#
# The variable num_classes is determined to find the minimum number of classes required.
# It is calculated based on the number of students, considering a maximum class size of 30.
# If there are remaining students after evenly distributing them into 30-student classes, an extra class is added.
#
# The variable students_per_class approximates the number of students per class by dividing the total number of
# students by the number of classes.
#
# The variable remaining_students calculates the number of students that cannot be evenly distributed among
# the classes.
#
# The class_allocation dictionary is created to store the allocation of students for each class.
#
# A loop iterates from 1 to num_classes to allocate students to each class. It checks if the current
# class index is within the range of remaining students. If so, it assigns an additional student to that class,
# making the distribution as even as possible.
#
# Finally, the function prints the proposed allocation by displaying the number of classes. It then prints
# the class_allocation dictionary, which shows the number of students allocated to each class.