#include <string>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        int size = s.length();
        numRows = 3;
        string res = "";
        int rest = s.length()%numRows;
        for (int i=0; i<numRows; ++i) {
            // supports i is oval
            int times =  size/(numRows+1);
            for (int j=0; j< + size%(numRows+1)%2;++j) {
                res += s[j*4+i];
            }
        }

        return "";
    }
};

int main(int argc, char* argv[]) {
}
