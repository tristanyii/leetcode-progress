// Last updated: 1/12/2026, 3:12:45 PM
class Router {
public:
    Router(int memoryLimit) {
        m_limit = memoryLimit;
    }
    
    bool addPacket(int source, int destination, int timestamp) {
        if(m_haspackets.count({source, destination, timestamp})) {
            return false;
        }
        if(m_packets.size() == m_limit) {
            int pop_src = m_packets.front()[0];
            int pop_dest = m_packets.front()[1];
            int pop_time = m_packets.front()[2];

            m_packets.pop_front();
            m_dest_packets[pop_dest].pop_front();
            m_haspackets.erase(m_haspackets.find({pop_src, pop_dest, pop_time}));
        }

        m_packets.push_back({source, destination, timestamp});
        m_dest_packets[destination].push_back({source, destination, timestamp});
        m_haspackets.insert({source, destination, timestamp});

        return true;
    }
    
    vector<int> forwardPacket() {
        if(m_packets.empty()) {
            return {};
        }

        int pop_src = m_packets.front()[0];
        int pop_dest = m_packets.front()[1];
        int pop_time = m_packets.front()[2];
        
        m_packets.pop_front();
        m_dest_packets[pop_dest].pop_front();
        m_haspackets.erase(m_haspackets.find({pop_src, pop_dest, pop_time}));

        return {pop_src, pop_dest, pop_time};
    }

    int getIndexLast(int time, const deque<vector<int>>& packets) {
        int l = 0, r = packets.size();
        while(l < r) {
            int mid = (l + r) / 2;
            if(packets[mid][2] <= time) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }

    int getIndexFirst(int time, const deque<vector<int>>& packets) {
        int l = 0, r = packets.size();
        while(l < r) {
            int mid = (l + r) / 2;
            if(packets[mid][2] < time) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }
    
    int getCount(int destination, int startTime, int endTime) {
        int l = getIndexFirst(startTime, m_dest_packets[destination]);
        int r = getIndexLast(endTime, m_dest_packets[destination]);

        if(l == r) {
            return 0;
        }

        return r - l;
    }

private:
    int m_limit;
    deque<vector<int>> m_packets;
    unordered_map<int, deque<vector<int>>> m_dest_packets;
    set<vector<int>> m_haspackets;
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */