class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        result = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            max_points = 0
            
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    
                    # Ensure consistent representation
                    if dx < 0:
                        dx *= -1
                        dy *= -1
                
                slopes[(dx, dy)] += 1
                max_points = max(max_points, slopes[(dx, dy)])
            
            result = max(result, max_points + 1)
        
        return result
