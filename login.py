import hashlib
import getpass

if __name__ == '__main__':

    print("这是一个简单的登录系统，作者为marv1ee")
    info = {}  # 初始化一个字典
    try:  # 目录内不存在logon时的避免报错
        with open("logon", "r", encoding="utf-8") as fp:
            info = fp.read()
            info = dict(eval(info))  # 强转字典数据类型
    except FileNotFoundError:
        print("没有找到logon，请先执行注册操作")
    while True:
        print("1.注册\n"
              "2.登录")
        sel = input()
        if sel == "1":
            while True:
                username = input("请输入用户名：")
                for i in info.keys():
                    if username == i:
                        print("该用户名已存在")
                        break
                else:
                    password = getpass.getpass("请输入密码：")
                    hax = hashlib.md5()
                    hax.update(password.encode(encoding="utf-8"))

                    info1 = {username: hax.hexdigest()}  # 将用户名和密码分别存入字典的键和值
                    info.update(info1)

                    with open("logon", "w", encoding="utf-8") as fp:
                        fp.write(str(info))
                    print("注册成功")
                    break
        elif sel == "2":
            print("请输入用户名和密码以登录")
            username = input("请输入用户名：")
            password = getpass.getpass("请输入密码：")

            hax = hashlib.md5()
            hax.update(password.encode(encoding="utf-8"))

            if info.get(username) == hax.hexdigest():  # 如果键和对应的值都存在则登陆成功
                print("登陆成功")
            else:
                print("用户名或密码错误")

        else:
            print("输入错误")
