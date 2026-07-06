# Banking System (Python Tkinter)

A simple **Banking System** application developed using **Python** and **Tkinter**. This project provides a graphical user interface (GUI) for performing basic banking operations such as creating accounts, depositing money, withdrawing money, transferring funds, checking balances, and viewing account details.

## Features

- Secure Admin Login
- Create Bank Account
- Deposit Money
- Withdraw Money
- Transfer Money Between Accounts
- Check Account Balance
- View All Accounts
- Simple and User-Friendly GUI

## Technologies Used

- Python 3.x
- Tkinter (GUI)
- Object-Oriented Programming (OOP)

## Project Structure

```
banking_system/
│── main.py          # Application entry point
│── gui.py           # GUI implementation
│── bank.py          # Banking operations
│── account.py       # Bank account class
└── README.md        # Project documentation
```

## Requirements

- Python 3.8 or above

Tkinter is included with the standard Python installation.

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/banking-system.git
```

2. Navigate to the project directory

```bash
cd banking-system
```

3. Run the application

```bash
python main.py
```

## Login Credentials

| Username | Password |
|----------|----------|
| admin | admin123 |

## Functionalities

### Create Account
- Enter Account Number
- Enter Account Holder Name
- Enter Initial Balance

### Deposit
- Deposit money into an existing account.

### Withdraw
- Withdraw money from an account if sufficient balance is available.

### Transfer
- Transfer money from one account to another.

### Balance Inquiry
- Display the current balance of an account.

### View Accounts
- Display all account details in a table.

## Project Architecture

```
main.py
    │
    ▼
BankGUI (gui.py)
    │
    ▼
Bank (bank.py)
    │
    ▼
BankAccount (account.py)
```

## Files Description

### main.py
Starts the application by creating the Tkinter window and launching the GUI. :contentReference[oaicite:0]{index=0}

### gui.py
Contains the graphical user interface including login, menus, and banking operations. :contentReference[oaicite:1]{index=1}

### bank.py
Implements the banking logic including account creation, deposits, withdrawals, transfers, and balance checking. :contentReference[oaicite:2]{index=2}

### account.py
Defines the `BankAccount` class and account-related operations such as deposit, withdraw, and retrieving account details. :contentReference[oaicite:3]{index=3}

## Future Improvements

- User Registration
- Database Integration (SQLite/MySQL)
- Transaction History
- Interest Calculation
- Password Encryption
- Account Deletion
- Input Validation
- Export Reports to PDF/Excel

## Author

**Bindhu Shree K. R**

## License

This project is created for educational purposes and is free to use and modify.# Banking-System
