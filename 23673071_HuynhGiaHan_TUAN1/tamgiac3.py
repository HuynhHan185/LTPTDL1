import Triangle as rect

fr = open('input.db',mode='r',encoding='utf-8')
listTriangle = []
for line in fr:
    stripLine = line.strip('\n')
    ds = stripLine.split(',')
    canhbc = float(ds[0])
    canhab = float(ds[1])
    canhac = float(ds[2])
    chieucao = float(ds[3])

    tamgiac = rect.Triangle(canhbc,canhab,canhac,chieucao)
    listTriangle.append(tamgiac)
fr.close()

# Ghi dữ liệu từ listTriangle xuống file
fw = open('output.db',mode='w',encoding='utf-8')
for item in listTriangle:
    fw.write(f'{item.bc}-{item.ab}-{item.ac}-{item.chieucao}-{item.perimeter()}-{item.area()}\n')
fw.close()


import Triangle as rect
menu ={
    1:'1- Đọc dữ liệu từ file input.db'   ,
    2:'2- Them moi hinh tam giac',
    3:'3- Hien thi danh sach tam giac',
    4:'4- Lưu danh sách hinh tam giac xuống file output.db',
    'Others':'Thoát'
}
def print_menu():
    for key in menu.keys():
        print (key,'--',menu[key])

#Khai bao bien luu tru hinh tam giac
while(True):
    print_menu()
    chon=''
    try:
        chon =int(input('Nhập tùy chọn:'))
    except:
        print('Nhập sai định dạng, hãy nhập lại:')
        continue
#Kiểm tra các lựa chọn
    if chon ==1:
#1- Đọc dữ liệu từ file input.db
        fr=open('input.db', mode='r',encoding ='utf-8') 
        dsTG =[]
        for line in fr:
            stripLine = line.strip('\n')
            ds =stripLine.split(',')
            canhbc = float(ds[0])
            canhab = float(ds[1])
            canhac = float(ds[2])
            chieucao = float(ds[3])
            tamgiac = rect.Triangle(canhbc,canhab,canhac,chieucao)
            dsTG.append(tamgiac)
        fr.close()
    elif chon ==2:
# 2- Thêm mới hình tam giac
        canhbc = float(input("Nhap canh bc: "))
        canhab = float(input("Nhap canh ab: "))
        canhac = float(input("Nhap canh ac: "))
        chieucao = float(input("Nhap chieu cao: "))
        tamgiac = rect.Triangle(canhbc,canhab,canhac,chieucao)
        dsTG.append(tamgiac)
    elif chon ==3:
#3- Hiển thị danh sách hinh tam giac
        if dsTG.count ==0:
            print('Danh sách rỗng')
        else:
            for item in dsTG:
                item.display()
    elif chon == 4:
#4- Lưu danh sách hình chữ nhật xuống file output.db
        fw =open('output.db',mode='w',encoding ='utf-8')
        for item in dsTG:
             fw.write(f'{item.bc}-{item.ab}-{item.ac}-{item.chieucao}-{item.perimeter()}-{item.area()}\n')
        fw.close() 
    else:
        print('Kết thúc chương trình') 
        break