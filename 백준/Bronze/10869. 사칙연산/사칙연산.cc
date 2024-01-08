#define _CRT_SECURE_NO_WARNINGS
#include <iostream> // 전처리 지시자
#include <climits>
#include <cstring>
#include <cstdio>
// 이렇게 상수를 정의할 수 있다. 이는 c스타일
/*
c++ 에서 함수를 사용하고자 한다면, 함수의 원형을 미리 정의하여야 한다,
*/

using namespace std;

int main() {
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d\n", a + b);
	printf("%d\n", a - b);
	printf("%d\n", a * b);
	printf("%d\n", a / b);
	printf("%d\n", a % b);
	return 0;
}



