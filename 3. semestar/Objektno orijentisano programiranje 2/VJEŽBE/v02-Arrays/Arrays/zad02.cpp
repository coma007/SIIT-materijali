#include <iostream>
#include <vector>
#define MAX_LENGTH 50

using namespace std;

vector<int> input() {

	vector<int> v;

	int size;
	cout << "Input size: ";
	cin >> size;

	int s;
	for (int i = 0; i < size; i++) {
		cout << "Input arr[" << i << "]: ";
		cin >> s;
		v.push_back(s);
	}

	return v;

}

void evenFirst() {
	
	// int arr[MAX_LENGTH];
	int size;
	cout << "Input size: ";
	cin >> size;
	int *arr = new int[size];
	for (int i = 0; i < size; i++) {
		cout << "Input arr[" << i << "]: ";
		cin >> arr[i];
	}
	cout << endl;
	for (int i = 0; i < size; i+=2) {
		cout << "arr[" << i << "] = " << arr[i] << endl;
	}
	for (int i = 1; i < size; i += 2) {
		cout << "arr[" << i << "] = " << arr[i] << endl;
	}
}