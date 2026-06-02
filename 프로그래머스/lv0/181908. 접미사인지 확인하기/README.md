# [lv0] 접미사인지 확인하기 - 181908 

[문제 링크](https://programmers.co.kr/) 

### 성능 요약

메모리: 11.4 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 06월 02일 13:50:12

### 문제 설명

<p>어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.<br>
문자열 <code>my_string</code>과 <code>is_suffix</code>가 주어질 때, <code>is_suffix</code>가 <code>my_string</code>의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>is_suffix</code>의 길이 ≤ 100</li>
<li><code>my_string</code>과 <code>is_suffix</code>는 영소문자로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>is_suffix</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"banana"</td>
<td>"ana"</td>
<td>1</td>
</tr>
<tr>
<td>"banana"</td>
<td>"nan"</td>
<td>0</td>
</tr>
<tr>
<td>"banana"</td>
<td>"wxyz"</td>
<td>0</td>
</tr>
<tr>
<td>"banana"</td>
<td>"abanana"</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사이기 때문에 1을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사가 아니기 때문에 0을 return 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>예제 3번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사가 아니기 때문에 0을 return 합니다.</li>
</ul>

<p>입출력 예 #4</p>

<ul>
<li>예제 4번에서 <code>is_suffix</code>가 <code>my_string</code>의 접미사가 아니기 때문에 0을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---

## 🗒️ 풀이 노트

### ❌ 오답 기록

> 틀렸던 코드와 이유를 기록해두세요.

```python
# 오답 코드
```

### ✅ 정답 풀이

> 최종 정답 코드와 핵심 아이디어를 메모하세요.

```python
# 정답 코드
```

### 💡 새로 배운 개념

> 이 문제를 통해 새로 알게 된 함수, 문법, 패턴을 정리하세요.

-

### 🔁 헷갈렸던 부분

> 헷갈렸거나 실수하기 쉬운 부분을 기록하세요.

-

### 📌 다음에 기억할 것

> 다음에 비슷한 문제를 풀 때 떠올려야 할 핵심 포인트를 적어두세요.

-
