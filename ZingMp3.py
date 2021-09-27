import hashlib
import hmac
import urllib
import requests
import datetime

class ZingMp3:
    api_key = "kI44ARvPwaqL7v0KuDSM0rGORtdY1nnw"
    secret_key = "882QcNXV4tUZbvAsjmFOHqNC1LpcBRKW"
    url_api = "https://zingmp3.vn"
    cookies = None

    @classmethod
    def getFullInfo(cls, id):
        data = cls.requestZing("/api/v2/song/get/info", {"id": id})
        data["streaming"] = cls.requestZing("/api/v2/song/get/streaming", {"id": id})
        return data

    @classmethod
    def getRecommendSongs(cls, id):
        return cls.requestZing("/api/v2/recommend/get/songs", {"id": id})

    @classmethod
    def getDetailPlaylist(cls, id):
        return cls.requestZing("/api/v2/page/get/playlist", {"id": id})

    @classmethod
    def getInfoMusic(cls, id):
        return cls.requestZing("/api/v2/song/get/info", {"id": id})

    @classmethod
    def getStreaming(cls, id):
        return cls.requestZing("/api/v2/song/get/streaming", {"id": id})

    @classmethod
    def getHome(cls, page=1):
        return cls.requestZing("/api/v2/page/get/home", {"page": page})

    @classmethod
    def getCookie(cls):
        if not cls.cookies:
            r = requests.get(cls.url_api)
            cls.cookies = dict(r.cookies)
        return cls.cookies

    @classmethod
    def hashParam(cls, path, param=""):

        hash256 = hashlib.sha256(param.encode("utf8")).hexdigest()
        sig = hmac.new(
            cls.secret_key.encode("utf8"),
            msg=f"{path}{hash256}".encode("utf8"),
            digestmod=hashlib.sha512
        ).hexdigest()

        return sig

    @classmethod
    def requestZing(cls, path, qs):
        cls.getCookie()
        ctime = int(datetime.datetime.now().timestamp())
        param = {
            "ctime": ctime
        }
        param.update(qs)
        param = urllib.parse.urlencode(param).replace("&", "")
        sig = cls.hashParam(path, param)
        params = {
            "ctime": ctime,
            "sig": sig,
            "apiKey": cls.api_key
        }
        params.update(qs)
        r = requests.get(cls.url_api + path, params=params, cookies=cls.cookies)
        
        r = r.json()
        if r["err"] != 0:
            raise Exception(r["msg"])

        return r["data"]
