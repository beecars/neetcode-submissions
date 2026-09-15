class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() !=t.size()) return false;    // not an anagram
        int counts[26] = {};                      // initialize array (zero)

        for (size_t i = 0; i < s.size(); ++i) {
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }

        for (int c : counts) {
            if (c != 0) return false;
        }

        return true;
    }
};