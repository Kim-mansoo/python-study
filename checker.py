import sys
# 암묵적 형변환, 자동 형변환 => 파이썬이 데이터의 형태를 지정하지 않아도 되는 이유
# 실행 코드는 무조건 밑에 위치하기

def main(arrays):
    flag = True  # flag는 반드시 True or False
    for index, number in enumerate(arrays, start=1): # enumerate는 인덱스를 부여하는 함수?? 기능??, start 인자를 주면 해당 값부터 시작
        if number % 2 == 0:
            continue
        else:
            print(f"{index}"+ "번째 숫자" + f"{number}" + "은 짝수가 아닙니다")
            # f는 number를 넣으라는 뜻
            flag = False
            break

def extract_even_list(arrays):
    even_list = []
    for index, number in enumerate(arrays):
        if number % 2 == 0:
            even_list.append(number)
    print(even_list + [16, 18]) # 자바에서는 array라고 부름
    # [16, 18] 추가하는 식으로 하면 안됨

def extract_even_set(arrays):
    even_set = set()
    for index, number in enumerate(arrays):
        if number % 2 == 0:
            even_set.add(number)
    print(even_set)

def extract_even_dict(arrays):
    even_dict = {"index": [], "number": []}
    for index, number in enumerate(arrays):
        if number % 2 == 0:
            even_dict["index"].append(index)
            even_dict["number"].append(number)
    print(even_dict)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python checker.py <1 2 3 4 5 6 7>")
        sys.exit(1)
    else:
        arrays = list(map(int, sys.argv[1:])) # argument의 약자
    # list를 int로 받겠다는 뜻
        extract_even_dict(arrays)

## json은 순서가 없음
## commit 메세지 작성 규칙도 존재
## 포트폴리오 제출 시 이것도 고려를 해야 됨