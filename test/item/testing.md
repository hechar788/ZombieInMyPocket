# Item Module Testing Guide

This directory contains unit tests for the item module components of the Zombie In My Pocket game.

## Test Files

- `test_base_item.py` - Tests for BaseItem, ConsumableItem, WeaponItem, CombinableItem, and SpecialWeaponItem classes
- `test_combination_engine.py` - Tests for item combination logic and rules engine
- `test_item_config.py` - Tests for item configuration data and validation
- `test_item_factory.py` - Tests for item creation factory methods

## Running Tests

### Prerequisites

1. Activate the virtual environment:
   ```bash
   venv/Scripts/activate.bat
   ```

2. Ensure pytest is installed:
   ```bash
   pip install pytest
   ```

### Run All Item Tests

```bash
python -m pytest test/item/ -v
```

### Run Specific Test Files

```bash
# Run base item tests
python -m pytest test/item/test_base_item.py -v

# Run combination engine tests
python -m pytest test/item/test_combination_engine.py -v

# Run item config tests
python -m pytest test/item/test_item_config.py -v

# Run item factory tests
python -m pytest test/item/test_item_factory.py -v
```

### Run Tests with Coverage (if coverage is installed)

```bash
python -m pytest test/item/ --cov=src/model/item
```

## Test Results

When successful, all 54 tests should pass:
- 15 tests for base item classes
- 16 tests for combination engine functionality
- 13 tests for item configuration validation
- 10 tests for item factory methods

## Code Style

All test files follow PEP8 style guidelines and can be verified with:

```bash
python -m pycodestyle test/item/
```