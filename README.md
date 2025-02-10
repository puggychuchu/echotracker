````markdown
# EchoTracker

EchoTracker is a simple Python program designed to check network connectivity and measure speeds by pinging servers directly from a Windows desktop. The program continuously pings specified servers and provides average, minimum, and maximum ping times.

## Features

- Ping multiple servers to test connectivity and speed.
- Retrieve average, minimum, and maximum ping times for each server.
- Continuously checks connectivity at specified intervals.

## Requirements

- Python 3.x
- Windows operating system

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/echotracker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd echotracker
   ```

3. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

1. Open a terminal or command prompt.
2. Run the script using Python:
   ```bash
   python echotracker.py
   ```

3. The program will start pinging the specified servers and display the results in the console.

## Configuration

- You can modify the list of servers to ping by editing the `servers_to_ping` list in the `main()` function of `echotracker.py`.
- Adjust the interval between checks by changing the `time.sleep(60)` duration in the `main()` function. The value is in seconds.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## Contact

For questions or support, please contact [your-email@example.com](mailto:your-email@example.com).
`