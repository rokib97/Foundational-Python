
# তোমাকে একটা function দেওয়া হবে called “findAddress()” যা ইনপুট হিসেবে একটা object নি বে । Object এর
# তি নটি property থাকবে ।
# Task:
# 1. ত োমাকে ১ম sample output এর format এ output return করতে হবে ।
# 2. Bonus: যদি object এর ক োন ো property missing থাকে সে ক্ষে ত্রে সে ই অংশটুকু double underscore
# দি য়ে replace হবে । (২য় output এর format এ )

def find_address(input_dict):
    
    output_parts = []
    for key in ["street", "house", "society"]:
        value = input_dict.get(key)
        if value is None:
            value = "__"
        output_parts.append(str(value))

    output_string = ", ".join(output_parts)
    return output_string
        


my_obj = {
    "street":10,
    "house":"15A",
    "society":"Earth Perfect"
}
print(find_address(my_obj))