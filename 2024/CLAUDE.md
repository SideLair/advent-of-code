# Advent of Code 2024 - Claude Context

## Projekt struktura
```
2024/
├── CLAUDE.md          # Tento kontext soubor
├── day01/
│   ├── day01.py      # Python řešení
│   └── day01_1.txt   # Vstupní data
├── day02/
│   └── ...
└── ...
```

## Konvence pro řešení

### Soubory pro každý den:
- `dayXX.py` - Python skript s řešením obou částí
- `dayXX_1.txt` - Vstupní data z AoC
- `test_dayXX.py` - Unit testy (pokud potřebné)

### Struktura Python skriptu:
```python
#!/usr/bin/env python3

def solve_part1(input_data):
    # Řešení první části
    pass

def solve_part2(input_data):
    # Řešení druhé části  
    pass

def main():
    # Test data
    test_data = """..."""
    print("Test data:")
    print(f"Part 1: {solve_part1(test_data)}")
    print(f"Part 2: {solve_part2(test_data)}")
    print()
    
    # Real data
    with open('dayXX_1.txt', 'r') as f:
        input_data = f.read()
    
    print("Real data:")
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")

if __name__ == "__main__":
    main()
```

### Workflow:
1. Vytvořit složku `dayXX/`
2. Připravit `dayXX.py` s template
3. Implementovat Part 1 na test datech
4. Spustit na skutečných datech
5. Implementovat Part 2
6. Finální test obou částí

### Poznámky:
- Skript vždy vypisuje výsledky obou částí
- Testuje se nejprve na ukázkových datech z zadání
- Pak se spouští na skutečných datech z `dayXX.txt`
- Kód je komentovaný pouze pokud je to nutné pro pochopení algoritmu