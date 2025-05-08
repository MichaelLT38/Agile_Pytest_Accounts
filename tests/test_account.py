import ctypes
import pytest
import os

# Load the shared library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../cmake-build-debug/account.so"))

# Define the Account class interface
class Account(ctypes.Structure):
    _fields_ = [("_balance", ctypes.c_double)]

# Set up function prototypes
lib._ZNK7Account10getBalanceEv.argtypes = [ctypes.POINTER(Account)]
lib._ZNK7Account10getBalanceEv.restype = ctypes.c_double
lib._ZN7AccountC1Ev.argtypes = [ctypes.POINTER(Account)]
lib._ZN7Account7depositEd.argtypes = [ctypes.POINTER(Account), ctypes.c_double]
lib._ZN7Account7depositEd.restype = ctypes.c_bool
lib._ZN7Account8withdrawEd.argtypes = [ctypes.POINTER(Account), ctypes.c_double]
lib._ZN7Account8withdrawEd.restype = ctypes.c_bool

@pytest.fixture
def account():
    # Create an Account instance
    acc = Account()
    lib._ZN7AccountC1Ev(ctypes.byref(acc))
    return acc

def test_initial_balance(account):
    balance = lib._ZNK7Account10getBalanceEv(ctypes.byref(account))
    assert balance == 0.0, "Initial balance should be 0"

def test_valid_deposit(account):
    result = lib._ZN7Account7depositEd(ctypes.byref(account), 100.0)
    balance = lib._ZNK7Account10getBalanceEv(ctypes.byref(account))
    assert result == True, "Deposit should succeed"
    assert balance == 100.0, "Balance should be 100 after deposit"

def test_negative_deposit(account):
    result = lib._ZN7Account7depositEd(ctypes.byref(account), -50.0)
    balance = lib._ZNK7Account10getBalanceEv(ctypes.byref(account))
    assert result == False, "Negative deposit should fail"
    assert balance == 0.0, "Balance should remain 0"

def test_valid_withdrawal(account):
    lib._ZN7Account7depositEd(ctypes.byref(account), 100.0)
    result = lib._ZN7Account8withdrawEd(ctypes.byref(account), 50.0)
    balance = lib._ZNK7Account10getBalanceEv(ctypes.byref(account))
    assert result == True, "Withdrawal should succeed"
    assert balance == 50.0, "Balance should be 50 after withdrawal"

def test_over_withdrawal(account):
    lib._ZN7Account7depositEd(ctypes.byref(account), 50.0)
    result = lib._ZN7Account8withdrawEd(ctypes.byref(account), 100.0)
    balance = lib._ZNK7Account10getBalanceEv(ctypes.byref(account))
    assert result == False, "Over-withdrawal should fail"
    assert balance == 50.0, "Balance should remain 50"

def test_negative_withdrawal(account):
    lib._ZN7Account7depositEd(ctypes.byref(account), 100.0)
    result = lib._ZN7Account8withdrawEd(ctypes.byref(account), -20.0)
    balance = lib._ZNK7Account10getBalanceEv(ctypes.byref(account))
    assert result == False, "Negative withdrawal should fail"
    assert balance == 100.0, "Balance should remain 100"