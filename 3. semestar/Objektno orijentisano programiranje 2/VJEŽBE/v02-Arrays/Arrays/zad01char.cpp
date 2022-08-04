#include <iostream>;

using namespace std;

void chars() {
	char c[4] = { 'a' , 'b', 'c', '\0' };
	char a[5] = "abcd";

	cout << strlen(a) << endl;
	for (int i = strlen(a); i >= 0; i--) {
		cout << a[i];
	}
}