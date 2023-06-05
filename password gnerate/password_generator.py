#パスワードジェネレーター: ランダムなパスワードを生成し、必要に応じてパスワードの長さや使用する文字セットをカスタマイズできるパスワードジェネレーターを作成してください。

import random
import string

def password_generate(length):
    # 文字列を生成
    password = string.ascii_letters + string.digits + string.punctuation
    # 文字列をシャッフル
    password = random.sample(password, length)
    # リストを文字列に変換
    password = ''.join(password)
    return password
if __name__ == '__main__':
    password = password_generate(8)
    print(password)
