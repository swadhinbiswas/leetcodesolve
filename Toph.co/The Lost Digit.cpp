#include <iostream>
#include <vector>
#include <numeric> // For std::iota (optional, for alternative input)

using namespace std;

int single_number(const vector<int>& number) {
    int answer = 0;
    for (int i : number) {  // Range-based for loop
        answer ^= i;
    }
    return answer;
}

int main() {
    int test;
    cin >> test;

    vector<int> numberlist(test); // Initialize vector with size 'test'

    for (int i = 0; i < test; ++i) {
        cin >> numberlist[i];
    }


    int x = single_number(numberlist);
    cout << x << endl;

    return 0;
}