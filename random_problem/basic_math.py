# ত োমাকে cubeNumber() নামে একটা function দে ওয়া হয়ে ছে । functionটা একটা input নাম্বার নি বে ।
# Task:
# 1. input নাম্বারটাকে cube করে result টা রি টার্ন করবে ফাংশন থে কে ।
# 2. Bonus: ইনপুট হি সে বে number টাইপ এর পরি বর্তে অন্য কি ছুদি লে তুমি একটা মি নি ংফুল মে সে জ রি টার্ন
# করে দি বে ফাংশন থে কে ।
import math
def cube_number(number):
    if(type(number) is not int or number <= 0):
        return "Invalid Number.. Please Input a positive Integer"
    return round(math.pow(number,3))


print(cube_number("10"))