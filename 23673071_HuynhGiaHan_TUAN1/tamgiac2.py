import Triangle as rect

menu_options = {
    1:"Them tam giac moi",
    2:"Hien thi danh sach tam giac",
    3:"Tinh tong dien tich cac tam giac",
    4:"Hien thi cac tam giac co chu vi nho nhat",
    "5": "Thoat chuong trinh"
    }

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key])
        
dsTG = []
while(True):
    print_menu()
    userChoice = ""
    try:
        userChoice = int(input("Nhap tuy chon: "))
    except:
        print('Nhập sai định dạng, hãy nhập lại.....')
        continue
    if userChoice == 1:
        canhbc = float(input("Nhap canh bc: "))
        canhab = float(input("Nhap canh ab: "))
        canhac = float(input("Nhap canh ac: "))
        chieucao = float(input("Nhap chieu cao: "))
        tamgiac = rect.Triangle(canhbc,canhab,canhac,chieucao)
        dsTG.append(tamgiac)
    elif userChoice == 2:
        for item in dsTG:
            item.display()
    elif userChoice == 3:
        dientich = 0.0
        for item in dsTG:
            dientich = dientich + item.area()
        print(f'Tổng diện tích là: {dientich}') 
    elif userChoice == 4:
        if dsTG.count == 0:
            print('Danh sách rỗng')
        else:
            chuvinn = dsTG[0].perimeter()
            for item in dsTG:
                if chuvinn > item.perimeter():
                    chuvinn = item.perimeter()
            for item in dsTG:
                if item.perimeter() == chuvinn:
                    item.display()
    else:
        print('Thoát chương trình BYE BYE')
        break
    
