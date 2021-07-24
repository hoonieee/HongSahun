sentence = "나는 소년입니다"
print(sentence)

sentence3 = """
나는 소년이고
파이썬은 쉬워요
"""
print(sentence3)
jumin = "021205-3456789"

print("성별 : " + jumin[7])
print("연 : " + jumin[:2]) # 0부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[ :6])
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지

#문자열 처리 함수

python = "Python is Amazing"
print(python.lower())  #모두 소문자로 변경
print(python.upper())  #모두 대문자로 변경
print(python[0].isupper())  #소문자인지 대문자인지 구분해줌 
print(len(python))   #문장의 길이를 이야기 해줌
print(python.replace("Python", "java")) #대소문자 구별해줘야됨


index = python.index("n") 
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("java")) #-1이 변환됨

print(python.count("i"))

#문자열 출력
print("나는 %d살 입니다." %20)  #d는 정수를 의미함
print("나는 %s을 좋아해요." % "파이썬") #s는 문자열 (str)값을 의미함
print("Apple 은 %c로 시작해요." % "A")  #c는 한 글자만 받는다.
# %s는 모두 출력을 받는다

print("나는 %s색과 %s색을 좋아해요."  %("파란", "빨간"))
print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))  #format 앞에 . 붙이고, 괄호 사이에 , 붙이기

print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


#\n 은 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

print("저는 '홍사훈'입니다.")
print('저는 "홍사훈"입니다.')
print("저는 \"홍사훈\"입니다.")
print("저는 \'홍사훈\'입니다.")

# \\ : 문장 내에서 하나의 \로 바뀐다.
# \r : 커서를 맨 앞으로 이동
print("red apple\rpine")
# \b : 백스페이스 (한 글자 삭제)
print("redd\bapple")
# \t : 탭
print("red\t\t\tapple")

#퀴즈
#사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

site = "http://naver.com"
pass1 = site[7:]
pass2 = pass1[:3]
pass3 = len(pass2)
pass4 = site.count("e")
pass5 = "!"
print(pass2, pass3, pass4, pass5)

site = "http://google.com"
pass1 = site.replace("http://", "")
pass2 = pass1[:pass1.index(".")]
pass3 = pass2[:3]
pass4 = len(pass2)
pass5 = pass2.count("e")
pass6 = "!"
password = pass3+str(pass4)+str(pass5)+pass6
print("{0} 사이트의 비밀번호는 {1} 입니다." .format( site, password))




























from random import *
site = "www.youtube.com"
pass1 = site.replace("www.", "")
pass2 = pass1[:pass1.index(".")]
pass3 = pass2[:3]
pass4 = len(pass2)
pass5 = pass2.count("e")
pass6 = randint(10,99)
pass7 = "!"
password = pass3 + str(pass4) + str(pass5) + str(pass6) + pass7
print(password)

