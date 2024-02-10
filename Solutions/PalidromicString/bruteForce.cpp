class Solution {
public:
    bool checkPalindrome(string s) {
        int l = 0,  r = s.length() - 1;

        while( l < r ) {
            if( s[l] != s[r] )
                return false;
            l++;
            r--;
        }
        return true;
    }
    int countSubstrings(string s) {
        int count = 0;

        for( int i = 0; i < s.length(); i++ ) {
            string temp = "";
            temp += s[i];
            if( checkPalindrome(temp))
                    count++;
            for( int j = i+1; j < s.length(); j++ ) {
                temp += s[j];
                if( checkPalindrome(temp))
                    count++;
                
            }
        }

        return count;

    }
};