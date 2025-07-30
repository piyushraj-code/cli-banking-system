
# 💰 Lena Dena Bank – Command Line Banking System

A simple, modular **Command-Line Banking System** built using **Python** and **Object-Oriented Programming (OOP)** concepts.

🔧 Perfect for beginners exploring Python, OOP, and modular coding.

---

## 📌 Features

- 🏦 **Account Creation** – Open accounts with an initial deposit  
- 💵 **Deposit & Withdraw** – Safely manage funds with balance validation  
- 📊 **Balance Inquiry** – Check your current account balance anytime  
- ⏱️ **User-Friendly Interface** – Interactive menu with countdown feedback  
- 🔒 **Data Privacy** – Encapsulated balance with private attributes

---

## 📁 Project Structure

```
banking_system/
│
├── account.py       # Account class: balance, deposit, withdraw, etc.
├── utils.py         # Utility functions (e.g., countdown timers)
├── interface.py     # CLI commands and menu interface
├── main.py          # Entry point: program flow and user input
└── README.md        # This file
```

---

## 📄 File Descriptions

### `account.py`
- Defines the `Account` class
- Implements:
  - Private `__balance` for encapsulation
  - `deposit()` and `withdraw()` methods
  - `getBalance()` method
  - Transaction success tracking

### `utils.py`
- Reusable helper functions:
  - `returnToHome()` – Displays countdown timer before returning to menu

### `interface.py`
- Menu and command system:
  - `commands()` function to print all available options

### `main.py`
- Core application logic:
  - Handles user input, account operations, and overall control flow

---

## ▶️ How to Run

1. **Clone the Repository**  
```bash
git clone https://github.com/piyushraj-code/cli-banking-system.git
cd cli-banking-system
```

2. **Run the Program**
```bash
python main.py
```

---

## 🧑‍💻 Usage Example

```text
Hello! Welcome to lena dena bank.
Enter 1 to create account
Enter 2 to check balance
Enter 3 to deposit
Enter 4 to withdraw
Enter 5 to exit

Enter your choice: 1
Enter users name: John Doe
Enter how much do you want to deposit: 1000

Account John with initial balance 1000 is created successfully.
```

---

## 🛠️ Code Highlights

- 📦 **Modular Design** – Organized into logical files
- 🔐 **Encapsulation** – Private `__balance` variable
- 📋 **Input Validation** – Checks account existence and valid transactions
- ✅ **User Feedback** – Clear messages and countdown animations

---

## 💡 Key Concepts Demonstrated

| Concept               | Description                                           |
|----------------------|-------------------------------------------------------|
| ✅ OOP                | Classes, methods, and encapsulation                  |
| ✅ CLI Interaction    | Interactive command-line user interface              |
| ✅ Modular Code       | Separated logic into manageable Python files         |
| ✅ Error Handling     | Checks for valid input and transaction safety        |
| ✅ State Tracking     | `transactionSuccess` flags for withdraw logic        |

---

## 🌱 Future Enhancements

- 📜 Transaction history
- 🔐 PIN/password-based login
- 💸 Account-to-account transfer
- 📂 File-based data storage (JSON/CSV)
- 📈 Interest calculation on balances
- ❌ Account deletion functionality

---

## 🤝 Contributing

This is an open-source learning project!  
Feel free to **fork** the repository, enhance it with new features, and create pull requests.

---

## 📜 License

This project is for **educational purposes** and is not intended for real-world financial applications.

---

> Built with ❤️ for learning Python and software design.
