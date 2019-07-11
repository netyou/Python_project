import random


class Settings:
    """场景布置"""

    def __init__(self):
        self.left = 0
        self.right = 10
        self.top = 0
        self.bottom = 10


class Turtle(Settings):
    """乌龟设置"""

    def __init__(self):
        super(Turtle, self).__init__()
        self.turtle_x = random.randint(0, 10)
        self.turtle_y = random.randint(0, 10)
        self.turtle_speed = random.randint(1, 2)
        self.turtle_life = 100

    def move(self):
        new_x = random.choice([self.turtle_speed, 2*self.turtle_speed,
                               -self.turtle_speed, -2*self.turtle_speed]) + self.turtle_x
        new_y = random.choice([self.turtle_speed, 2 * self.turtle_speed,
                               -self.turtle_speed, -2 * self.turtle_speed]) + self.turtle_y

        # 判断乌龟的移动是否超出了边界
        if new_x > 10:
            self.turtle_x = 10 - (new_x - 10)
        elif new_x < 0:
            self.turtle_x = 0 - (new_x - 0)
        else:
            self.turtle_x = new_x

        if new_y > 10:
            self.turtle_y = 10 - (new_y - 10)
        elif new_y < 0:
            self.turtle_y = 0 - (new_y - 0)
        else:
            self.turtle_y = new_y
        self.turtle_life -= 1
        return self.turtle_x, self.turtle_y

    def power(self):
        return self.turtle_life

    def eat(self):
        self.turtle_life += 20
        if self.turtle_life >= 100:
            self.turtle_life = 100


class Fishes(Settings):
    """鱼"""

    def __init__(self):
        super(Fishes, self).__init__()
        self.fishes_x = random.randint(0, 10)
        self.fishes_y = random.randint(0, 10)
        self.fishes_speed = 1
        self.fishes_number = 10

    def move(self):
        new_x = random.choice([self.fishes_speed, -self.fishes_speed]) + self.fishes_x
        new_y = random.choice([self.fishes_speed, -self.fishes_speed]) + self.fishes_y

        # 判断乌龟的移动是否超出了边界
        if new_x > 10:
            self.fishes_x = 10 - (new_x - 10)
        elif new_x < 0:
            self.fishes_x = 0 - (new_x - 0)
        else:
            self.fishes_x = new_x

        if new_y > 10:
            self.fishes_y = 10 - (new_y - 10)
        elif new_y < 0:
            self.fishes_y = 0 - (new_y - 0)
        else:
            self.fishes_y = new_y

        return self.fishes_x, self.fishes_y


def event():
    turtle = Turtle()
    fish = []
    for i in range(10):
        new_fish = Fishes()
        fish.append(new_fish)

    while True:
        if not len(fish):
            print("鱼被吃完了")
            break
        if not turtle.power():
            print("乌龟没有体力了")
            break

        pos = turtle.move()

        # 在迭代中做列表的删除元素是非常危险的，经常会出现一些意想不到的问题，因为迭代器是直接饮用列表元素
        # 的数据做的操作， 所以我们把列表拷贝一份传给迭代器，然后再对元列表操作
        # 相当于一个做循环，一个做操作
        for each_fish in fish[:]:
            if each_fish.move() == pos:
                turtle.eat()
                fish.remove(each_fish)
                print("有一条鱼被吃掉了")

event()




