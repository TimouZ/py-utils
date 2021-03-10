import sys

# Save the current stdout so that we can revert sys.stdout after we complete
# our redirection
stdout_std_handler = sys.stdout

sample_input = ['Item1', 'Item2', 'Item3']

# Redirect sys.stdout to the file
sys.stdout = open('Output.txt', 'w')

for item in sample_input:
    # Prints to the redirected stdout (Output.txt)
    sys.stdout.write(item + '\n')
    # Prints to the actual saved stdout handler
    stdout_std_handler.write(item + '\n')

# Close the file
sys.stdout.close()
# Restore sys.stdout to our old saved file handler
sys.stdout = stdout_std_handler
