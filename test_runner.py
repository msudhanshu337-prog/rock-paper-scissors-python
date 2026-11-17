import subprocess
import os

SCRIPT_DIR = r"C:\Users\SUDHANSHU MANDAL\.gemini\antigravity\scratch\rock_paper_scissors"
SCRIPT_PATH = os.path.join(SCRIPT_DIR, "rock_paper_scissors.py")

def run_test(name, input_data):
    p = subprocess.run(
        ["python", SCRIPT_PATH],
        input=input_data,
        text=True,
        capture_output=True,
        cwd=SCRIPT_DIR
    )
    print(f"==================== {name} ====================")
    print("OUTPUT:")
    print(p.stdout)
    if p.stderr:
        print("STDERR:")
        print(p.stderr)

# Test Case 1: rock, rock, rock -> Match drawn
run_test("Test Case 1: Normal Input (rock, rock, rock)", "rock\nrock\nrock\nn\n")

# Test Case 2: rock, paper, scissors -> You win the match!
run_test("Test Case 2: Boundary / Minimum Input (rock, paper, scissors)", "rock\npaper\nscissors\nn\n")

# Test Case 3: stone, rock, rock, rock -> Invalid choice then resumes
run_test("Test Case 3: Invalid Input (stone -> rock, rock, rock)", "stone\nrock\nrock\nrock\nn\n")

# Test Case 4: scissors, scissors, rock -> Computer wins the match
run_test("Test Case 4: Different Valid Scenario (scissors, scissors, rock)", "scissors\nscissors\nrock\nn\n")
