class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> result(n, vector<int>(n));
        int op = 1;
        for (int k = 0; k < n / 2; k++) {
            for (int i = k; i < n - k - 1; i++) {
                result[k][i] = op++;
            }
            for (int i = k; i < n - k - 1; i++) {
                result[i][n - k - 1] = op++;
            }
            for (int i = n - 1 - k; i > k; i--) {
                result[n - 1 - k][i] = op++;
            }
            for (int i = n - 1 - k; i > k; i--) {
                result[i][k] = op++;
            }
        }
        if (n % 2 == 1) {
            result[n / 2][n / 2] = op;
        }
        return result;
    }
};