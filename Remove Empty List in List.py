test_list = [4,5,6,[],3,[],9]
print("The original list is: " + str(test_list))
res = list(filter(None, test_list))
print("List after empty list removal : " + str(res))
