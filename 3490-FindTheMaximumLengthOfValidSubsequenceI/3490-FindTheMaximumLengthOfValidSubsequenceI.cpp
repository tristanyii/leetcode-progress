// Last updated: 1/12/2026, 3:13:19 PM
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int numAlternatingEndingOdd = 0;
        int numAlternatingEndingEven = 0;
        int numEvens = 0;
        int numOdds = 0;

        for(int x : nums) {
            if(x % 2 == 0) {
                numEvens++;
                numAlternatingEndingEven = numAlternatingEndingOdd + 1;
            } else {
                numOdds++;
                numAlternatingEndingOdd = numAlternatingEndingEven + 1;
            }
        }

        return max({numAlternatingEndingEven, numAlternatingEndingOdd, numEvens, numOdds});
    }
};

/*
you need either all evens, all odds, or alternating evens and odds

1, 1, 0, 1, 0, 1, 0, 0
odd = 1
even = 2
*/