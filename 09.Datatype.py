# try:
#     print("집 가고 싶다.")
# except :
#     print("집에 못 갑니다. 3시간만 참으세요.")

# try:
#     10/0
#     print("hello world")
# except ZeroDivisionError:
#     print("어떤 수를 0으로 나누는 에러가 발생했습니다. 관리자에게 문의하세요. ")

def my_function() :
    a = 10 / 0

    return
try:
    my_function()
except :
    print("에러가 있습니다.")