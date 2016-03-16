#include <iostream>
#include <string>
#include <assert.h>
using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        long result = 0;
        char fc = *str.begin();
        bool neg = false;
        bool started = false;
        int i = 0;
        for (string::iterator it = str.begin(); it!=str.end(); ++it) {
            if (isdigit(*it)) {
                result = result*10 + int(*it-'0');
                started = true;
                if (!neg && result > INT_MAX) {return INT_MAX;}
                if (neg && result > (unsigned)INT_MAX+1) {return INT_MIN;}
            } else if (!started && (*it == '+' || *it == '-')) {
                started = true;
                neg = (*it=='-');
                continue;
            } else if (*it==' ' && !started){
                continue;
            } else {
                break;
            }
        }
        return neg? -(int)result:(int)result;
    }
};

int main(int argc, char* argv[]) {
    Solution solution;
    int result = solution.myAtoi(argv[1]);
    cout << result << endl;


    //char a[] = {'a', '1'};
    //for (int i=0; i<(sizeof(a)/sizeof(*a)); ++i) {
    //    cout << a[i] << " : " << int(a[i]-'0') <<endl;
    //}
}
