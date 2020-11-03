#include <stdio.h>
#include <string>

class CMyString
{
    public:
        CMyString(char* str = NULL);
        CMyString(const CMyString& str);
        ~CMyString(void);
        CMyString& operator = (const CMyString& str);

        size_t size() const;
        const char* c_str() const;

    private:
        char* data;
        size_t length;
};


CMyString::CMyString(char* str) {
    if (!str) {
        length = 0;
        data = new char[1];
        *data = '\0';
    } else {
        length = strlen(str);
        data = new char[length + 1];
        strcpy(data, str);
    }
}

CMyString::CMyString(const CMyString& str) {
    length = str.size();
    data = new char[length+1];
    strcpy(data, str.c_str());
}

size_t CMyString::size() const{
    return length;
}

inline const char* CMyString::c_str() const{
    return data;
}

CMyString::~CMyString() {
    delete []data;
    length = 0;
}

int main(){
    CMyString str;
}
