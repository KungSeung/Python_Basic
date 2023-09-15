# 주석처리 : ctrl k+c / 주석해제 : ctrl k+u
print('hello')

name = 'my name is seung'

print(name)
print(name[0])

# 리스트
중고차 = ['k5', 'white', '5000']
중고차[1] = 'black'
print(중고차[0])

# 딕셔너리
중고차2 = {'brand' : 'bmw', 'model' : '520d' }
중고차2['brand'] = 'benz'
print(중고차2['brand'])

# if
재고량 = 10
if 재고량 > 0 : 
    print('지금 주문 가능합니다')

중고차재고 = ['k5', 'bmw', 'Tico']

if 'k6' in 중고차재고: 
    print('지금 주문 가능합니다')
elif 'bmw2' in 중고차재고:
    print('지금 주문 가능합니다2')
else:
    print('지금 주문 가능합니다3')

# for
중고차들 = ['k5', 'bmw','Tico'] # List
중고차들2 = {'brand1':'k5', 'brand2':'bmw', 'brand3':'Tico'} # dict

for i in range(0, 10):
    print('bmw 있음')

for i in 중고차들:
    print(i * 3)

for i,name in 중고차들2.items():
    print(i * 3, name * 3)



# 함수 def
def 인사하기() :
    print('Hello 승입니다')

인사하기()

def 모자(x, y):
    print(1+x, 2+y)

모자(121, 123)

def 함수():
    return 10

print(함수())

print(len([1,2,3]))