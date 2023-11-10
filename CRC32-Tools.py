#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
import zipfile
import argparse
import string
import binascii
import io, sys

def title():
    print('+-----------------------------------------------------+')
    print('+              渊龙Sec安全团队CTF工具包               +')
    print('+              团队公开QQ群：877317946                +')
    print('+            Title: CRC32-Tools,so easy!!!            +')
    print('+  python3 CRC32-Tools.py -h --> 根据不同情况选择参数 +')
    print('+                作者：曾哥（AabyssZG）               +')
    print('+                  版本：V2.3整合版                   +')
    print('+-----------------------------------------------------+')

def FileRead(zipname):
    try:
        f =open(zipname)                               #打开目标文件
        f.close()
    except FileNotFoundError:
        print ("未找到同目录下的压缩包文件" + zipname) #如果未找到文件，输出错误
        return                                         #退出线程，进行详细报错
    except PermissionError:
        print ("无法读取目标压缩包（无权限访问）")     #如果发现目标文件无权限，输出错误
        return                                         #退出线程，进行详细报错

def ReadCRC(zipname):
    zip_url = "./" + zipname
    file_zip = zipfile.ZipFile(zip_url) #用zipfile读取指定的压缩包文件
    name_list = file_zip.namelist()     #使用一个列表，获取并存储压缩包内所有的文件名
    crc_list = []
    print('+--------------遍历指定压缩包的CRC值----------------+')
    for name in name_list:
        name_message = file_zip.getinfo(name)
        crc_list.append(hex(name_message.CRC))
        print('[OK] {0}: {1}'.format(name,hex(name_message.CRC)))
    print('+---------------------------------------------------+')
    crc32_list = str(crc_list)
    crc32_list = crc32_list.replace('\'' , '')
    print("读取成功，导出CRC列表为：" + crc32_list) #导出CRC列表后，导入其他脚本进行CRC碰撞
    
def OneByte(zipname):
    zip_url = "./" + zipname
    file_zip = zipfile.ZipFile(zip_url)    #用zipfile读取指定的压缩包文件
    name_list = file_zip.namelist()        #使用一个列表，获取并存储压缩包内所有的文件名
    crc_list = []
    crc32_list = []
    print('+--------------遍历指定压缩包的CRC值----------------+')
    for name in name_list:
        name_message = file_zip.getinfo(name)
        crc_list.append(name_message.CRC)
        crc32_list.append(hex(name_message.CRC))
        print('[OK] {0}: {1}'.format(name,hex(name_message.CRC)))
    print('+-------------对输出的CRC值进行碰撞-----------------+')
    comment = ''
    chars = string.printable
    for crc_value in crc_list:
        for char1 in chars:                              #获取任意1Byte字符
            thicken_crc = binascii.crc32(char1.encode()) #获取任意1Byte字符串的CRC32值
            calc_crc = thicken_crc & 0xffffffff          #将任意1Byte字符串的CRC32值与0xffffffff进行与运算
            if calc_crc == crc_value:                    #匹配两个CRC32值
                print('[Success] {}: {}'.format(hex(crc_value),char1))
                comment += char1
    print('+-----------------CRC碰撞结束！！！-----------------+')
    crc32_list = str(crc32_list)
    crc32_list = crc32_list.replace('\'' , '')
    print("读取成功，导出CRC列表为：" + crc32_list)                     #导出CRC列表
    if comment:
        print('CRC碰撞成功，结果为: {}'.format(comment))                  #输出CRC碰撞结果
    else:
        print('CRC碰撞没有结果，请检查压缩包内文件是否为1Byte！！！')

def TwoByte(zipname):
    zip_url = "./" + zipname
    file_zip = zipfile.ZipFile(zip_url)    #用zipfile读取指定的压缩包文件
    name_list = file_zip.namelist()        #使用一个列表，获取并存储压缩包内所有的文件名
    crc_list = []
    crc32_list = []
    print('+--------------遍历指定压缩包的CRC值----------------+')
    for name in name_list:
        name_message = file_zip.getinfo(name)
        crc_list.append(name_message.CRC)
        crc32_list.append(hex(name_message.CRC))
        print('[OK] {0}: {1}'.format(name,hex(name_message.CRC)))
    print('+-------------对输出的CRC值进行碰撞-----------------+')
    comment = ''
    chars = string.printable
    for crc_value in crc_list:
        for char1 in chars:
            for char2 in chars:
                res_char = char1 + char2                        #获取任意2Byte字符
                thicken_crc = binascii.crc32(res_char.encode()) #获取任意2Byte字符串的CRC32值
                calc_crc = thicken_crc & 0xffffffff             #将任意2Byte字符串的CRC32值与0xffffffff进行与运算
                if calc_crc == crc_value:                       #匹配两个CRC32值
                    print('[Success] {}: {}'.format(hex(crc_value),res_char))
                    comment += res_char
    print('+-----------------CRC碰撞结束！！！-----------------+')
    crc32_list = str(crc32_list)
    crc32_list = crc32_list.replace('\'' , '')
    print("读取成功，导出CRC列表为：" + crc32_list)                     #导出CRC列表
    if comment:
        print('CRC碰撞成功，结果为: {}'.format(comment))                  #输出CRC碰撞结果
    else:
        print('CRC碰撞没有结果，请检查压缩包内文件是否为2Byte！！！')

