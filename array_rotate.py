def solution(A, K):
    # if the size of k > len(A), rotate only necessary with
   # module of the division

   rotations = K % len(A)
   return A[-rotations:] + A[:-rotations]


print(solution([1, 2, 3, 6], 3))
