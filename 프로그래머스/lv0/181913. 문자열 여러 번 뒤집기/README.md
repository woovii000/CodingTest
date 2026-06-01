# [lv0] 문자열 여러 번 뒤집기 - 181913 

[문제 링크](https://programmers.co.kr/) 

### 성능 요약

메모리: 64.8 MB, 시간: 0.10 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

Empty

### 제출 일자

2026년 06월 01일 18:11:38

### 문제 설명

<p>문자열 <code>my_string</code>과 이차원 정수 배열 <code>queries</code>가 매개변수로 주어집니다. <code>queries</code>의 원소는 [s, e] 형태로, <code>my_string</code>의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. <code>my_string</code>에 <code>queries</code>의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>my_string</code>은 영소문자로만 이루어져 있습니다.</li>
<li>1 ≤ <code>my_string</code>의 길이 ≤ 1,000</li>
<li><code>queries</code>의 원소는 [s, e]의 형태로 0 ≤ s ≤ e &lt; <code>my_string</code>의 길이를 만족합니다.</li>
<li>1 ≤ <code>queries</code>의 길이 ≤ 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>queries</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"rermgorpsam"</td>
<td>[[2, 3], [0, 7], [5, 9], [6, 10]]</td>
<td>"programmers"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<ul>
<li>예제 1번의 <code>my_string</code>은 "rermgorpsam"이고 주어진 <code>queries</code>를 순서대로 처리하면 다음과 같습니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>queries</th>
<th>my_string</th>
</tr>
</thead>
        <tbody><tr>
<td></td>
<td>"rermgorpsam"</td>
</tr>
<tr>
<td>[2, 3]</td>
<td>"remrgorpsam"</td>
</tr>
<tr>
<td>[0, 7]</td>
<td>"progrmersam"</td>
</tr>
<tr>
<td>[5, 9]</td>
<td>"prograsremm"</td>
</tr>
<tr>
<td>[6, 10]</td>
<td>"programmers"</td>
</tr>
</tbody>
      </table><div class="highlight"><pre class="codehilite"><code>따라서 "programmers"를 return 합니다.
</code></pre></div>

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
