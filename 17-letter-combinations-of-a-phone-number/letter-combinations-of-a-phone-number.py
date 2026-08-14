class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz", 
        }
        lgth = len(digits)
        val = []
        if lgth == 1:
            for i in nums[digits]:
                val.append(i)
        elif lgth == 2:
            op1 = digits[0]
            op2 = digits[1]
            for i in nums[op1]:
                for j in nums[op2]:
                    val.append(i+j)
        elif lgth == 3:
            op1 = digits[0]
            op2 = digits[1]
            op3 = digits[2]
            for i in nums[op1]:
                for j in nums[op2]:
                    for k in nums[op3]:
                        val.append(i+j+k)
        elif lgth == 4:
            op1 = digits[0]
            op2 = digits[1]
            op3 = digits[2]
            op4 = digits[3]
            for i in nums[op1]:
                for j in nums[op2]:
                    for k in nums[op3]:
                        for m in nums[op4]:
                            val.append(i+j+k+m)
        return val

            
            
        