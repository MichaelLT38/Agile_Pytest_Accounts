#include <iostream>
#include <string>
#include "../include/Account.h"

int main() {
    Account account;
    std::string command;
    double amount;

    std::cout << "Bank Account CLI (commands: deposit <amount>, withdraw <amount>, balance, exit)\n";

    while (true) {
        std::cout << "> ";
        std::cin >> command;

        if (command == "exit") {
            break;
        } else if (command == "deposit") {
            std::cin >> amount;
            if (account.deposit(amount)) {
                std::cout << "Deposited $" << amount << ". New balance: $" << account.getBalance() << "\n";
            } else {
                std::cout << "Invalid deposit amount.\n";
            }
        } else if (command == "withdraw") {
            std::cin >> amount;
            if (account.withdraw(amount)) {
                std::cout << "Withdrew $" << amount << ". New balance: $" << account.getBalance() << "\n";
            } else {
                std::cout << "Invalid withdrawal amount or insufficient funds.\n";
            }
        } else if (command == "balance") {
            std::cout << "Current balance: $" << account.getBalance() << "\n";
        } else {
            std::cout << "Unknown command.\n";
        }
    }

    return 0;
}