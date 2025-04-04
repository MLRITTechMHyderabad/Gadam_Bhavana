import random

class Character:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed
    
    def attack(self, target):
        damage = max(1, self.attack_power - target.defense)
        print(f"{self.name} attacks {target.name}! Deals {damage} damage.")
        target.take_damage(damage)
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Remaining health: {self.health}")
    
    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=25, defense=10, speed=8)
        self.rage = 0
    
    def take_damage(self, amount):
        super().take_damage(amount)
        self.rage += amount
        if self.health < 36:  # Berserk Mode if health < 30%
            self.attack_power *= 2
            print(f"{self.name} enters Berserk Mode! Attack power increased.")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=40, defense=5, speed=10)
        self.mana = 100
    
    def fireball(self, target):
        if self.mana >= 20:
            damage = self.attack_power
            self.mana -= 20
            self.health -= 5  # Self-damage
            print(f"{self.name} casts Fireball! Deals {damage} damage but loses 5 health.")
            target.take_damage(damage)
        else:
            print(f"{self.name} doesn't have enough mana!")

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=22, defense=6, speed=15)
        self.critical_chance = 30  # 30% critical hit chance
    
    def attack(self, target):
        if random.randint(1, 100) <= self.critical_chance:
            damage = max(1, self.attack_power * 2 - target.defense)
            print(f"{self.name} lands a Critical Hit! Deals {damage} damage.")
        else:
            damage = max(1, self.attack_power - target.defense)
            print(f"{self.name} shoots an arrow! Deals {damage} damage.")
        target.take_damage(damage)

# Battle System
def battle(fighter1, fighter2):
    print("Battle Begins!")
    fighters = sorted([fighter1, fighter2], key=lambda x: -x.speed)
    while fighter1.is_alive() and fighter2.is_alive():
        for fighter in fighters:
            if fighter.is_alive():
                if isinstance(fighter, Mage):
                    fighter.fireball(fighters[1] if fighter == fighters[0] else fighters[0])
                else:
                    fighter.attack(fighters[1] if fighter == fighters[0] else fighters[0])
            if not fighter1.is_alive() or not fighter2.is_alive():
                break
    
    winner = fighter1 if fighter1.is_alive() else fighter2
    print(f"{winner.name} wins the battle!")

# Example Battle
alex = Archer("Alex")
thor = Warrior("Thor")
gandalf = Mage("Gandalf")

battle(alex, thor)
