# Advanced File Organization Automation

This project is an advanced Python script for automating the organization of files within a directory. It sorts files based on their types or extensions into designated folders, improving file management efficiency.

## Features

- **File Type Detection**: Automatically detects file types or extensions.
- **Customizable Rules**: Allows customization of rules for organizing files into folders.
- **Logging**: Logs file movements and errors for review.
- **Error Handling**: Handles exceptions gracefully.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/anesu398/file-organization-automation.git
    ```

2. Navigate to the project directory:

    ```bash
    cd file-organization-automation
    ```

3. Install dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Configure the organization rules in the `config.py` file. You can define rules based on file extensions and destination folders.

    ```python
    # Example rules
    ORGANIZATION_RULES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Videos': ['.mp4', '.mov', '.avi'],
        # Add more rules as needed
    }
    ```

2. Run the script:

    ```bash
    python organize_files.py
    ```

3. Review the log file (`file_organization.log`) for details on file movements and errors.

## Contribution

Contributions are welcome! If you have any suggestions, feature requests, or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
