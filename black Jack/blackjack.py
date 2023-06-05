#ブラックジャックゲーム: ブラックジャックゲームのコードを作成してください。

import random
import time

# カードのデッキを作成
def create_deck():
    suits = ['♠', '♦', '♥', '♣']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K']
    deck = []
    for suit in suits:
        for number in numbers:
            deck.append(suit + number)
    random.shuffle(deck)
    return deck

# カードを引く
def draw_card(deck):
    card = deck.pop()
    return card

# カードの合計を計算
def count_score(cards):
    score = 0
    for card in cards:
        number = card[1:]
        if number in ['J', 'Q', 'K']:
            score += 10
        elif number == 'A':
            if score >= 11:
                score += 1
            else:
                score += 11
        else:
            score += int(number)
    return score

# ゲームを開始
def start_game(deck):
    player_cards = []
    dealer_cards = []
    # プレイヤーとディーラーにカードを2枚ずつ配る
    for i in range(2):
        player_cards.append(draw_card(deck))
        dealer_cards.append(draw_card(deck))
    # プレイヤーのカードを表示
    print('あなたのカード: {}'.format(player_cards))
    # ディーラーの1枚目のカードを表示
    print('ディーラーのカード: {}'.format(dealer_cards[0]))
    # プレイヤーのカードの合計を計算
    player_score = count_score(player_cards)
    # ディーラーのカードの合計を計算
    dealer_score = count_score(dealer_cards)
    # プレイヤーがカードを引く
    while True:
        # プレイヤーのカードの合計を表示
        print('あなたの合計は{}です'.format(player_score))
        # プレイヤーがバストしていないかチェック
        if player_score > 21:
            print('バストしてしまいました')
            print('あなたの負けです')
            return
        # プレイヤーがブラックジャックかチェック
        elif player_score == 21:
            print('ブラックジャックです！')
            break
        # プレイヤーがカードを引くか選択
        else:
            draw = input('カードを引きますか？(y/n): ')
            if draw == 'y':
                player_cards.append(draw_card(deck))
                player_score = count_score(player_cards)
            elif draw == 'n':
                break
            else:
                print('yかnを入力してください')
    # ディーラーがカードを引く
    while True:
        # ディーラーのカードの合計を表示
        print('ディーラーの合計は{}です'.format(dealer_score))
        # ディーラーがバスト

        if dealer_score > 21:
            print('ディーラーがバストしました')
            print('あなたの勝ちです')
            return
        # ディーラーがブラックジャックかチェック
        elif dealer_score == 21:
            print('ディーラーがブラックジャックです')
            break
        # ディーラーが17以上になるまでカードを引く
        elif dealer_score >= 17:
            break
        else:
            print('ディーラーがカードを引きます')
            time.sleep(2)
            dealer_cards.append(draw_card(deck))
            dealer_score = count_score(dealer_cards)
    # プレイヤーとディーラーの合計を比較
    if player_score > dealer_score:
        print('あなたの勝ちです')
    elif player_score == dealer_score:
        print('引き分けです')
    else:
        print('あなたの負けです')

if __name__ == '__main__':
    deck = create_deck()
    start_game(deck)