data = input()
res = []                     ## 최종 결과 출력을 위한 List
word = []                    ## 단어를 뒤집기 위한 List
tag_flag = False             ## 괄호의 시작을 알리는 Flag
for value in data:
    if value == '>':         ## 닫는 괄호를 먼저 체크  --> 괄호가 열리면 tag_flag가 True로 바뀌고           
        res.append(value)    ## tag_flag가 True일 때는 괄호 안에 있는 문자임을 의미
        tag_flag = False     ## 괄호가 닫히기 전까지 tag_flag를 활용하여 괄호 안에 있는 문자를 구분하기 위함
                             ## 만약 닫는 괄호를 체크하는 if 문이 뒤에 있다면 tag_flag를 False로 바꿔주지 못한다.
    elif tag_flag:
        res.append(value)

    elif value == '<':                            
        if word:                                  ## 이 괄호의 시작이 처음이 아니라 앞에 다른 괄호가 있을 수 있음
            res.append(''.join(reversed(word)))   ## Ex) <abc>def<ghi>
            word = []                             ##               ↑ 이 괄호가 시작된 부분 일 경우
        res.append(value)                         ## def는 word안에 존재하게 됨
        tag_flag = True                           ## word를 뒤집어서 res에 넣어주고자 word에 문자가 있는지 먼저 체크
    
    elif value == ' ':                            ## 단어가 구분될 경우 word에 있는 단어를 뒤집어서 res에 넣어줘야함
        res.append(''.join(reversed(word)))       ## 기존의 word에 존재하던 단어를 뒤집어서 res에 넣어주고
        res.append(value)                         ## 공백도 넣어준다.
        word = []                                 ## 다음 단어를 위해서 word는 비워준다.
    
    else:                                         ## 공백도 아니고 괄호도 아니고 tag_flag가 True도 아닐 경우에는
        word.append(value)                        ## 뒤집어야 하는 일반적인 문자이기 때문에 word에 추가해준다.

res.append(''.join(reversed(word)))               ## 테스트 케이스가 닫히는 괄호로 끝날 경우 word는 빈 상태가 되지만
print(''.join(res))                               ## Ex) abc def 일 경우 abc는 res에 들어가 있지만 def는 word에 남아 있게 된다.
                                                  ## 남아 있는 문자를 뒤집어서 res에 넣어준다. 