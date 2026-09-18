def add_tax(price,taxrate=0.1):
    if price >= 0 and taxrate >= 0:
        return int(price + price * taxrate)
    else:
        return ValueError("問題が発生しました")




# ファイル本体が呼び出されたときのみ実行する
if __name__ == "__main__":
    # assert：==の結果がTrueだと何も返さない
    assert add_tax(1000) == 1100
    assert add_tax(1000,0.08) == 1080
    # print("test")
    print(add_tax(-100, 0.8))
    print(add_tax(100, -0.8))