# coding=utf-8

import os
from base64 import b64decode
from datetime import date #year, month, day

import requests #HTTP客户端库

# 这里填写我之前发给你的 key
KEY = 'kvXPcFf4etzOkwTdOxZrDDfRA0ZooPowlxlbcpeG'


def check_in():
    data = {'secretkey': KEY}
    resp = requests.post('https://enjoyit.fun/api/checkin', data=data).json()

    print(resp['message'])

    resp_data = resp.get('data')
    if resp_data:
        if resp['status'] == 0:
            image = f"{resp_data['day']} 天 {date.today()}.jpg"
            with open(image, 'wb') as f:
                f.write(b64decode(resp_data['img']))
                os.startfile(img)
        days_detail = resp_data.get('days_detail')
        if days_detail:
            print("\n[签到状态(￣▽￣)]")
            for k, v in days_detail.items():
                print(f"第 {k} 天状态: {v['color']}, 详情: {v['detail']}")


def get_news():
    data = {'secretkey': KEY}
    resp = requests.post('https://enjoyit.fun/api/getnews', data=data).json()

    if resp['status'] == 0:
        print("[三三广播(●'◡'●)]")
        for k, v in resp['data']['msgs'].items():
            print(f'{k}. {v}')
    else:
        print(resp['message'])


def main():
    check_in()

    # 可根据自身情况，修改以下内容
    print(
        '\n[每日自省（￣︶￣）]\n'
        '1. 我今天是否做了与编程有关的事？\n'
        '   1.1 我今天留了多少时间给编程？\n'
        '2. 我今天是否做了一点三三布置的作业？\n'
        '   2.1 Microsoft To Do 是否存在已完成但没有勾掉的任务？\n'
    )

    get_news()


if __name__ == '__main__':
    main()
