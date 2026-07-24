public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> sMap = new Dictionary<char, int>();
        Dictionary<char, int> tMap = new Dictionary<char, int>();

        foreach(char ch in s){
            if(sMap.ContainsKey(ch))
                sMap[ch]++;
            else
                sMap[ch]=1;
        }
        foreach(char ch in t){
            if(tMap.ContainsKey(ch))
                tMap[ch]++;
            else
                tMap[ch]=1;
        }
        if(sMap.Count!=tMap.Count)
            return false;

        foreach(var pair in sMap){
            if(!tMap.ContainsKey(pair.Key)||(tMap[pair.Key]!=pair.Value)){
                return false;
            }
        }
        return true;
    }
}
