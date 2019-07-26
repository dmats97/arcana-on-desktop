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
    Life = [8, 8]
    CP = [0,0]
    JokerID = [0, 0]
    JokerGuage = [0, 0]

    # - objects list
    new_deck0 = []
    new_deck1 = []
    deck0 = []
    deck1 = []
    hand0 = []
    hand1 = []
    trash0 = []
    trash1 = []
    delete0 = []
    delete1 = []
    trigger0 = []
    trigger1 = []

    # - const
    _Top_Draw = 2
    _Turn_Seconds = 60
    _LastTurnNumber = 10
    _Incremental_JokerGuege_ByLifeDamege = 10
    _Incremental_JokerGuege_ByTurnEnd = 10
    _CP_Table = [[2,3,4,5,6,7,7,7,7,7],[3,3,4,5,6,7,7,7,7,7]]

    def __init__(this):
        # - initialize
        # pygame.init()
        # window = pygame.display.set_mode((1280,680))
        # pygame.display.set_caption("Pygame Practice")

        # - load database
        fd = open("data.json")
        this.db = json.load(fd)

        # - load starterdeck
        fd = open("deck.csv", encoding="utf-8")
        for data in csv.reader(fd):
            this.deck0.append(data[0])
            this.deck1.append(data[0])
            this.new_deck0.append(data[0])
            this.new_deck1.append(data[0])

        for i in this.deck0:
            print(this.db[str(i)]['name'])

    def start(this):
        random.shuffle(this.deck0)
        random.shuffle(this.deck1)

        while(True):
            a = input('Action:')
            if a=="draw":
                if this.draw(0):
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
                print("Deck:")
                print(len(this.deck0))
                print("\n\nHand:\n")
                for obj in this.hand0:
                    print(this.db[str(obj)]['name'])

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
        if len(this.hand0)<7:
            if len(this.deck0)<=0:
                this.deck0 = this.new_deck0
            this.hand0.append(this.deck0[0])
            del this.deck0[0]
            return 1
        else:
            return 0

    def drive(this, obj):
        return 0

newgame = Game()
newgame.start()
