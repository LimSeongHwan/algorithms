data = input()
max_str = ''
min_str = ''
m_num = 0

for i in range(len(data)):
    if data[i] == 'M':
        m_num += 1
    else:
        max_str += str(5) + str(0) * m_num
        if m_num:
            min_str += (str(1) + str(0) * (m_num - 1)) + str(5)
        else:
            min_str += str(5)
        m_num = 0

if m_num:
    max_str += str(1) + str(1) * (m_num - 1)
    min_str += str(1) + str(0) * (m_num - 1)

print(max_str)
print(min_str)