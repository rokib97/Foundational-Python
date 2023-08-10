# তুমি দ োকানে একটা চি প্স কি নতে গে লা কি ছুখুচরা টাকার ন োট নি য়ে । একটা canPay() নামে function বানাও যে টা
# ২টা ইনপুট নে ইঃ একটা array, এবং আরে কটা number।
# 1. Array এর প্রত্যে ক টা element ত োমার খুচরা টাকা বঝু াই
# 1 taka
# 2 taka
# 5 taka
# 2. second input টা বঝু াই চি প্স এর দাম।
# Task:
# 1. যদি খুচরা টাকা গুল ো য োগ করে চি প্স এর দামে র সমান বা তার বে শি হয় তাহলে boolean true রি টার্ন
# করবে
# 2. আর যদি ন োটগুল োর য োগফল চি প্স এর দামে র চে য়ে কম হয় সে ক্ষে ত্রে boolean false রি টার্ন করবে ।
# 3. Bonus: ইনপুট এর প্রথম উপাদান empty অ্যারে কি না চে ক করবে । empty অ্যারে হলে মি নি ংফুল মে সে জ
# রি টার্ন করে দি বে ।

def can_pay(my_arr, number):
    if(not my_arr):
        return "Invalid Input"
    sum = 0
    for money in my_arr:
        sum += money
    if(sum >= number):
        return True
    else:
        return False
print(can_pay([1,5,5],10))