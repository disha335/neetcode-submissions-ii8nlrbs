public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        // string res = "";
        // for(int i=0; i<strs[0].Length;i++){
        //     foreach(string st in strs){
        //         if(i==st.Length || st[i]!=strs[0][i])
        //             return res;
        //     }
        //     res+=strs[0][i];
        // }
        // return res;
        Array.Sort(strs);
        string start = strs[0];
        string end = strs[strs.Length-1];
        for(int i=0;i<Math.Min(start.Length, end.Length);i++){
            if(start[i]!=end[i])
                return strs[0].Substring(0, i);
        }
        return strs[0];
    }
}