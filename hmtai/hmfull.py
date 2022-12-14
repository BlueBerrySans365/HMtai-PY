import requests as r
import json

class hmfull:
    def hmtai(category):
        res = r.get(f"https://hmtai.hatsunia.cfd/v2/{category}")
        if "message" in res.json():
            return 0
        else:
            return res.json()["url"]

    def nekos(category):
        blacklist = ['https://cdn.nekos.life/blowjob/blowjob31.jpg', 'https://cdn.nekos.life/blowjob/blowjob32.jpg', 'https://cdn.nekos.life/lewdkemo/lewd_neko_v2_132.jpg', 'https://cdn.nekos.life/Random_hentai_gif/Random_hentai_gifNB_1039.gif']
        res = r.get(url=f"https://nekos.life/api/v2/img/{category}")
        res = json.loads(res.text)
        if "msg" in res:
            return 0
        if res["url"] in blacklist:
            return hmfull.nekos(category)
        return res["url"]

    def nekobot(category):
        blacklist = ['https://i0.nekobot.xyz/0/2/9/1b50d3f619f1bafdf114a530a2570.jpg', 'https://cdn.nekobot.xyz/9/3/9/448bb2ff69b3457a82f32ecd31c06.jpg', 'https://i0.nekobot.xyz/4/9/3/3b6ccf0c081db887fbe38038af996.jpg', 'https://i0.nekobot.xyz/8/6/9/ee21a6ac7d06aabf0b71691e6dfb5.jpg', 'https://cdn.nekobot.xyz/b/4/d/c1fdf4234fbfba326fb282de9ef8c.jpg', 'https://cdn.nekobot.xyz/b/4/d/c1fdf4234fbfba326fb282de9ef8c.jpg']
        res = r.get(f"https://nekobot.xyz/api/image?type={category}")
        if not res.status_code == 200:
            return print('This endpoint don\'t work, or you got a Rate Limit')
        if res.json()["success"] == "false":
            return 0
        if res.json()["message"] in blacklist:
            return hmfull.nekobot(category)
        return res.json()["message"]

    def freaker(category):
        return print('Freaker is not supported for now.')

    def nekolove(category):
        res = r.get(f"https://neko-love.xyz/api/v1/{category}")
        if "message" in res.json():
            return 0
        else:
            return res.json()["url"]
