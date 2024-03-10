'''
Anish and Binish are playing a game. They both have to pick 'n' stones of varying sizes with non-duplicates and give their set of stones to the other. 
They have to sort these stones in increasing order but are allowed to do just one operation on them that is they can swap any adjacent stones with each other.
The one who sorts their set of stones with the least number of swaps wins. You are given two arrays named 'Anish' and 'Binish' representing the size of stones that they have to sort.
Determine the winner of the game.

Note: If the game is a tie print out "Tie".

Sample Input:
5

7 2 8 9 5

4 6 2 5 3
Sample Output:
Anish
Constraints:
1<=n<=1000

1<=s[i]<=10^5

'''


class Solution:
    def game(self, a, b, n):
        #Write your code here;
        def Sort(arr,n):
            x=0
            for i in range(n):
                for j in range(0,n-i-1):
                    if arr[j]>arr[j+1]:
                        arr[j],arr[j+1] = arr[j+1],arr[j]
                        x+=1
            return x
        Anish = Sort(a,n)
        Binish = Sort(b,n)
        if Anish<Binish:
          return("Anish")
        elif Anish == Binish:
          return("Tie")
        else:
          return("Binish")
s = Solution()
print(s.game([7, 2, 8, 9, 5], [4, 6, 2, 5, 3], 5))