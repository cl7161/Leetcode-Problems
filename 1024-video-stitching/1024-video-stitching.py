class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        clips.sort()

        if clips[0][0] != 0:
            return -1
        
   
        e = 0
        max_e = 0
        count = 0

        for i,j in clips:
            if (i <= e) and (j > max_e):
                max_e = j

                if max_e >= time:
                    count += 1
                    return count
            
            elif (i <= e) and (j <= max_e):
                continue

            elif i <= max_e:
                count += 1
                e = max_e
                max_e = j

                if max_e >= time:
                    count += 1
                    return count
                
            elif i > max_e:
                return -1

        return -1

