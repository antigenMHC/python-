import random
import tkinter

class RandomBall():
    '''
    运动的球
    '''
    def __init__(self, canvas, scrn_width,scrn_heigh):
        '''
        球的构造函数
        :param canvas: 传入画布，在画布上进行球的构造
        :param scrn_width: 传入屏幕宽度
        :param scrn_heigh: 传入屏幕高度
        '''
        #x，y表示出现的球的圆心
        self.ball_x = random.randint(20, int(scrn_width - 20)) #球出现的随机x坐标
        self.ball_y = random.randint(10, int(scrn_heigh - 10)) #球出现的随机y坐标
        #模拟运动：就是不断地重画球，不断地更新球的位置
        self.x_move = random.randint(4, 30) #模拟x方向运动
        self.y_move = random.randint(5, 20) #模拟y方向运动
        #定义宽度和高度和画布
        self.canvas = canvas
        self.scrn_width = scrn_width
        self.scrn_heigh = scrn_heigh
        #球的大小随机
        self.rad = random.randint(20, 150) #用半径rad表示球的大小
        #定义颜色
        c = lambda : random.randint(0, 255)
        self.color = "#%02x%02x%02x"%(c(), c(), c())

    def creat_ball(self):
        '''
        用构造函数中的值创建一个球
        :return:
        '''
        #tkinter没有画圆函数，只有椭圆函数
        #但在正方形里面画的椭圆就是正圆
        #已知圆心坐标和半径，则圆心坐标减半径能求出正方形左上角
        #圆心坐标加上半径，能求出右下角
        #已知左上角和右上角，可以画出
        x1 = self.ball_x - self.rad #左上角的x坐标
        y1 = self.ball_y - self.rad #左上角的y坐标
        x2 = self.ball_x + self.rad #右下角的x坐标
        y2 = self.ball_y + self.rad #右下角的y坐标
        #在有对角坐标的情况下就可以创建圆
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill = self.color, outline = self.color)

        # 球动
    def move_ball(self):
        self.ball_x += self.x_move #球移动后的新x坐标
        self.ball_y += self.y_move #球移动后的新y坐标
        # 碰壁回弹判断
        if self.ball_x + self.rad >= self.scrn_width: #撞到了右边的墙
            self.x_move = -self.x_move
        if self.ball_x - self.rad <= 0: #撞到了左边的墙
            self.x_move = -self.x_move
        if self.ball_y + self.rad >= self.scrn_heigh: #撞到下面的墙
            self.y_move = -self.y_move
        if self.ball_y - self.rad <= 0: #撞到上面的墙
            self.y_move = -self.y_move
        self.canvas.move(self.item, self.x_move, self.y_move) #利用x，y的移动距离控制球的移动快慢

class ScreenSaver():
    '''
    可以被启动的屏保
    '''
    #创建一个list装创建的球

    def __init__(self):
        self.balls = list()
        self.nums_balls = random.randint(6, 20) #产生随机数量的球
        self.baseFrame = tkinter.Tk() #启动界面
        self.baseFrame.overrideredirect(1) #取消边框
        #移动鼠标则退出屏保
        self.baseFrame.bind("<Motion>", self.my_quit)
        self.baseFrame.attributes('-alpha', 1)
        #键盘任意键退出屏保
        self.baseFrame.bind("<Key>",self.my_quit)
        #得到屏幕的宽和高
        w = self.baseFrame.winfo_screenwidth()
        h = self.baseFrame.winfo_screenheight()
        #创建画布
        self.canvas = tkinter.Canvas(self.baseFrame, width = w, height = h)
        self.canvas.pack()

        #在画布上画球
        for i in range(self.nums_balls):
            ball = RandomBall(self.canvas, scrn_width = w, scrn_heigh =  h)
            ball.creat_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.baseFrame.mainloop()
    #球动函数
    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        #在sleep100ms以后启动第二个参数函数，相当于100ms动一次
        self.canvas.after(100, self.run_screen_saver)
    #当事件发生时，传入event，退出屏保
    def my_quit(self, event):
        #销毁(析构)(退出)界面
        self.baseFrame.destroy()
if __name__ == "__main__":
    #启动屏保
    ScreenSaver()
