# Author: Lily Timmermans
# GitHub username: LilyTimmermans
# Date: 07/31/2023
# Description: This code squares values in a list.

def square_list(nums):
    """
    Square each value in the given list.

    Args:
        nums (list of int): Square the values of this list. The original list will be modified in-place.

    Returns:
        None
    """
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
