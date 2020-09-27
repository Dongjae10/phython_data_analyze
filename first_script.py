# coding=utf-8
from math import exp, log, sqrt

print ("Output #1 : I'm excited to learn Python")

# 두 수를 더한다.
x = 4
y = 5
z = x + y
print ("Output #2 : Four plus five equals {0:d}." .format(z))

# 두 리스트를 더한다.
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a + b
print ("Output #3 : {0}, {1}, {2}" .format(a, b, c))

# 정수

x = 9
print ("Output #4 : {0}" .format(x))
print ("Output #5 : {0}" .format(3**4)) # 3의 4승
print ("Output #6 : {0}" .format(int(8.3)/int(2.7))) # 실수형을 정수형으로 변환

# 실수

print ("Output #7 : {0:.3f}" .format(8.3/2.7)) # 소수 3번째 자리까지 출력
y = 2.5 * 4.8
print ("Output #8 : {0:.1f}" .format(y))
r = 8 / float(3)
print ("Output #9 : {0:.2f}" .format(r))
print ("Output #10 : {0:.4f}" .format(8.0/3)) # 정수와 실수 연산의 결과값은 실수형이다.

# type
print ("Output #11 : {0}" .format(type(r))) # 자료형 리턴

# 표준 모듈 math
print ("Output #12 : {0:.4f}" .format(exp(3))) # 자연상수 e 거듭제곱
print ("Output #13 : {0:.2f}" .format(log(4))) # 자연로그
print ("Output #14 : {0:.1f}" .format(sqrt(81))) # 제곱근

# 문자열
print ("Output #15 : {0:s}" .format('I\'m enjoying learning Python')) # 작은 따옴표를 구분하기 위해 역슬래쉬 사용
print ("Output #16 : {0:s}" .format("This is a long string. Without the backslash\
it would run off of the page on the right in text editor and be very\
difficult to read and edit. By using the backslash you can split the long\
string into smaller string on seperate lines so that whole string is easy\
")) # 단일문자열을 개발자가 읽기 쉽게 라인을 나누는 법
print ("Output # 17 : {0:s}" .format('''You can use triple single quotes
for multi-line comment strings.''')) # 문자열을 라인별로 나눠서 출력하기
print ("Output # 18 : {0:s}" .format("""You can also use triple quotes
for multi-line comment strings."""))

string1 = "This is a "
string2 = "short string."
sentence = string1 + string2 #문자열 합치기
print ("Output #19 : {0:s}" .format(sentence))
print ("Output #20 : {0:s} {1:s}{2:s}" .format("She is", "very"*4, "beautiful")) #문자열 여러번 출력
m = len(sentence) #문자열 길이
print ("Output #21 : {0:d}" .format(m))

#split
string1 = "My deliverable is due May"
string1_list1 = string1.split() # 문자열을 split 배열에 담는다.
string1_list2 = string1.split(" ", 2) # 공백을 기준으로 2번 나누면 3개의 요소가 생긴다
print ("Output #22 : {0}".format(string1_list1))
print ("Output #23 : FIRST PIECE : {0} SECOND PIECE : {1} THIRD PIECE : {2}"\
       .format(string1_list2[0], string1_list2[1], string1_list2[2]))

string2 = "Your ,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #24: {0}" .format(string2_list))
print("Output #25: {0} {1} {2}" .format(string2_list[1], string2_list[5],\
string2_list[-1]))

#join
print("Output #26 : {0}" .format(',' .join(string2_list))) #split으로 나누어진 문자열 합치기

#strip
string3 = "   Remove   unwanted characters    from this string.\t\t    \n"
print("Output #27 : string3 : {0:s}".format(string3)) #공백문자 왼쪽 제거
string3_lstrip = string3.lstrip()
print("Output #28 : lstrip : {0:s}" .format(string3_lstrip)) #공백문자 오른쪽 제거
string3_rstrip = string3.rstrip()
print("Output #29 : rstrip : {0:s}" .format(string3_rstrip)) #공백문자 양끝 제거
string3_strip = string3.strip()
print("Output #30 : strip : {0:s}" .format(string3_strip))
string4 = "$$Here's another string that has unwanted charcater.__---++"
print("Output #31 : {0:s}" .format(string4)) #사용자가 지정한 문자 양끝 제거
string4_strip = string4.strip('$_-+')
print("Output #32 : strip :{0:s}" .format(string4_strip))

#replace

string5 = "Let's replace the spaces in this sentence with other character."
print ("Output #33 : {0:s}" .format(string5))
string5_replace = string5.replace(" ", "!@!") # 사용자가 지정한 문자열 다른 문자열로 교체
print("Output #34 (with !@!) : {0:s}" .format(string5_replace))

string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #35 : {0:s}" .format(string6))
string6_lower = string6.lower() # 각각의 문자열을 소문자로 바꿔준다.
print("Output #36 : lower :{}" .format(string6_lower))
string7 = "Here's what Happens WHEN You Use UPPER."
print("Output #37 : {0:s}" .format(string7))
string7_upper = string7.upper() # 각각의 문자열을 대문자로 바꿔준다.
print("Output #38 : {0:s}" .format(string7_upper))
string5 = "here's WHAT Happens when you use Capitalize"
print("Output #39 : {0:s}" .format(string5))
string5_list = string5.split()
print("Output #40 : (on each word) : ")
for word in string5_list: # 리스트 내에 있는 모든 원소에 대해 어떤일을 수행하겠다.
    print("{0:s}" .format(word.capitalize())) # 리스트의 각 원소에 대해 capitalize 함수를 적용 (앞 글자 대문자로 치환)







