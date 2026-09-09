class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        seen.reserve(nums.size());
        for (int n : nums) {
            auto [it, inserted] = seen.insert(n);
            if (!inserted) return true;
        }
        return false;
    }
};