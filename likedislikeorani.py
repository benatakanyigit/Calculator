def rating_hesaplayici():
    global rating
    rating = (like_num / ((like_num+dislike_num)))*100

def rating_gosterici():
    print("Bu videonun beğenilme oranı: %", rating)

    if rating < 50:
        print("Bu video az beğenildi.")
    elif rating == 50:
        print("Bu videonun like ve dislike sayıları birbirine eşit.")
    else:
        print("Bu video çok beğenildi.")


def user_input():
    global like
    global dislike
    global like_num
    global dislike_num

    print("Lütfen video like değerini giriniz:")
    try:
        like_num = int(input())

    except ValueError:
        print("Sayı girmelisiniz.")
        user_input()
    print("Lütfen video dislike değerini giriniz:")
    try:
        dislike_num = int(input())
    except ValueError:
        print("Sayı girmelisiniz...")
        user_input()

print("Selam, videonun Rating değerini hesaplamak için aşağıdaki adımları takip edebilirsin!")
user_input()
rating_hesaplayici()
print ("Rating değeri:", rating)
rating_gosterici()



