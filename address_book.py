# 初始化一个空的通讯录字典
contacts = {
    "李明轩": "13812345678",
    "王雨桐": "13987654321",
    "赵子涵": "13765432109",
    "陈思妍": "13698765432",
    "刘浩然": "13511223344"
}

print("--- 欢迎使用简易通讯录 ---")
while True:
    print("\n请选择操作：")
    print("1. 添加联系人")
    print("2. 查找联系人")
    print("3. 删除联系人")
    print("4. 查看所有联系人")
    print("5. 退出")
    
    choice = input("请输入数字 (1-5): ").strip() # 去除用户输入的空格

    # 1. 添加
    if choice == '1':
        name = input("姓名: ").strip()
        phone = input("电话: ").strip()
        if name in contacts:
            print(f"联系人 {name} 已存在！")
        else:
            contacts[name] = phone
            print(f"成功添加 {name}。")

    # 2. 查找
    elif choice == '2':
        name = input("请输入要查找的姓名: ").strip()
        if name in contacts:
            print(f"{name} 的电话是: {contacts[name]}")
        else:
            print("查无此人。")

    # 3. 删除
    elif choice == '3':
        name = input("请输入要删除的姓名: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"已删除 {name}。")
        else:
            print("查无此人，无法删除。")

    # 4. 查看所有
    elif choice == '4':
        if not contacts:
            print("通讯录是空的。")
        else:
            print("--- 通讯录列表 ---")
            # 遍历字典的键和值
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    # 5. 退出
    elif choice == '5':
        print("再见！")
        break
    
    else:
        print("输入无效，请输入 1-5。")