#include <iostream>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        if (x==0x00000000)
            return 0;
        bool neg = false;
        if (x<0) {
            neg=true;
            x=-x;
            cout << x << endl;
        }
        cout << x << endl;
        long num = 0;
        while(x/10) {
            num = num*10 + x%10;
            x = x/10;
        }
        num = num*10 + x;
        if (num>0x7fffffff){
            return 0;
        }
        if (neg)
            return (int)-num;
        else
            return (int)num;
    }
};

int main(int argc, char *argv[]) {
    Solution solution;
    cout << solution.reverse(atoi(argv[1])) << endl;
}
