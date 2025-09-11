total = 0;
count = 0;
user_num = input("输入或输入q退出并返回结果：");
while user_num != "q":
    total = total + float(user_num);
    count += 1;
    user_num = input("输入或输入q退出并返回结果：");
Average = total / count;
if count != 0:
    print(Average);
else:
    print("bye");

