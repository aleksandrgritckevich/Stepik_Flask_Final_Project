class Game:
    def __init__(self):
        self.fields = [[100,1,100],[1,1,1],[1,1,1]]
        self.directions = {"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}
        self.curr = [2,0]
        self.room = [["","Балкон",""],["Спальня","Холл","Кухня"],["Подземелье","Коридор","Оружейная"]]
        self.to_display = ["Привет!"]
        self.times=0
    def move(self,direction):
        new = [self.curr[0]+self.directions[direction][0],self.curr[1]+self.directions[direction][1]]
        if 0<=new[0]<=2 and 0<=new[1]<=2 and self.fields[new[0]][new[1]]!=100:
            self.curr = new
        return self.curr
    def move_multiple(self,direction,steps):
        self.times+=1
        self.to_display = []
        while steps:
            if self.curr==self.move(direction):
                self.to_display.append("Вы не можете идти сюда!")
                break
            else:
                self.to_display.append(f"Вы находитесь в {self.room[self.curr[0]][self.curr[1]]}")
                steps-=1
        return self.to_display





