# ত োমাকে একটা ফাংশন লি খতে হবে যার নাম হবে sortMaker()। এই ফাংশনে র parameter হবে একটি array এবং
# এই array তে সবসময় দইুটি উপাদান থাকবে ।
# Task:
# 1. যদি অ্যারে র দইুটি উপাদান পজি টিভ সংখ্যা হয় সে ক্ষে ত্রে তুমি অ্যারে টিকে বড় ো থে কে ছ োট ক্রমে সাজি য়ে রি টার্ন
# করবে ।
# 2. যদি দইুটি উপাদান একই হয় সে ক্ষে ত্রে তুমি এই স্ট্রি ং রি টার্ন করবে ঃ “equal”
# 3. Bonus: যদি অ্যারে র যে ক োন ো একটি উপাদান নে গে টিভ সংখ্যা হয় সে ক্ষে ত্রে তুমি রি টার্ন করবে “Invalid Input”

def sortMaker(my_arr):
    if(type(my_arr) is not list):
        return "Enter list only!"
    first_element = my_arr[0]
    for element in my_arr:
        if element < 0:
            return "Invalid"
        if element != first_element:
            my_arr.sort(reverse=True)
            return my_arr
        
    return "equal"
    
        
print(sortMaker([-77,5]))