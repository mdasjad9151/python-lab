# 1. Write a program to generate a 6-digit random secure OTP.
import random
import math

def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP

print("Generated OTP:", generate_otp())
