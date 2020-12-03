import doctest
import socket


class Person:

    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        '''
        >>> person = Person('hello', 21, 'male')
        >>> str(person)
        I am hello,21 years old
        '''
        return "I am {},{} years old".format(self.name, self.age)

    def __repr__(self) -> str:
        return "I am {},{} years old".format(self.name, self.age)

    def __eq__(self, o: 'Person') -> bool:
        return self.name == o.name

    def introduceSelf(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def sayHello(self) -> None:
        print("Hello")


def socket_test() -> None:
    s = socket.socket()         # 创建 socket 对象
    host = socket.gethostname()  # 获取本地主机名
    port = 8084                # 设置端口
    s.bind((host, port))        # 绑定端口

    s.listen(5)                 # 等待客户端连接
    while True:
        c, addr = s.accept()     # 建立客户端连接
        print('连接地址：', addr)
        c.send('欢迎访问菜鸟教程！')
        c.close()                # 关闭连接


def main():
    socket_test()


if __name__ == "__main__":
    main()
