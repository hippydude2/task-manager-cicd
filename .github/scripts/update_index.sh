
#!/bin/bash
set -e

# Input files
TASK_OUTPUT="$1"
TEST_OUTPUT="$2"
HTML_FILE="index.html"

# Verify input files exist
if [ ! -f "$TASK_OUTPUT" ] || [ ! -f "$TEST_OUTPUT" ]; then
    echo "Error: Input files not found."
    exit 1
fi

if [ ! -f "$HTML_FILE" ]; then
    echo "Error: index.html not found."
    exit 1
fi

# Extract ToDo tasks
TODO_TASKS=$(awk '
    /^ToDo Tasks:/ {show=1; next}
    /^Done Tasks:/ {show=0}
    show && NF {print}
' "$TASK_OUTPUT")

# Extract Done tasks
DONE_TASKS=$(awk '
    /^Done Tasks:/ {show=1; next}
    show && NF {print}
' "$TASK_OUTPUT")

# Read unit test results
TEST_RESULTS=$(cat "$TEST_OUTPUT")

# Export variables for Perl
export TODO_TASKS DONE_TASKS TEST_RESULTS

# Update the HTML <pre> sections
perl -0777 -i -pe '
    s{(<pre id="todo-tasks">).*?(</pre>)}
     {$1."\n".$ENV{TODO_TASKS}."\n".$2}gse;

    s{(<pre id="done-tasks">).*?(</pre>)}
     {$1."\n".$ENV{DONE_TASKS}."\n".$2}gse;

    s{(<pre id="test-results">).*?(</pre>)}
     {$1."\n".$ENV{TEST_RESULTS}."\n".$2}gse;
' "$HTML_FILE"

echo "index.html updated successfully!"
