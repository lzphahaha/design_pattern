# -*- coding:utf-8 -*-


"""

模式定义:
抽象工厂模式(Abstract Factory Pattern)：提供一个创建一系列相关或相互依赖对象的接口，而无须指定它们具体的类。
抽象工厂模式又称为Kit模式，属于对象创建型模式。


抽象工厂模式包含如下角色：

AbstractFactory：抽象工厂
ConcreteFactory：具体工厂
AbstractProduct：抽象产品
Product：具体产品


工厂模式的退化:
当抽象工厂模式中每一个具体工厂类只创建一个产品对象，也就是只存在一个产品等级结构时，抽象工厂模式退化成工厂方法模式；
当工厂方法模式中抽象工厂与具体工厂合并，提供一个统一的工厂来创建产品对象，并将创建对象的工厂方法设计为静态方法时，
工厂方法模式退化成简单工厂模式。


总结:
- 抽象工厂模式提供一个创建一系列相关或相互依赖对象的接口，而无须指定它们具体的类。抽象工厂模式又称为Kit模式，属于
对象创建型模式。
- 抽象工厂模式包含四个角色：抽象工厂用于声明生成抽象产品的方法；具体工厂实现了抽象工厂声明的生成抽象产品的方法，生
成一组具体产品，这些产品构成了一个产品族，每一个产品都位于某个产品等级结构中；抽象产品为每种产品声明接口，在抽象产
品中定义了产品的抽象业务方法；具体产品定义具体工厂生产的具体产品对象，实现抽象产品接口中定义的业务方法。
- 抽象工厂模式是所有形式的工厂模式中最为抽象和最具一般性的一种形态。抽象工厂模式与工厂方法模式最大的区别在于，工厂
方法模式针对的是一个产品等级结构，而抽象工厂模式则需要面对多个产品等级结构。
- 抽象工厂模式的主要优点是隔离了具体类的生成，使得客户并不需要知道什么被创建，而且每次可以通过具体工厂类创建一个产
品族中的多个对象，增加或者替换产品族比较方便，增加新的具体工厂和产品族很方便；主要缺点在于增加新的产品等级结构很复
杂，需要修改抽象工厂和所有的具体工厂类，对“开闭原则”的支持呈现倾斜性。
- 抽象工厂模式适用情况包括：一个系统不应当依赖于产品类实例如何被创建、组合和表达的细节；系统中有多于一个的产品族，
而每次只使用其中某一产品族；属于同一个产品族的产品将在一起使用；系统提供一个产品类的库，所有的产品以同样的接口出现，
从而使客户端不依赖于具体实现。

"""


import math



# 定义一个“形状”的接口，里面定义一个面积的接口方法，只有方法的定义，并没有实现体
class IShape(object):
    def Area(self):
        pass


# 定义4个图形类，都是实现Ishape接口，并且每一个图形都有一个可以计算面积的方法，相当于重写接口方法
class Circle(IShape):
    def Area(self, radius):
        return math.pow(radius, 2) * math.pi


class Rectangle(IShape):
    def Area(self, longth, width):
        return 2 * longth * width


class Triangle(IShape):
    def Area(self, baselong, height):
        return baselong * height / 2


class Ellipse(IShape):
    def Area(self, long_a, short_b):
        return long_a * short_b * math.pi


# 定义一个“颜色”的接口，里面定义一个颜色名称的接口方法，只有方法的定义，并没有实现体
class IColor(object):
    def color(self):
        pass


# 定义3个颜色类，都是实现IColor接口，并且每一个图形都有一个可以获取颜色名称的方法，相当于重写接口方法
class Red(IColor):
    def color(self, name):
        print(f'我的颜色是：{name}')


class Blue(IColor):
    def color(self, name):
        print(f'我的颜色是：{name}')


class Black(IColor):
    def color(self, name):
        print(f'我的颜色是：{name}')



# 定义抽象工厂以及与每一个系列对应的工厂
class IFactory:  # 模拟接口
    def create_shape(self):  # 定义接口的方法，只提供方法的声明，不提供方法的具体实现
        pass

    def create_color(self):
        pass


# 创建形状这一个系列的工厂
class ShapeFactory(IFactory):  # 模拟类型实现某一个接口，实际上是类的继承
    def create_shape(self, name):  # 重写接口中的方法
        if name == 'Circle':
            return Circle()
        elif name == 'Rectangle':
            return Rectangle()
        elif name == 'Triangle':
            return Triangle()
        elif name == 'Ellipse':
            return Ellipse()
        else:
            return None


# 创建颜色这一个系列的工厂
class ColorFactory(IFactory):  # 模拟类型实现某一个接口，实际上是类的继承
    def create_color(self, name):  # 重写接口中的方法
        if name == 'Red':
            return Red()
        elif name == 'Blue':
            return Blue()
        elif name == 'Black':
            return Black()
        else:
            return None


# 定义产生工厂类的类——抽象工厂模式的核心所在
#定义一个专门产生工厂的类
class FactoryProducer:
    def get_factory(self,name):
        if name=='Shape':
            return ShapeFactory()
        elif name=='Color':
            return ColorFactory()
        else:
            return None


if __name__ == '__main__':
    factory_producer = FactoryProducer()
    shape_factory = factory_producer.get_factory('Shape')
    color_factory = factory_producer.get_factory('Color')
    # --------------------------------------------------------------

    circle = shape_factory.create_shape('Circle')
    circle_area = circle.Area(2)
    print(f'这是一个圆，它的面积是：{circle_area}')

    rectangle = shape_factory.create_shape('Rectangle')
    rectangle_area = rectangle.Area(2, 3)
    print(f'这是一个长方形，它的面积是：{rectangle_area}')

    triangle = shape_factory.create_shape('Triangle')
    triangle_area = triangle.Area(2, 3)
    print(f'这是一个三角形，它的面积是：{triangle_area}')

    ellipse = shape_factory.create_shape('Ellipse')
    ellipse_area = ellipse.Area(3, 2)
    print(f'这是一个椭圆，它的面积是：{ellipse_area}')

    # ---------------------------------------------------------------
    red = color_factory.create_color('Red')
    red.color('红色')

    blue = color_factory.create_color('Blue')
    blue.color('蓝色')

    black = color_factory.create_color('Black')
    black.color('黑色')