import time

def write_loop(i):
    length = len(str(i))
    with open("人类高质量代码.cpp", "at") as fo:
        fo.write('\tcase {}:\n'.format(i))
        fo.write('\t\tcout << "是{}位数" << endl;\n'.format(length))
    ls = ['个', '十', '百', '千', '万']
    a = i
    for j in range(5):
        a = a%10
        with open("人类高质量代码.cpp", "at") as fo:
            fo.write('\t\tcout << "{}位数是：{}" << endl;\n'.format(ls[j], a))
        a = i//10
        if a == 0:
            break
    with open("人类高质量代码.cpp", "at") as fo:
        fo.write('\t\tcout << "倒过来是：{}" << endl;\n'.format(str(i)[::-1]))
        fo.write('\t\tbreak;\n')
        

start = time.time()
with open("人类高质量代码.cpp", "wt") as fo:
    fo.write("# include<iostream>\nusing namespace std;\n\n")
    fo.write("int main()\n{\n")
    fo.write('\tcout << "请给出一个不多于5位的正整数：":\n')
    fo.write('\tint x;\n')
    fo.write('\tcin >> x;\n\n')
    fo.write('\tswitch(x) {')
# 开始正式步骤
for i in range(1, 100000):
    write_loop(i)
# 结个尾
with open("人类高质量代码.cpp", "at") as fo:
    fo.write('\t}\n')
    fo.write('}')
print("人类高质量代码完成！")
print("用时{}s".format(time.time() - start))
