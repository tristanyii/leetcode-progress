// Last updated: 1/12/2026, 3:12:51 PM
class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        vector<pair<int, int>> meetings;
        meetings.push_back({0, 0});
        for(int i = 0; i < (int) startTime.size(); i++) {
            meetings.push_back({startTime[i], endTime[i]});
        }
        meetings.push_back({eventTime, eventTime});

        sort(meetings.begin(), meetings.end());

        vector<int> gaps;
        for(int i = 1; i < meetings.size(); i++) {
            gaps.push_back(meetings[i].first - meetings[i - 1].second);
        }

        deque<int> slidingWindow;
        int curSlidingWindowSum = 0;
        int maxSum = 0;

        for(int i = 0; i <= k; i++) {
            slidingWindow.push_back(gaps[i]);
            curSlidingWindowSum += gaps[i];
        }

        maxSum = max(maxSum, curSlidingWindowSum);

        for(int i = k + 1; i < gaps.size(); i++) {
            curSlidingWindowSum -= slidingWindow.front();
            slidingWindow.pop_front();

            curSlidingWindowSum += gaps[i];
            slidingWindow.push_back(gaps[i]);

            maxSum = max(maxSum, curSlidingWindowSum);
        }

        return maxSum;
    }
};