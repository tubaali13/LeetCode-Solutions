class Solution {
public:
    int checkPalindrome(string s, int left, int right) {
        if( left < 0 || right > s.length() - 1 )
            return 0;
        else if( s[left] != s[right] )
            return 0;
        else 
            return (1 + checkPalindrome(s, left -1, right +1));
    }
    int countSubstrings(string s) {
        int count = 0;
        for( int i = 0; i < s.length(); i++ ) {

            //odd length
            count += checkPalindrome(s,i,i);

            //even length
            count += checkPalindrome(s,i,i+1);
        }

        return count;
    }
    
};