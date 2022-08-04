#include <iostream>

using namespace std;

void reverse(int arr[], int size) {

	for (int i = 0; i < size / 2; i++) {
		int tmp = arr[i];
		arr[i] = arr[size - 1 - i];
		arr[size - 1 - i] = tmp;
	}

}

void print(int arr[], int size) {

	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;

}

void printReversedArr() {

	int arr[] = { 1, 2, 3, 4, 5 };
	int size = sizeof(arr) / sizeof(arr[0]);

	cout << "Array: ";
	print(arr, size);

	reverse(arr, size);
	cout << "Reversed array: ";
	print(arr, size);


}