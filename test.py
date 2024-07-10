import random

def make_card_heap():
    lst = []
    for i in range(1, 14):
        [lst.append(str(i)) for _ in range(4)]

    lst += ['14','15']
    return lst

def update(heap, cards):
    for card in cards:
        heap.remove(card)


def show_cards(lst):
    replace = {'1':'A', '11':'J', '12':'Q', '13':'K', '14':'小王', '15':'大王'}
    return [replace[card] if card in replace else card for card in lst ]

def card_to_num(lst):
    replace = {'A':'1', 'J':'11', 'Q':'12', 'K':'13', '小王':'14', '大王':'15'}
    return [replace[card] if card in replace else card for card in lst]

class Card(object):
    card_heap = make_card_heap()

    @classmethod
    def deal_cards(cls):
        if len(Card.card_heap) >= 10:
            computer_cards = random.sample(Card.card_heap, 5)
            update(Card.card_heap, computer_cards)

            user_cards = random.sample(Card.card_heap, 5)
            update(Card.card_heap, user_cards)
            return computer_cards, user_cards
            
        elif len(Card.card_heap) < 10:
            computer_cards = random.sample(Card.card_heap, 2)
            update(Card.card_heap, computer_cards)

            user_cards = random.sample(Card.card_heap, 2)
            update(Card.card_heap, user_cards)
            return computer_cards, user_cards


class Game(object):
    @staticmethod
    def menu():
        print('=' * 14 + '游戏' + '=' * 14)
        print('1. 猜数字游戏')
        print('2. 纸牌猜大小游戏')
        print('3. 退出游戏系统')
        print('=' * 32)

    def guess_num(self):
        print('-' * 32)
        print('欢迎来到猜数字游戏！')
        target = random.randint(1, 100)
        n = 0
        while n < 10:
            guess_num = int(input('请输入您要猜测的数字，数字范围1-100：'))
            if guess_num < target:
                print('数字小了！')
                print(f'您已猜测{n+1}次，剩余次数{9-n}次！')
            elif guess_num > target:
                print('数字大了！')
                print(f'您已猜测{n+1}次，剩余次数{9-n}次！')
            else:
                print('恭喜你赢了！')
                return
            n += 1

    def guess_card(self):
        print('-' * 32)
        print('欢迎来到扑克牌比大小游戏！')
        n = 1
        users_win_cards = []
        computer_win_cards = []
        while len(Card.card_heap) != 0:
            print(f'现在开始第{n}轮：')
            print("开始发牌！")
            computer, user = Card.deal_cards()

            

            while len(user) != 0:
                if len(user) == 5:
                    print("您的牌为：")
                    print(show_cards(user))
                    user_choose_card = list(input("请从中选一张牌："))
                    computer_choose_crad = random.sample(computer, 1)
                else:
                    print("您的牌为：")
                    print(show_cards(user))
                    user_choose_card = list(input("请从中选两张牌：").split(' '))
                    computer_choose_crad = random.sample(computer, 2)

                user_choose_card = card_to_num(user_choose_card)
                
                for u, c in zip(user_choose_card, computer_choose_crad):
                    user.remove(u)
                    computer.remove(c)

                user_sum = sum(list(map(lambda x:int(x), user_choose_card)))
                computer_sum = sum(list(map(lambda x:int(x), computer_choose_crad)))

                if user_sum < computer_sum:
                    print('你的点数小了！')
                    [computer_win_cards.append(card) for card in computer_choose_crad]
                    [computer_win_cards.append(card) for card in user_choose_card]
                else:
                    print("你的点数大了！")
                    [users_win_cards.append(card) for card in computer_choose_crad]
                    [users_win_cards.append(card) for card in user_choose_card]

            print(f'你赢得的牌：{show_cards(users_win_cards)}')
            print(f'电脑赢得的牌：{show_cards(computer_win_cards)}')
            print('-' * 32)
            n += 1

        user_total_sum = sum(list(map(lambda x: int(x), users_win_cards)))
        computer_total_sum = sum(list(map(lambda x: int(x), computer_win_cards)))

        if user_total_sum < computer_total_sum:
            print("你输了！")
        else:
            print("你赢了")
        



    def play(self):
        while True:
            Game.menu()
            num = int(input('请输入你要玩的游戏：'))
            if num == 1:
                self.guess_num()
            elif num == 2:
                self.guess_card()
                pass
            elif num == 3:
                print("感谢使用！再见！")
                break
            else:
                print("无效！请重新输入！")



if __name__ == '__main__':
    game = Game()
    game.play()
    


  