def ThreeByte(zipname):
    zip_url = "./" + zipname
    file_zip = zipfile.ZipFile(zip_url)    #用zipfile读取指定的压缩包文件
    name_list = file_zip.namelist()        #使用一个列表，获取并存储压缩包内所有的文件名
    crc_list = []
    crc32_list = []
    print('+--------------遍历指定压缩包的CRC值----------------+')
    for name in name_list:
        name_message = file_zip.getinfo(name)
        crc_list.append(name_message.CRC)
        crc32_list.append(hex(name_message.CRC))
        print('[OK] {0}: {1}'.format(name,hex(name_message.CRC)))
    print('+-------------对输出的CRC值进行碰撞-----------------+')
    comment = ''
    chars = string.printable
    result_dict={}
    for char1 in chars:
        for char2 in chars:
            for char3 in chars:
                res_char = char1 + char2 + char3                #获取任意3Byte字符
                thicken_crc = binascii.crc32(res_char.encode()) #获取任意3Byte字符串的CRC32值
                calc_crc = thicken_crc & 0xffffffff             #将任意3Byte字符串的CRC32值与0xffffffff进行与运算
                for crc_value in crc_list:
                    if calc_crc == crc_value:                       #匹配两个CRC32值
                        index = crc32_list.index(hex(crc_value))
                        num = int(index)
                        new_data = {num : res_char}
                        print('[Success] 第 {} 个文件 {}: {}'.format(num,hex(crc_value),res_char))
                        result_dict.update(new_data)
                        break
    sorted_items = sorted(result_dict.items())
    for key, res_char in sorted_items:
        comment += res_char
    print('+-----------------CRC碰撞结束！！！-----------------+')
    crc32_list = str(crc32_list)
    crc32_list = crc32_list.replace('\'' , '')
    print("读取成功，导出CRC列表为：" + crc32_list)                     #导出CRC列表
    if comment:
        print('CRC碰撞成功，结果为: {}'.format(comment))                  #输出CRC碰撞结果
    else:
        print('CRC碰撞没有结果，请检查压缩包内文件是否为3Byte！！！')

def FourByte(zipname):
    zip_url = "./" + zipname
    file_zip = zipfile.ZipFile(zip_url)    #用zipfile读取指定的压缩包文件
    name_list = file_zip.namelist()        #使用一个列表，获取并存储压缩包内所有的文件名
    crc_list = []
    crc32_list = []
    print('+--------------遍历指定压缩包的CRC值----------------+')
    for name in name_list:
        name_message = file_zip.getinfo(name)
        crc_list.append(name_message.CRC)
        crc32_list.append(hex(name_message.CRC))
        print('[OK] {0}: {1}'.format(name,hex(name_message.CRC)))
    print('+-------------对输出的CRC值进行碰撞-----------------+')
    comment = ''
    chars = string.printable
    result_dict={}
    for char1 in chars:
        for char2 in chars:
            for char3 in chars:
                for char4 in chars:
                    res_char = char1 + char2 + char3 + char4        #获取任意4Byte字符
                    thicken_crc = binascii.crc32(res_char.encode()) #获取任意4Byte字符串的CRC32值
                    calc_crc = thicken_crc & 0xffffffff             #将任意4Byte字符串的CRC32值与0xffffffff进行与运算
                    for crc_value in crc_list:
                        if calc_crc == crc_value:                       #匹配两个CRC32值
                            index = crc32_list.index(hex(crc_value))
                            num = int(index)
                            new_data = {num : res_char}
                            print('[Success] 第 {} 个文件 {}: {}'.format(num,hex(crc_value),res_char))
                            result_dict.update(new_data)
                            break
    sorted_items = sorted(result_dict.items())
    for key, res_char in sorted_items:
        comment += res_char
    print('+-----------------CRC碰撞结束！！！-----------------+')
    crc32_list = str(crc32_list)
    crc32_list = crc32_list.replace('\'' , '')
    print("读取成功，导出CRC列表为：" + crc32_list)                     #导出CRC列表
    if comment:
        print('CRC碰撞成功，结果为: {}'.format(comment))                  #输出CRC碰撞结果
    else:
        print('CRC碰撞没有结果，请检查压缩包内文件是否为4Byte！！！')

if __name__ == '__main__':
    title()
    parser = argparse.ArgumentParser(description="CRC-Tools V2.2", epilog='根据压缩包内容选择不同参数，诸如：python3 CRC-Tools.py -4 4Byte-Demo.zip 目前只支持1-4Byte的压缩包CRC碰撞')
    #parser = argparse.ArgumentParser(prog="CRC32-Tools", usage="开源项目[%(prog)s] 实现了如下功能：")
    parser.add_argument('-z', action='store', dest='readzip', help='读取对应压缩包，输出各个文件CRC值列表')
    parser.add_argument('-1', action='store', dest='onebyte', help='对1Byte的压缩包自动进行CRC碰撞并输出文件内容')
    parser.add_argument('-2', action='store', dest='twobyte', help='对2Byte的压缩包自动进行CRC碰撞并输出文件内容')
    parser.add_argument('-3', action='store', dest='threebyte', help='对3Byte的压缩包自动进行CRC碰撞并输出文件内容')
    parser.add_argument('-4', action='store', dest='fourbyte', help='对4Byte的压缩包自动进行CRC碰撞并输出文件内容')
    args = parser.parse_args()
    try:
        if args.readzip:
            FileRead(args.readzip)
            ReadCRC(args.readzip)
        if args.onebyte:
            FileRead(args.onebyte)
            OneByte(args.onebyte)
        if args.twobyte:
            FileRead(args.twobyte)
            TwoByte(args.twobyte)
        if args.threebyte:
            FileRead(args.threebyte)
            ThreeByte(args.threebyte)
        if args.fourbyte:
            FileRead(args.fourbyte)
            FourByte(args.fourbyte)
    except KeyboardInterrupt:
        print("Ctrl + C 手动终止了进程")
        sys.exit()
    except BaseException as e:
        err = str(e)
        print('脚本详细报错：' + err)
        sys.exit(0)
