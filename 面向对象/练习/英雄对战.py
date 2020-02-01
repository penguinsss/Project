class Weapons:
    def __init__(self, weapons_name, aggressive):
        self.weapons_name = weapons_name
        self.aggressive = aggressive

    def __str__(self):
        return '武器名称：%s，攻击力：%s' % (self.weapons_name, self.aggressive)


class Hero:
    def __init__(self, hero_name, weapons):
        self.hero_name = hero_name
        self.blood_volume = 100
        self.weapons = weapons
        self.grade = 1

    def attack(self, hero):
        while True:
            attack_damage_to_me = (1 + hero.grade * 0.1) * hero.weapons.aggressive
            attack_damage_to_other = (1 + self.grade * 0.1) * self.weapons.aggressive

            hero.blood_volume -= attack_damage_to_other
            self.blood_volume -= attack_damage_to_me

            if self.blood_volume <= attack_damage_to_me:
                print('%s挂了' % self.hero_name)
                break
            if hero.blood_volume <= attack_damage_to_other:
                print('%s挂了' % hero.hero_name)
                break

            if attack_damage_to_me == attack_damage_to_other:
                print('由于二人水平在同一个级别，打成平手')
                break
            elif attack_damage_to_other > attack_damage_to_me:
                self.grade += 1
            else:
                hero.grade += 1

    def __str__(self):
        return '英雄名称：%s，血量：%s，持有的武器名称：%s，英雄等级：%s' % (self.hero_name, self.blood_volume, self.weapons.weapons_name, self.grade)


z = Hero('张无忌',Weapons('屠龙刀', 10))
d = Hero('东方不败',Weapons('绣花针', 2))
z.attack(d)
print(z)
print(d)

# print('对方的等级：%s ' % hero.grade)
# print('我的等级：%s ' % self.grade)
# print('对方的攻击力：%s ' % attack_damage_to_me)
# print('我的攻击力：%s ' % attack_damage_to_other)
# print('我的血量：%s ' % self.blood_volume)
# print('对方的血量：%s ' % hero.blood_volume)