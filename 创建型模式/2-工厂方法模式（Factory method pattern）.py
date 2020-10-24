# -*- coding:utf-8 -*-


"""

模式定义:
工厂方法模式(Factory Method Pattern)又称为工厂模式，也叫虚拟构造器(Virtual Constructor)模式或者多态工厂(Polymorphic Factory)模式，
它属于类创建型模式。在工厂方法模式中，工厂父类负责定义创建产品对象的公共接口，而工厂子类则负责生成具体的产品对象，这样做的目的是将产品类的实例
化操作延迟到工厂子类中完成，即通过工厂子类来确定究竟应该实例化哪一个具体产品类。


工厂方法模式包含如下角色：
Product：抽象产品
ConcreteProduct：具体产品
Factory：抽象工厂
ConcreteFactory：具体工厂


总结
- 工厂方法模式又称为工厂模式，它属于类创建型模式。在工厂方法模式中，工厂父类负责定义创建产品对象的公共接口，而工厂子类则负责生成具体的产品
对象，这样做的目的是将产品类的实例化操作延迟到工厂子类中完成，即通过工厂子类来确定究竟应该实例化哪一个具体产品类。
- 工厂方法模式包含四个角色：抽象产品是定义产品的接口，是工厂方法模式所创建对象的超类型，即产品对象的共同父类或接口；具体产品实现了抽象产品
接口，某种类型的具体产品由专门的具体工厂创建，它们之间往往一一对应；抽象工厂中声明了工厂方法，用于返回一个产品，它是工厂方法模式的核心，任
何在模式中创建对象的工厂类都必须实现该接口；具体工厂是抽象工厂类的子类，实现了抽象工厂中定义的工厂方法，并可由客户调用，返回一个具体产品类
的实例。
- 工厂方法模式是简单工厂模式的进一步抽象和推广。由于使用了面向对象的多态性，工厂方法模式保持了简单工厂模式的优点，而且克服了它的缺点。在工
厂方法模式中，核心的工厂类不再负责所有产品的创建，而是将具体创建工作交给子类去做。这个核心类仅仅负责给出具体工厂必须实现的接口，而不负责产
品类被实例化这种细节，这使得工厂方法模式可以允许系统在不修改工厂角色的情况下引进新产品。
- 工厂方法模式的主要优点是增加新的产品类时无须修改现有系统，并封装了产品对象的创建细节，系统具有良好的灵活性和可扩展性；其缺点在于增加新产
品的同时需要增加新的工厂，导致系统类的个数成对增加，在一定程度上增加了系统的复杂性。
- 工厂方法模式适用情况包括：一个类不知道它所需要的对象的类；一个类通过其子类来指定创建哪个对象；将创建对象的任务委托给多个工厂子类中的某一
个，客户端在使用时可以无须关心是哪一个工厂子类创建产品子类，需要时再动态指定。


"""

import math
from abc import ABCMeta, abstractmethod


class Graphical(metaclass=ABCMeta):

    @abstractmethod
    def Area(self, *args):
        pass


# 定义4个图形类，并且每一个图形都有一个可以计算面积的方法
class Circle(Graphical):
    def Area(self, radius):
        return math.pow(radius, 2) * math.pi


class Rectangle(Graphical):
    def Area(self, longth, width):
        return 2 * longth * width


class Triangle(Graphical):
    def Area(self, baselong, height):
        return baselong * height / 2


class Ellipse(Graphical):
    def Area(self, long_a, short_b):
        return long_a * short_b * math.pi


# =================================
# 定义创建对象的工厂接口，因为python中并没有接口的概念，所以，这里打算通过“类的继承”加以实现
class IFactory:  # 模拟接口
    def create_shape(self, name):  # 定义接口的方法，只提供方法的声明，不提供方法的具体实现
        pass


class CircleFactory(IFactory):  # 模拟类型实现某一个接口，实际上是类的继承
    def create_shape(self, name):  # 重写接口中的方法
        if name == 'Circle':
            return Circle()


class RectangleFactory(IFactory):  # 模拟类型实现某一个接口，实际上是类的继承
    def create_shape(self, name):  # 重写接口中的方法
        if name == 'Rectangle':
            return Rectangle()


class TriangleFactory(IFactory):  # 模拟类型实现某一个接口，实际上是类的继承
    def create_shape(self, name):  # 重写接口中的方法
        if name == 'Triangle':
            return Triangle()


class EllipseFactory(IFactory):  # 模拟类型实现某一个接口，实际上是类的继承
    def create_shape(self, name):  # 重写接口中的方法
        if name == 'Ellipse':
            return Ellipse()


if __name__ == '__main__':
    factory1 = CircleFactory()
    factory2 = RectangleFactory()
    factory3 = TriangleFactory()
    factory4 = EllipseFactory()

    circle = factory1.create_shape('Circle')
    circle_area = circle.Area(2)
    print(f'这是一个圆，它的面积是：{circle_area}')

    rectangle = factory2.create_shape('Rectangle')
    rectangle_area = rectangle.Area(2, 3)
    print(f'这是一个长方形，它的面积是：{rectangle_area}')

    triangle = factory3.create_shape('Triangle')
    triangle_area = triangle.Area(2, 3)
    print(f'这是一个三角形，它的面积是：{triangle_area}')

    ellipse = factory4.create_shape('Ellipse')
    ellipse_area = ellipse.Area(3, 2)
    print(f'这是一个椭圆，它的面积是：{ellipse_area}')



