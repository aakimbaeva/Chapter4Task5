class Soldier:
    def __init__(self, name):
        self.name = name

class Gun:
    def __init__(self):
        self.bullets = 10

    def fire(self):
        for bullet in range(self.bullets):
            self.bullets -= 1
            print('tigi-tigitishh')
            if self.bullets == 0:
                print('RELOAD is required!')

    def reload(self):
        self.bullets = 10
        print('Reloaded successfully!')
        self.fire()

class Act_of_Shooting(Soldier, Gun):
    def __init__(self, name):
        Soldier.__init__(self, name)
        Gun.__init__(self)


example = Act_of_Shooting('Ryan')
example.fire()
print('\n')
example.reload()


