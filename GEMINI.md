# Global Agent Rules

## Code Editing & Diff Preferences

1. **In the IDE (Interactive GUI / VS Code / Antigravity IDE)**:
   - Always perform code changes step-by-step: execute **one single atomic edit per turn** using `replace_file_content` or `write_to_file`.
   - Stop execution immediately after each edit so that the IDE displays the interactive **Visual Diff Overlay** with the **Accept / Deny** buttons for user review.
   - Do not batch or chain multiple edits across the file in a single response unless explicitly requested.

2. **In the CLI (`agy` / Terminal)**:
   - Apply code changes directly, automatically, and in batch without waiting for intermediate step-by-step confirmations.
   - Maintain fast, unattended task execution.

