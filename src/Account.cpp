//
// Created by mltac on 5/8/2025.
//

#include "../include/Account.h"

Account::Account() : balance(0.0) {}

bool Account::deposit(double amount) {
    if (amount <= 0) {
        return false; // Negative or zero deposits not allowed
    }
    balance += amount;
    return true;
}

bool Account::withdraw(double amount) {
    if (amount <= 0 || amount > balance) {
        return false; // Negative withdrawals or overdrafts not allowed
    }
    balance -= amount;
    return true;
}

double Account::getBalance() const {
    return balance;
}