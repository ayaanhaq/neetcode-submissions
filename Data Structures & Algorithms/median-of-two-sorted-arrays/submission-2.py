class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A=nums1
        B=nums2

        total=len(A)+len(B)
        half=total//2

        if len(A)>len(B):
            A,B=B,A

        left=0
        right=len(A)-1

        while True:
            midA=(left+right)//2
            midB=half-midA-2

            Aleft=A[midA] if midA>=0 else float('-infinity')
            Aright=A[midA+1] if (midA+1)<len(A) else float('infinity')
            Bleft=B[midB] if midB>=0 else float('-infinity')
            Bright=B[midB+1] if (midB+1)<len(B) else float('infinity')

            if Aleft<=Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+min(Aright,Bright)) /2
            elif Aleft>Bright:
                right=midA-1
            else:
                left=midA+1