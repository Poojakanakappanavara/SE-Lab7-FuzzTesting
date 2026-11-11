
# SE Lab 7 - Fuzz Testing

## Objective
To identify and fix input validation bugs in a Python application using fuzz testing with the Hypothesis library.

## Tools Used
- Python 3.10
- Pytest
- Hypothesis
- Ubuntu on WSL

## Project Files
- processor.py - Fixed Python application.
- test_processor.py - Automated fuzz testing test cases.
- requirements.txt - Required Python libraries.
- .gitignore - Files excluded from Git.

## Functions Tested
1. parse_int_list() - Converts comma-separated values into integers.
2. calculate_average() - Calculates the average of a list.
3. validate_age() - Checks whether an age is valid.

## Testing Process
1. Created an application containing intentional bugs.
2. Executed the original application.
3. Created Hypothesis-based tests.
4. Identified four failures in the original application.
5. Fixed the application.
6. Updated the tests to verify corrected behaviour.
7. Executed all tests again.

## Final Test Result
6 tests passed successfully.

## Execution Commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python processor.py
```

Run tests:

```bash
python -m pytest test_processor.py -v
```

## Conclusion
Fuzz testing helped identify input validation errors and edge cases. After fixing the application and updating the tests, all six tests passed successfully.
