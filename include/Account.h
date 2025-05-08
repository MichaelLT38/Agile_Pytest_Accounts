//
// Created by mltac on 5/8/2025.
//

#ifndef ACCOUNT_H
#define ACCOUNT_H

class Account {
public:
    Account();
    bool deposit(double amount);
    bool withdraw(double amount);
    double getBalance() const;

private:
    double balance;
};

#endif // ACCOUNT_H
