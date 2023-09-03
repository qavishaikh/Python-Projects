# import os

# Dictionary to store attendance records
attendance_records = {}

def mark_attendance():
    date = input("Enter the date (YYYY-MM-DD): ")
    while True:
        roll_number = input("Enter Roll Number (or 'q' to exit): ")
        if roll_number == 'q':
            break
        if roll_number not in attendance_records:
            attendance_records[roll_number] = {}
        if date not in attendance_records[roll_number]:
            attendance_records[roll_number][date] = 'Present'
        else:
            print("Attendance already marked for this date.")

def view_attendance():
    roll_number = input("Enter Roll Number to view attendance: ")
    if roll_number in attendance_records:
        print(f"Attendance for {roll_number}:")
        for date, status in attendance_records[roll_number].items():
            print(f"{date}: {status}")
    else:
        print("No attendance records found for this Roll Number.")

def main_menu():
    while True:
        print("\nAttendance Management System")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
