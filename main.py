import os
import Mailraffle


def main():
    url = 'https://jaychouxpsg.com/'
    target_route = r'D:\token\0 My Libraries\7.Multi_Mail\MailName\sum.txt'
    ts = Mailraffle.Mailraffle()
    f = open(target_route)
    lines = f.readlines()
    f.close
    for line in lines:
        mailaddr = line.split('|')[0] + '@buffermail.com'
        ts.mailinput(url, mailaddr)

if __name__ == '__main__':
    main()
