class Birds:
    def __init__(self,name,color,skill_desciption):
        self.name = name
        self.color = color
        self.skill_desciption = skill_desciption
    def fly(self):
        print(f"{self.name} can fly.")
    def call(self):
        print(f"{self.name} can call")
    def use_skill(self):
        print(f"{self.name} use {self.skill_desciption}.")

    
class RedBirds(Birds):
    def __init__(self):
        super().__init__('红', '红色', '快速飞行,大声叫')
    def fly(self):
        print(f"{self.name} can fly very fast.")
    def call(self):
        print(f"{self.name} can call loudly.")
        
class YellowBirds(Birds):
    def __init__(self):
        super().__init__('黄', '黄色', '瞬间加速')
    def fly(self):
        print(f"{self.name} can fly very fast.")
    def call(self):
        print(f"{self.name} can call loudly.")
        
class BlueBirds(Birds):
    def __init__(self):
        super().__init__('蓝', '蓝色', '分裂成三只小鸟')
    def fly(self):
        print(f"{self.name} can fly very fast.")
    def call(self):
        print(f"{self.name} can call loudly.")
        
        
class Obstacle:
    def __init__(self,name,strength):
        self.name = name
        self.strength = strength
    def be_attacked(self, bird):
        print(f'{bird.name}attacks {self.name}')
        bird.use_skill()
        
        if isinstance(bird, RedBirds):
            dagame = 80
        elif isinstance(bird, YellowBirds):
            dagame = 50
        elif isinstance(bird, BlueBirds): 
            dagame = 30
        self.strength -= dagame
        
        if self.strength <= 0:
            print(f'{self.name} is destroyed by {bird.name}.')
            
o1 = Obstacle('木头', 100)
r1 = RedBirds()
r1.fly()
o1.be_attacked(r1)