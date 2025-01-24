#include <iostream>
using namespace std;

int main() {
    int n = 4;
    for (int i = 0; i < n; i++) { 
        // Corrected the inner loop condition
        for (int j = 0; j < n - i - 1; j++) { 
            cout << " ";
        }
        for (int j = 1; j <= i + 1; j++) { 
            cout << j;
        }
        // Corrected the inner loop condition and initialization
        for (int j = i; j > 0; j--) { 
            cout << j;
        }
        cout << endl;
    }
    return 0; // Added return statement
}