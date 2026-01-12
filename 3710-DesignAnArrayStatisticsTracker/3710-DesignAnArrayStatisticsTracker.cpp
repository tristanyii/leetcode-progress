// Last updated: 1/12/2026, 3:12:56 PM
class StatisticsTracker {
public:
    queue<int> added_nums;
    long long sum_nums = 0;
    int len = 0;
    map<int, int> num_to_freq;
    map<int, set<int>, greater<int>> freq_to_num;

    multiset<int, greater<int>> lower_half;
    multiset<int> upper_half;

    StatisticsTracker() {

    }

    void print() {
    }
    
    void addNumber(int number) {
        upper_half.insert(number);
        lower_half.insert(*upper_half.begin());
        upper_half.erase(upper_half.begin());

        if(lower_half.size() > upper_half.size()) {
            upper_half.insert(*lower_half.begin());
            lower_half.erase(lower_half.begin());
        }

        if(upper_half.size() - lower_half.size() > 1) {
            lower_half.insert(*upper_half.begin());
            upper_half.erase(upper_half.begin());
        }

        added_nums.push(number);
        len++;
        sum_nums += number;

        int old_count = num_to_freq[number];
        num_to_freq[number]++;

        if(old_count != 0) {
            freq_to_num[old_count].erase(number);
        }

        int new_count = old_count + 1;
        freq_to_num[new_count].insert(number);

        if(freq_to_num[old_count].empty()) {
            freq_to_num.erase(old_count);
        }

        print();
    }
    
    void removeFirstAddedNumber() {
        int number = added_nums.front();
        added_nums.pop();

        if(lower_half.count(number)) {
            lower_half.erase(lower_half.find(number));
        } else if(upper_half.count(number)) {
            upper_half.erase(upper_half.find(number));
        }

        if(lower_half.size() > upper_half.size()) {
            upper_half.insert(*lower_half.begin());
            lower_half.erase(lower_half.begin());
        }

        if(upper_half.size() - lower_half.size() > 1) {
            lower_half.insert(*upper_half.begin());
            upper_half.erase(upper_half.begin());
        }

        len--;
        sum_nums -= number;

        int old_count = num_to_freq[number];
        num_to_freq[number]--;

        freq_to_num[old_count].erase(number);

        int new_count = old_count - 1;

        if(new_count != 0) {
            freq_to_num[new_count].insert(number);
        }

        if(freq_to_num[old_count].empty()) {
            freq_to_num.erase(old_count);
        }

        print();
    }
    
    int getMean() {
        return sum_nums / len;
    }
    
    int getMedian() {
        return *upper_half.begin();
    }
    
    int getMode() {
        return *(freq_to_num.begin()->second.begin());
    }
};

/**
 * Your StatisticsTracker object will be instantiated and called as such:
 * StatisticsTracker* obj = new StatisticsTracker();
 * obj->addNumber(number);
 * obj->removeFirstAddedNumber();
 * int param_3 = obj->getMean();
 * int param_4 = obj->getMedian();
 * int param_5 = obj->getMode();
 */