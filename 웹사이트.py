from requests import get

websites = (
    "naver",
    "google",
    "tiktok",
    "youtube"
)

results = {}

for w in websites:
    if not w.startswith("https://") and not w.endswith(".com"):
        w = f"https://{w}.com"
        responce = get(w)
        res = int(responce.status_code/100)
        if res == 1:
            res = f"정보 응답: {responce.status_code}"
        elif res == 2:
            res = f"성공 응답: {responce.status_code}"
        elif res == 3:
            res = f"리다이렉션 메시지: {responce.status_code}"
        elif res == 4:
            res = f"클라이언트 에러 응답: {responce.status_code}"
        else:
            res = f"서버 에러 응답: {responce.status_code}"
        results[w] = res
        
print(results)