# 121. Best Time to Buy and Sell Stock

<div align="center">

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Arrays](https://img.shields.io/badge/Topic-Arrays-blue)
![Dynamic Programming](https://img.shields.io/badge/Topic-Dynamic%20Programming-orange)

</div>

---

## 📋 Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the **maximum profit** you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

### Example 2:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

### Constraints:
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## 💡 Approach

### My Thinking Process

When I first saw this problem, I thought about checking every possible buy-sell pair, but that would be O(n²) - too slow!

**The key insight**: As we go through the array, we only need to track:
1. The **minimum price** we've seen so far (best day to buy)
2. The **maximum profit** we can make

For each price, we:
- Calculate profit if we sell today: `current_price - min_price`
- Update our maximum profit if this is better
- Update minimum price if current price is lower

This way, we only need **one pass** through the array!

### Why This Works

We're essentially asking at each day: "If I sell today, what's the best profit I can get?" and keeping track of the best answer.

---

## 📝 Solution

### Python Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate maximum profit from single buy-sell transaction.
        
        Time Complexity: O(n) - single pass
        Space Complexity: O(1) - only two variables
        """
        # Edge case: empty or single price
        if not prices or len(prices) < 2:
            return 0
        
        # Track minimum price seen so far (best buy day)
        min_price = prices[0]
        # Track maximum profit found
        max_profit = 0
        
        # Iterate through each price
        for price in prices[1:]:
            # Calculate profit if we sell at current price
            potential_profit = price - min_price
            
            # Update max profit if we found a better one
            max_profit = max(max_profit, potential_profit)
            
            # Update min price if current price is lower
            min_price = min(min_price, price)
        
        return max_profit
```

### Alternative Python Solution (More Concise)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
```

### JavaScript Solution

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;
    
    for (let price of prices) {
        minPrice = Math.min(minPrice, price);
        maxProfit = Math.max(maxProfit, price - minPrice);
    }
    
    return maxProfit;
};
```

---

## 📊 Complexity Analysis

| Metric | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(n) | Single pass through prices array |
| **Space** | O(1) | Only using two variables regardless of input size |

### Comparison with Brute Force

| Approach | Time | Space | Why |
|----------|------|-------|-----|
| Brute Force | O(n²) | O(1) | Check all pairs |
| Optimal (Ours) | O(n) | O(1) | Single pass with tracking |

---

## 🧪 Test Cases

```python
# Test Case 1: Profit possible
prices = [7, 1, 5, 3, 6, 4]
# Expected: 5 (buy at 1, sell at 6)

# Test Case 2: No profit possible
prices = [7, 6, 4, 3, 1]
# Expected: 0 (prices only decrease)

# Test Case 3: Buy and sell on consecutive days
prices = [2, 4, 1]
# Expected: 2 (buy at 2, sell at 4)

# Test Case 4: Single price
prices = [5]
# Expected: 0 (can't make any transaction)

# Test Case 5: All same prices
prices = [3, 3, 3, 3]
# Expected: 0 (no profit to be made)

# Test
