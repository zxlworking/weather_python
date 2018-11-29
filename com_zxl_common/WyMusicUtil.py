#!/usr/bin/env python
# coding=utf-8
import base64
import binascii
import json
import random
import urllib2

import requests

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from string import ascii_letters, digits

from selenium import webdriver


# reload(sys)
# sys.setdefaultencoding("utf8")


class WyMusicUtil:
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'music.163.com',
        'Origin': 'http://music.163.com',
        'Referer': 'http://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }

    _charset = ascii_letters + digits

    def rand_char(self, num=16):
        return ''.join(random.choice(self._charset) for _ in range(num))

    def aes_encrypt(self, msg, key, iv='0102030405060708'):
        def padded(msg):
            pad = 16 - len(msg) % 16
            return msg + pad * chr(pad)

        msg = padded(msg)
        cryptor = AES.new(key, IV=iv, mode=AES.MODE_CBC)
        text = cryptor.encrypt(msg)
        text = base64.b64encode(text)
        return text

    def gen_params(self, d, i):
        text = self.aes_encrypt(d, '0CoJUm6Qyw8W8jud')
        text = self.aes_encrypt(text, i)
        return text

    def rsa_encrypt(self, msg):
        cryptor = RSA.construct((
                                0x00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7,
                                0x10001L))
        text = cryptor.encrypt(msg[::-1], '')[0]
        text = binascii.b2a_hex(text)
        return text

    def encrypt(self, query):
        query = json.dumps(query)
        rand_i = self.rand_char(16)
        params = self.gen_params(query, rand_i)
        enc_sec_key = self.rsa_encrypt(rand_i)
        data = {
            'params': params,
            'encSecKey': enc_sec_key
        }
        return data

    def search_music_by_name(self, name):
        # data-type="1"  歌手
        # data - type = "10" 专辑
        # data - type = "1014" 视频
        # data - type = "1006" 歌词
        # data - type = "1000" 歌单
        # data - type = "1009" 主播电台
        # data - type = "1002" 用户

        url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='

        query = {
            "id": "2060011116",
            "s": name,
            "type": "1",
            "offset": "0",
            "total": "false",
            "limit": "2"
        }
        data = self.encrypt(query)

        r = requests.post(url, data=data, headers=self.headers)
        print(r.content)

    def get_music_lrc(self, id):
        url = 'https://music.163.com/weapi/song/lyric?csrf_token='

        query = {
            "id": "440207429", "lv": -1, "tv": -1
        }
        data = self.encrypt(query)

        r = requests.post(url, data=data, headers=self.headers)
        print(r.content)

    def get_music_comment(self, id):
        url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token=' % id

        query = {
            "rid": "R_SO_4_%s" % id,
            "offset": "0",
            "total": "true",
            "limit": "20",
        }
        data = self.encrypt(query)

        r = requests.post(url, data=data, headers=self.headers)
        print(r.content)

    def get_music_play_url(self, id):
        url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='

        query = {
            "ids": "[%s]" % id,
            "br": 128000,

        }
        data = self.encrypt(query)

        r = requests.post(url, data=data, headers=self.headers)
        print(r.content)
