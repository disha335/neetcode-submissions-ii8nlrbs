public class Solution {
    public string MergeAlternately(string word1, string word2) {
        StringBuilder answer = new StringBuilder();
        int n1 = word1.Length;
        int n2 = word2.Length;
        int i=0, j=0;
        while(i<n1 && j<n2){
            answer.Append(word1[i]);
            answer.Append(word2[j]);
            i++;
            j++;
        }
        answer.Append(word1.Substring(i));
        answer.Append(word2.Substring(j));
        return answer.ToString();
    }
}