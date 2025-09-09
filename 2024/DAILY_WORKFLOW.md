# Daily Advent of Code Workflow

## Quick Start Checklist
- [ ] Create `dayXX/` folder
- [ ] Copy template and rename to `dayXX.py`
- [ ] Read problem and fill in template placeholders
- [ ] Download input data to `input.txt`
- [ ] Implement and test Part 1
- [ ] Implement and test Part 2
- [ ] Run final validation

## Step-by-Step Instructions

### 1. Setup New Day
```bash
# Create folder for new day (replace XX with day number)
mkdir day{XX}
cd day{XX}

# Copy template
cp ../template_dayXX.py day{XX}.py
```

### 2. Initial Template Customization

Open `dayXX.py` and fill in these placeholders:

**Header Section:**
- `[PROBLEM_TITLE]` → Actual problem title from AoC
- `[BRIEF_DESCRIPTION_OF_PROBLEM]` → 1-2 sentence summary
- `[INSIGHT_1/2/3]` → Key observations about the problem
- `[APPROACH_DESCRIPTION]` → High-level strategy for each part
- `[COMPLEXITY]` → Expected time/space complexity

**Test Data:**
- `[PASTE_TEST_DATA_HERE]` → Copy example from problem description

### 3. Problem Analysis Framework

Before coding, answer these questions:

**Input Understanding:**
- What format is the input? (grid, list, structured text, etc.)
- What are the constraints? (size limits, value ranges)
- Are there edge cases to consider?

**Problem Classification:**
- [ ] Grid/2D traversal
- [ ] Graph problem (BFS/DFS)
- [ ] Dynamic programming
- [ ] String parsing/regex
- [ ] Mathematical/algorithmic
- [ ] Simulation
- [ ] Combinatorics

**Strategy Selection:**
- What's the most straightforward approach?
- Are there any obvious optimizations needed?
- How might Part 2 extend Part 1?

### 4. Implementation Process

**Phase 1: Parse Input**
1. Implement `parse_input()` function
2. Test with sample data
3. Ensure data structure fits the problem

**Phase 2: Part 1**
1. Implement basic algorithm in `solve_part1()`
2. Test with sample data first
3. Add educational comments explaining the approach
4. Validate against expected test result

**Phase 3: Part 2**
1. Read Part 2 requirements
2. Identify how it differs from Part 1
3. Implement in `solve_part2()`
4. Test and validate

**Phase 4: Real Data**
1. Download input from AoC to `input.txt`
2. Run both parts on real data
3. Submit answers

### 5. Educational Enhancement

For each solution, include:

**Algorithm Explanation:**
- Why this approach over alternatives?
- What CS concepts does it demonstrate?
- Time/space complexity analysis

**Python-Specific Features:**
- Built-in functions used and why
- Data structures chosen and their benefits
- Any elegant Python idioms

**Real-World Applications:**
- Where might this algorithm be useful?
- What industry problems use similar techniques?

### 6. Common Patterns & Solutions

**Grid Problems:**
```python
# Standard grid setup
grid = [list(line) for line in lines]
height, width = len(grid), len(grid[0])

# Direction vectors
directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
diagonals = [(1,1), (1,-1), (-1,1), (-1,-1)]

# Bounds checking
def in_bounds(r, c):
    return 0 <= r < height and 0 <= c < width
```

**BFS Template:**
```python
from collections import deque

def bfs(start, grid):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited and is_valid(neighbor):
                visited.add(neighbor)
                queue.append(neighbor)
```

**Dynamic Programming:**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(state):
    # Base case
    if is_base_case(state):
        return base_result
    
    # Recursive case
    result = 0
    for next_state in get_next_states(state):
        result += solve(next_state)
    
    return result
```

### 7. Debugging Strategies

**When Stuck:**
1. Print intermediate results to understand data flow
2. Test with minimal custom examples
3. Check boundary conditions
4. Verify input parsing is correct
5. Compare with problem description step-by-step

**Performance Issues:**
1. Profile with small inputs first
2. Look for nested loops that could be optimized
3. Consider using sets instead of lists for lookups
4. Cache expensive computations

**Common Mistakes:**
- Off-by-one errors in indexing
- Not handling empty/single-element inputs
- Misunderstanding problem constraints
- Forgetting to handle negative numbers or zero

### 8. Optimization Checklist

After getting correct solution:
- [ ] Can any loops be eliminated?
- [ ] Are there redundant calculations?
- [ ] Could sets replace list searches?
- [ ] Would caching help with repeated computations?
- [ ] Are there mathematical shortcuts?

### 9. Final Validation

Before submitting:
- [ ] Test data produces expected results
- [ ] Real data runs without errors
- [ ] Code is well-commented and educational
- [ ] Performance is acceptable
- [ ] Edge cases are handled

### 10. Template Customization Tips

**For specific problem types:**

**String/Parsing Problems:**
```python
import re
# Add regex patterns at top of file
PATTERN = re.compile(r'...')
```

**Mathematical Problems:**
```python
import math
from fractions import Fraction
# Consider number theory, modular arithmetic
```

**Graph Problems:**
```python
from collections import defaultdict, deque
import heapq  # for Dijkstra's algorithm
```

**Combinatorial Problems:**
```python
from itertools import combinations, permutations, product
from math import factorial
```

## Quick Reference Commands

```bash
# Create new day
mkdir dayXX && cd dayXX && cp ../template_dayXX.py dayXX.py

# Test solution
python3 dayXX.py

# Time execution
time python3 dayXX.py
```

Remember: The goal is not just to solve the problem, but to learn and explain the solution clearly!
