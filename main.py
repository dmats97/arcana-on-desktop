import os, sys, csv, json, random
#import pygame

class Object:
    def __init__(this, ID, Place):
        this.ID = ID
        this.level = 1
        this.place = Place
        this.cost  = 0
        this.BP    = 0
        this.death = 0
        this.diff_cost = 0
        this.diff_BP   = 0
        this.image = pygame.image.load("cards/thum_0001.jpg")

    #オブジェクトのレベルを変更する
    def level(this, value):
        this.level += value
        if this.level > 3 : this.level = 3
        if this.level > 0 : this.level = 0
        return this.level

class Game:

    def __init__(this):
        # - initialize
        # pygame.init()
        # window = pygame.display.set_mode((1280,680))
        # pygame.display.set_caption("Pygame Practice")

        this.Life = [8, 8]
        this.CP = [0,0]
        this.JokerID = [0, 0]
        this.JokerGuage = [0, 0]

        # - objects list
        this.deck0 = []
        this.deck1 = []
        this.hand0 = []
        this.hand1 = []
        this.trash0 = []
        this.trash1 = []
        this.delete0 = []
        this.delete1 = []
        this.trigger0 = []
        this.trigger1 = []

        # - load database
        fd = open("data.json")
        this.db = json.load(fd)

        # - load starterdeck
        fd = open("deck.csv", encoding="utf-8")
        for data in csv.reader(fd):
            this.deck0.append(data[0])
            this.deck1.append(data[0])

        for i in this.deck0:
            print(this.db[str(i)]['name']);

        # - const
        this._Top_Draw = 2
        this._Turn_Seconds = 60
        this._LastTurnNumber = 10
        this._Incremental_JokerGuege_ByLifeDamege = 10
        this._Incremental_JokerGuege_ByTurnEnd = 10
        this._CP_Table = [[2,3,4,5,6,7,7,7,7,7],[3,3,4,5,6,7,7,7,7,7]]

    def start(this):
        while(True):
            a = input('Action:')
            if a=="draw":
                if draw(0):
                    print("あなたはカードを引きました.\n")
                else:
                    print("エラーが返されました.正常に操作を行えませんでした\n")

            if a=="drive":
                if len(this.hand0):
                    tmp_obj=this.hand0[0]

                if tmp_obj and drive(tmp_obj):
                    print("あなたは手札からユニットを召喚しました\n")
                    del this.hand0[0]
                else:
                    print("エラーが返されました.正常に操作を行えませんでした\n")

            if a=="help":
                print("draw\ndrive\n")

            if a=="show":
                #print(this.hand0)
                print(this.deck0)

            if a=="exit":
                break

            #window.fill((0,0,0))

            ##ここに描画対象を列挙
            #for card in hand0:
            #    window.blit(card.image,(32,48))

            #pygame.display.update()

            #for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()
            #        sys.exit()

        def draw(this, player):
            return 0

newgame = Game()
newgame.start()
