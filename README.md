# Python Metadata Extractor

This is a Python project that extracts all available metadata from images and saves it in a separate folder.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites

- Python 3.6 or higher
- exiftool

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/aaronedev/metadata-extractor
    ```

2. Navigate to the project directory:

    ```sh
    cd metadata-extractor
    ```

3. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Install exiftool. For Windows users, you can use Chocolatey:

    ```sh
    choco install exiftool
    ```

## Usage

1. Place your images in the `images` directory.
2. Run the main script:

    ```sh
    python main.py
    ```

3. The metadata will be extracted and saved in the `metadata` directory.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
