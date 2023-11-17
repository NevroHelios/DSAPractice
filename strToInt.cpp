class Solution {
public:
    int myAtoi(string s) {
        int i = 0; int l = s.size();
        while(s[i] == ' '){
            i++;
        }

        int pos = 0; int neg = 0;
        if (s[i] == '-'){
            neg += 1;
            i++;
        }
        if (s[i] == '+'){
            pos += 1;
            i++;
        }

        double num = 0;
        while(i < l && s[i] >= '0' && s[i] <= '9'){
            num = num*10 + (s[i] - '0');
            i++;
        }

        if (neg > 0 and pos > 0){
            return 0;
        }
        if(neg > 0){
            num = -num;
        }


        if (num > INT_MAX){
            return INT_MAX;
        }
        if (num < INT_MIN){
            return INT_MIN;
        }
        
        return (int)num;
    }
};
