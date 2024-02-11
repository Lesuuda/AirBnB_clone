# 0x00. AirBnB Clone - The Console

This is the first part of the AirBnB Clone project, which involves creating a command-line interface (CLI) for managing AirBnB objects. This CLI, also known as the console, allows users to create, update, delete, and manage AirBnB objects such as users, places, cities, amenities, and reviews.

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Examples](#examples)
7. [Contributing](#contributing)
8. [License](#license)

## Description

The AirBnB Clone project is a recreation of the popular AirBnB website, focusing on the backend functionality and CLI interface. The console serves as the primary interface for interacting with the AirBnB objects, providing various commands for managing and querying the data.

## Features

- Create, read, update, and delete AirBnB objects such as users, places, cities, amenities, and reviews.
- Supports various commands for interacting with objects, including `create`, `show`, `update`, `destroy`, and `all`.
- Flexible and extensible design, allowing for easy integration of new object types and commands.
- Persistence using JSON file storage, ensuring data is saved between sessions.

## Technologies Used

- Python: The core programming language used for developing the console.
- JSON: File storage format used for persistence.
- Git: Version control system for tracking changes and collaborating on the project.

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/lesuuda/AirBnB_clone.git
```

2. Navigate to the project directory:

```
cd AirBnB_clone
```

3. Install any necessary dependencies:

```
pip install -r requirements.txt
```

## Usage

To start the console, run the following command from the project directory:

```
./console.py
```

Once the console is running, you can start entering commands to interact with AirBnB objects. Use the `help` command to see a list of available commands and their usage.

## Examples

Create a new user:
```
(hbnb) create User
```

Show details of a specific user:
```
(hbnb) show User 1234-5678-9012
```

Update the name of a place:
```
(hbnb) update Place 9876-5432-1098 name "New Name"
```

Delete a city:
```
(hbnb) destroy City 5678-1234-9012
```

List all amenities:
```
(hbnb) all Amenity
```

## Contributing

Contributions to the project are welcome! If you find any bugs or have suggestions for improvements, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
