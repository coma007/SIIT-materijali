#include <iostream>;
#include <vector>;

using namespace std;

void oddEven() {
	
	vector<int> v;

	int size;
	cout << "Input size: ";
	cin >> size;

	int s;
	for (int i = 0; i < size; i++) {
		cout << "Input " << i << ". element: ";
		cin >> s;
		v.push_back(s);
	}

	int odd = 0, even = 0;

	for (int n : v) {
		if (n % 2 == 0) {
			even++;
		}
		else odd++;
	}

	cout << "Odd: " << odd << endl;
	cout << "Even: " << even << endl;

}