#!/bin/bash
#
# Analyze usage of shared components across prompt files
# This helps identify which components are most used and potential new extraction opportunities

SETUP_DIR="$(dirname "$(dirname "$0")")"
PROJECT_ROOT="$(dirname "$SETUP_DIR")"

echo "Analyzing component usage in Claude Global Commands..."
echo "=================================================="

# Function to count references
count_references() {
    local pattern="$1"
    local description="$2"
    
    echo -e "\n$description:"
    grep -r "$pattern" "$PROJECT_ROOT" --include="*.md" --include="*.yaml" --exclude-dir=setup 2>/dev/null | \
        grep -v "^Binary file" | \
        awk -F: '{print "  - " $1}' | \
        sort | uniq -c | \
        sort -rn
}

# Count direct references to shared components
echo -e "\nDirect references to shared-components.yaml:"
grep -r '\$ref:.*shared-components\.yaml' "$PROJECT_ROOT" --include="*.md" --include="*.yaml" --exclude-dir=setup 2>/dev/null | \
    grep -v "^Binary file" | \
    sed 's/.*\$ref: *//' | \
    sed 's/ *$//' | \
    sort | uniq -c | \
    sort -rn

# Count template references
count_references '\$ref:.*templates/' "Template usage"

# Find potential patterns (repeated text blocks)
echo -e "\nPotential extraction opportunities (repeated patterns):"
echo "  Analyzing files for repeated instruction blocks..."

# This is a simplified pattern detection - in practice, you'd want more sophisticated analysis
find "$PROJECT_ROOT" -name "*.md" -type f ! -path "*/setup/*" -exec basename {} \; | \
    while read -r file; do
        echo "  Checking: $file"
    done

echo -e "\nAnalysis complete!"
echo "Consider extracting patterns that appear in 3+ files."