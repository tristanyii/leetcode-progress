// Last updated: 1/12/2026, 3:13:00 PM
struct Task {
    int userId;
    int taskId;
    int priority;
};

class TaskManager {
public:
    TaskManager(vector<vector<int>>& tasks) {
        for(const vector<int>& task : tasks) {
            int userId = task[0], taskId = task[1], priority = task[2];
            add(userId, taskId, priority);
        }
    }
    
    void add(int userId, int taskId, int priority) {
        userid_to_tasks[userId].push_back({userId, taskId, priority});
        taskid_to_task[taskId] = prev(userid_to_tasks[userId].end());
        priority_to_taskid[priority].insert(taskId);
    }
    
    void edit(int taskId, int newPriority) {
        auto it = taskid_to_task[taskId];
        priority_to_taskid[it->priority].erase(taskId);
        if(priority_to_taskid[it->priority].empty()) {
            priority_to_taskid.erase(it->priority);
        }
        priority_to_taskid[newPriority].insert(taskId);
        it->priority = newPriority;
    }
    
    void rmv(int taskId) {
        auto it = taskid_to_task[taskId];
        priority_to_taskid[it->priority].erase(taskId);
        if(priority_to_taskid[it->priority].empty()) {
            priority_to_taskid.erase(it->priority);
        }
        userid_to_tasks[it->userId].erase(it);
    }

    void print() {
        // for(auto &x : priority_to_taskid) {
        //     cout << x.first << ": ";
        //     for(auto &y : x.second) {
        //         cout << y << " ";
        //     }
        //     cout << "\n";
        // }
        // cout << "\n\n";
    }
    
    int execTop() {
        if(priority_to_taskid.empty()) {
            return -1;
        }
        int taskId = *priority_to_taskid.begin()->second.begin();

        auto it = taskid_to_task[taskId];

        int userId = it->userId;
        priority_to_taskid[it->priority].erase(taskId);
        if(priority_to_taskid[it->priority].empty()) {
            priority_to_taskid.erase(it->priority);
        }
        userid_to_tasks[userId].erase(it);

        return userId;
    }

private:
    unordered_map<int, list<Task>> userid_to_tasks;
    unordered_map<int, list<Task>::iterator> taskid_to_task;
    map<int, set<int, greater<int>>, greater<int>> priority_to_taskid;
};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
 */