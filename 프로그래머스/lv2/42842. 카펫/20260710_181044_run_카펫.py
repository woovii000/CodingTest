def solution(brown, yellow):
    # g*s 형태(g >= s) -> 조합 찾기
    # 카펫 패턴 - i**2 , n*m -> 무의미
    carpet = brown + yellow
    
    pattern = []
    # 타일 수 패턴
    for i in range(carpet):
        if carpet//i >= i:
            pattern.append((i,carpet//i))
    
    # 색 조건
    for se, ga in answer:
        if (ga-2)*(se-2)==yellow:
            return [ga, se]
    # => 약수 조합(ga * se == carpet) 찾기