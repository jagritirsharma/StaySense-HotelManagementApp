# StaySense-HotelManagementApp

## Description

The Hotel Management System is a comprehensive Python-based application designed to streamline hotel operations. This system integrates MySQL for database management and provides functionalities for managing customer information, room bookings, and generating reports. The application features a user-friendly graphical interface built using Tkinter, enabling easy interaction and management of hotel data.

## Key Features

- **Customer Management**: Add, update, delete, and search customer details.
- **Room Booking**: Manage room bookings for customers, including availability tracking.
- **Reports Generation**: Create and export reports related to customers and bookings.
- **User Authentication**: Secure login and registration for users.
- **Interactive Dashboard**: Simple navigation with buttons for each function.

## Technology Stack

- **Backend**: Python
- **Database**: MySQL
- **GUI**: Tkinter

## Installation

### Create and Set Up the Database

1. Use the provided `management.sql` script to create the necessary tables in a MySQL database.
2. Update your database credentials in the `config.py` file.

### Install Python Dependencies

Run the following command to install the required packages:

```bash
pip install mysql-connector-python Pillow
```

### Run the Application

Execute the `hotel.py` script to start the application:

```bash
python hotel.py
```

## Database Schema

The system includes the following key tables:

- **Customer Table**: Stores customer information, including ID, name, mother’s name, gender, contact details, nationality, and address.
- **Details Table**: Manages room details, including floor, room number, and room type.
- **Register Table**: Handles user registration, including first name, last name, contact, email, security questions, and passwords.
- **Room Table**: Records room booking details, including contact, check-in/check-out dates, room type, meal preference, and number of days booked.

## Example Use Case

- **User Registration**: New users can register and log in to access the system.
- **Manage Customers**: Users can add, update, or delete customer records.
- **Book Rooms**: Users can view available rooms and make bookings for customers.

## Contribution

Contributions to improve and extend the system are welcome. Please refer to the contribution guidelines in the repository for more details.
