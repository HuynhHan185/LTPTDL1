import matplotlib.pyplot as plt
import Song as song  

menu_options = {
    1:'Load data from file',
    2:'Add new song',
    3:'Display list of songs',
    4:'Show song details',
    5:'Update song information',
    6:'Delete song',
    7:'Increase views of song',
    8:'Decrease views of song',
    9:'Show total number of songs',
    10:'Show total views',
    11:'Show average of views',
    12:'Show average release year',
    13:'Show song(s) with maximum views',
    14:'Sort list of songs according to views by ascending',
    15:'Draw chart of views according to release year',
    16:'Draw average views by year group (<2010, 2010-2020, >2020)',
    17:'Draw percentage of views by year group',
    18:'Draw percentage of total songs by genre',
    19:'Store data to file',
    20: 'Exit program'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key])

dsBaiHat = []

while(True):
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input('Input choice: '))
    except:
        print('Invalid input, try again')
        continue

    if userChoice == 1:
        fr = open('dbsong_input.db', mode='r', encoding='utf-8')
        for line in fr:
            stripLine = line.strip('\n')
            ds = stripLine.split(',')
            code = ds[0]
            title = ds[1]
            singer = ds[2]
            genre = ds[3]
            year = int(ds[4])
            views = int(ds[5])
            bh = song.Song(code,title,singer,genre,year,views)
            dsBaiHat.append(bh)
        fr.close()

    elif userChoice == 2:
        code = input("Nhap code: ")
        title = input("Nhap title: ")
        singer = input("Nhap singer: ")
        genre = input("Nhap genre: ")
        year = int(input("Nhap year: "))
        views = int(input("Nhap views: "))
        bh = song.Song(code,title,singer,genre,year,views)
        dsBaiHat.append(bh)

    elif userChoice == 3:
        if len(dsBaiHat)==0:
            print('Danh sach rong')
        else:
            for item in dsBaiHat:
                item.display()

    elif userChoice == 4:
        code = input("Nhap ma bai hat: ")
        for item in dsBaiHat:
            if item.code == code:
                item.display()

    
    elif userChoice == 5:
        code = input("Input song code for update: ")
        for item in dsBaiHat:
            if item.code == code:
                item.display()
                menu = {
                    1:'Update title',
                    2:'Update singer',
                    3:'Update genre',
                    4:'Update year',
                    5:'Update views',
                    'Others':'Exit'
                }
                def Xuat_menu():
                    for key in menu.keys():
                        print(key,'--',menu[key])
                while(True):
                    Xuat_menu()
                    try:
                        chon = int(input("Nhap tuy chon: "))
                    except:
                        print("Nhap sai dinh dang")
                        continue
                    if chon == 1:
                        item.title = input("New title: ")
                    elif chon == 2:
                        item.singer = input("New singer: ")
                    elif chon == 3:
                        item.genre = input("New genre: ")
                    elif chon == 4:
                        item.year = int(input("New year: "))
                    elif chon == 5:
                        item.views = int(input("New views: "))
                    else:
                        break
                item.display()

    
    elif userChoice == 6:
        code = input("Nhap ma code muon xoa: ")
        for item in dsBaiHat:
            if item.code == code:
                dsBaiHat.remove(item)
                print("Da xoa thanh cong!")

    elif userChoice == 7:
        code = input("Nhap ma code: ")
        for item in dsBaiHat:
            if item.code == code:
                amount = int(input("Nhap ma code muon tang luot xem: "))
                item.increaseViews(amount)
                item.display()

    elif userChoice == 8:
        code = input("Nhap ma code: ")
        for item in dsBaiHat:
            if item.code == code:
                amount = int(input("Nhap ma code muon giam luot xem: "))
                item.decreaseViews(amount)
                item.display()
    
    elif userChoice == 9:
        print(f"Tổng số bài hát: {len(dsBaiHat)}")

    elif userChoice == 10:
        total = sum(item.views for item in dsBaiHat)
        print(f"Tổng lượt nghe: {total}")

    
    elif userChoice == 11:
        if len(dsBaiHat) > 0:
            avg = sum(item.views for item in dsBaiHat) / len(dsBaiHat)
            print(f"Lượt nghe trung bình: {avg}")

    elif userChoice == 12:
        # Average year
        if len(dsBaiHat) > 0:
            avg = sum(item.year for item in dsBaiHat) / len(dsBaiHat)
            print(f"Năm phát hành trung bình: {avg}")

    elif userChoice == 13:
        # Song with max views
        if len(dsBaiHat) > 0:
            maxv = max(item.views for item in dsBaiHat)
            print("Bài hát có lượt nghe nhiều nhất:")
            for item in dsBaiHat:
                if item.views == maxv:
                    item.display()

    elif userChoice == 14:
        # Sort songs by views ascending
        dsBaiHat.sort(key=lambda x: x.views)
        for item in dsBaiHat:
            item.display()

    elif userChoice == 15:
        # Draw views according to year
        arrYear = [item.year for item in dsBaiHat]
        arrViews = [item.views for item in dsBaiHat]
        plt.bar(arrYear, arrViews)
        plt.title("Views by Year")
        plt.xlabel("Year")
        plt.ylabel("Views")
        plt.show()

    elif userChoice == 16:
        # Average views by year group
        group1 = [item.views for item in dsBaiHat if item.year < 2010]
        group2 = [item.views for item in dsBaiHat if 2010 <= item.year <= 2020]
        group3 = [item.views for item in dsBaiHat if item.year > 2020]
        labels = ['<2010','2010-2020','>2020']
        values = [
            sum(group1)/len(group1) if group1 else 0,
            sum(group2)/len(group2) if group2 else 0,
            sum(group3)/len(group3) if group3 else 0
        ]
        plt.bar(labels, values)
        plt.title("Average Views by Year Group")
        plt.show()

    elif userChoice == 17:
        # Percentage views by year group
        group1 = sum(item.views for item in dsBaiHat if item.year < 2010)
        group2 = sum(item.views for item in dsBaiHat if 2010 <= item.year <= 2020)
        group3 = sum(item.views for item in dsBaiHat if item.year > 2020)
        labels = ['<2010','2010-2020','>2020']
        sizes = [group1, group2, group3]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title("Percentage Views by Year Group")
        plt.show()

    elif userChoice == 18:
        # Percentage songs by genre
        genres = {}
        for item in dsBaiHat:
            if item.genre not in genres:
                genres[item.genre] = 0
            genres[item.genre] += 1
        plt.pie(genres.values(), labels=genres.keys(), autopct='%1.1f%%')
        plt.title("Percentage Songs by Genre")
        plt.show()

    elif userChoice == 19:
        # Store data to file
        fw = open('dbsong_output.db', mode='w', encoding='utf-8')
        for item in dsBaiHat:
            fw.write(f"{item.code},{item.title},{item.singer},{item.genre},{item.year},{item.views}\n")
        fw.close()
        print("Lưu file thành công!")

    else:
        print("BYE BYE")
        break