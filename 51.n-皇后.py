#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[]
        res=[]
        for i in range(0,n):
            board.append(["."]*n)

        
        def is_vaild(board,row,col):
            n=len(board)
            
            #检查列的合法性
            for i in range(0,row):
                if board[i][col]=="Q":
                    return False
            
            # 检查左上方
            r=row-1
            c=col-1
            while r>=0 and c>=0:
                
                if board[r][c]=="Q":
                    return False
                r-=1
                c-=1
            
            #检查右上方
            r=row-1
            c=col+1
            while r>=0 and c<n:
                
                if board[r][c]=="Q":
                    return False
                r-=1
                c+=1            
            return True


        def back_track(board,row):
            if len(board)==row:
                n=[]
                for i in range(len(board)):
                    a=""
                    for j in range(len(board)):
                        a+=board[i][j]
                    n.append(a)
                res.append(n)
                print(n)
                return 

            n=len(board)
            for col in range(0,n):
                if is_vaild(board,row,col)==False:
                    continue

                board[row][col]="Q"
                back_track(board,row+1)
                board[row][col]="."
        
        back_track(board,0)
        return res
            


# @lc code=end

