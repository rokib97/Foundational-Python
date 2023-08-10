
# ত োমাকে একটা function দে ওয়া হবে called “findAddress()” যা ইনপুট হি সে বে একটা object নি বে । Object এর
# তি নটি property থাকবে ।
# Task:
# 1. ত োমাকে ১ম sample output এর format এ output return করতে হবে ।
# 2. Bonus: যদি object এর ক োন ো property missing থাকে সে ক্ষে ত্রে সে ই অংশটুকু double underscore
# দি য়ে replace হবে । (২য় output এর format এ )

def find_address(obj):
    my_list = []
    for key, _ in obj.items():
        my_list.append(obj[key])
    
    new_value = ", ".join([str(item) for item in my_list])
    return new_value
        


my_obj = {
    "street":10,
    "house":"15A",
    "society":"Earth Perfect"
}
print(find_address(my_obj))