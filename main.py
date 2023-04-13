class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in Counter(nums).most_common(k)]
# i[0] to search from the first element and
# for i in Counter(nums) to find the count of repetitive numbers
#.most_common(k) functin used to find the k times of most repetitive numbers in the nums list
