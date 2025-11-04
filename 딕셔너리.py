# 변경 가능

Man = {
    "name": "kimtaejung",
    "age": 22,
    "hometown": "ChunCheon",
    "interesting": ["study", "soccer", "game"]
}

Man.update({"hobby": "gmae"})  # 다른 딕셔너리와 병합

Man.popitem()  # 마지막 키-값 제거하며 반환

Man.pop("age")  # 해당 키-값 제거하며 반환

Man.clear()  # 전부 제거

Man.keys()  # 모든 키 반환
Man.values()  # 모든 값 반환

Man["School"] = "Hallym"  # 키-값 추가

Man["interesting"].append("Gold")  # 해당 키가 리스트 구조기 때문에 append로 추가

print(Man.get("interesting", "default"))  # 해당 키의 값 출력 없으면 default 출력