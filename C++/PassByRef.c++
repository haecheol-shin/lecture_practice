// a, b, c, d, e, f 변수 그냥 double로 두고 입력은 정수로
// 함수가 void타입으로 되어있는데 bool 타입으로 바꾸고 리턴값으로 해가 있는지 없는지 알려줘라 그리고 x, y값도 리턴해야된다
// 사용자는 a,b,c,d,e,f를 정수로 입력

#include <iostream>
using namespace std;
bool solveEquation(double a, double b, double c, double d, double e, double f, double& x, double& y); // 함수 선언

int main() {
	double a, b, c, d, e, f; // 변수 선언
	double x = 0; // 초기화
	double y = 0; // 초기화
	bool result; // 함수결과를 담을 변수 선언

	cout << "a: ";
	cin >> a;

	cout << "b: ";
	cin >> b;

	cout << "c: ";
	cin >> c;

	cout << "d: ";
	cin >> d;

	cout << "e: ";
	cin >> e;

	cout << "f: ";
	cin >> f;

	result = solveEquation(a, b, c, d, e, f, x, y); // 함수 호출 후 리턴 값을 result변수에 저장

	if (result == true) { // 함수 리턴 값이 true면 x, y를 리턴
		cout << "x: " << x << endl;
		cout << "y: " << y << endl;
	}

	else { // 함수 리턴 값이 false이면 문장 출력
		cout << "The equation has no solution." << endl;
	}

	return 0;
}

bool solveEquation(double a, double b, double c, double d, double e, double f, double& x, double& y) { // 함수 구현
	x = (e * d - b * f) / (a * d - b * c); 
	y = (a * f - e * c) / (a * d - b * c); // x, y는 passbyref이기 때문에 함수 실행 중 값이 변경되면 main에서도 값이 변경된다

	if ((a * d - b * c) == 0) {
		return false;
	}

	else {
		return true;
	}
}
