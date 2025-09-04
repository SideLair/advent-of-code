# Advent of Code 2024 - Claude Context

## Project Structure
```
2024/
├── CLAUDE.md          # This context file
├── day01/
│   ├── day01.py      # Python solution
│   ├── input.txt     # Input data from AoC
│   └── test.txt      # Test data from problem description
├── day02/
│   └── ...
└── ...
```

## Solution Conventions

### Files for each day:
- `dayXX.py` - Python script with both parts solution
- `input.txt` - Input data from AoC
- `test.txt` - Test data from problem description (if in separate file)

### Python script structure:
```python
#!/usr/bin/env python3

def solve_part1(input_data):
    # Part 1 solution
    pass

def solve_part2(input_data):
    # Part 2 solution  
    pass

def main():
    # Test data
    test_data = """..."""
    print("Test data:")
    print(f"Part 1: {solve_part1(test_data)}")
    print(f"Part 2: {solve_part2(test_data)}")
    print()
    
    # Real data
    with open('input.txt', 'r') as f:
        input_data = f.read()
    
    print("Real data:")
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")

if __name__ == "__main__":
    main()
```

### Workflow:
1. Create `dayXX/` folder
2. Prepare `dayXX.py` with template
3. Implement Part 1 on test data
4. Run on real data
5. Implement Part 2
6. Final test of both parts

### Notes:
- Script always prints results of both parts
- Test first on sample data from problem description
- Then run on real data from `input.txt`
- Code is commented only when necessary for algorithm understanding

### Coding Standards:
- **Language**: All variable names, file names, and comments must be in English
- **Problem-solving approach**: Always propose multiple solution approaches first, then let the user choose which one to implement
- These standards apply to all code in this repository by default

### Best Practices for Daily AoC Problem Solving:

#### Code Structure:
- Keep functions small and focused on single responsibility
- Use descriptive function names that explain what they do
- Prefer list comprehensions and built-ins over manual loops when readable
- Use regex for pattern matching problems, but consider readability vs performance

#### Problem-Solving Strategy:
1. **Read carefully** - understand input format, edge cases, constraints
2. **Start simple** - get Part 1 working with test data first
3. **Optimize later** - focus on correctness before performance
4. **Part 2 evolution** - often extends Part 1 logic, plan for modification
5. **Input parsing** - handle both test strings and file input consistently

#### Common Patterns:
- **Grid problems**: Use (row, col) tuples, consider directions as vectors
- **Graph problems**: BFS for shortest path, DFS for exploration
- **State machines**: Track current state, process transitions
- **Dynamic programming**: Memoization for overlapping subproblems
- **Parsing**: Regex for structured text, split() for simple formats

#### Debugging Tips:
- Print intermediate results to understand data flow
- Test with minimal examples before full input
- Use assertions to verify assumptions
- Consider boundary conditions and empty inputs

#### Performance Considerations:
- Most AoC problems run in < 1 second with reasonable algorithms
- O(n²) is usually acceptable for n < 10,000
- Use sets for O(1) lookups instead of lists when possible
- Cache expensive computations with functools.lru_cache

#### Educational Approach:
- **Always provide learning context** with each solution
- Explain **why** this approach was chosen over alternatives
- Discuss **trade-offs**: readability vs performance, memory vs time
- Highlight **key algorithms/data structures** used and when to apply them
- Connect to **computer science concepts**: complexity analysis, design patterns
- Point out **Python-specific features** and their benefits
- Mention **alternative approaches** and their pros/cons
- Include **real-world applications** of the techniques used

Examples of educational context:
- "Regex chosen over manual parsing because pattern is well-defined and complex"
- "Used set for O(1) lookups instead of list's O(n) - critical for large inputs"
- "State machine pattern handles complex conditional logic cleanly"
- "This demonstrates dynamic programming's optimal substructure principle"