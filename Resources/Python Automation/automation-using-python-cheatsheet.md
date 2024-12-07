# Using Python to Interact with the Operating System Cheatsheet

This cheatsheet is designed to provide a quick reference guide for managing operating systems using Python. It covers various modules, commands, and Python libraries that are essential for interacting with the operating system. The content is based on the course [Using Python to Interact with the Operating System](https://www.coursera.org/learn/python-operating-system?specialization=google-it-automation) from Coursera.

## Table of Contents

1. [Introduction to Operating Systems](#using-python-to-interact-with-the-operating-system---module-1)
2. [Managing Files and Directories](#using-python-to-interact-with-the-operating-system---module-2)
3. [Regular Expressions](#using-python-to-interact-with-the-operating-system---module-3)
4. [Networking](#using-python-to-interact-with-the-operating-system---module-4)
5. [Testing with Python](#using-python-to-interact-with-the-operating-system---module-5)
6. [Advanced Shell Commands and System Monitoring & Performance](#using-python-to-interact-with-the-operating-system---module-6)
7. [Scheduling Tasks](#using-python-to-interact-with-the-operating-system---module-7)

# Using Python to Interact with the Operating System - Module 1

## Introduction to Operating Systems

### Key Concepts

- **Operating System (OS)**: Software that manages everything that goes on in the computer, composed of two main parts: the kernel and the user space.
- **User space**: Everything outside of the kernel that users interact with directly
- **Kernel**: Core part of the OS, managing system resources and communication between hardware and software.
- **Shell**: Interface that allows users to interact with the OS, either through a command-line interface (CLI) or graphical user interface (GUI).

### Basic Commands

- **pwd**: Print working directory.
  ```bash
  pwd
  ```
- **ls**: List directory contents.
  ```bash
  ls
  ```
- **cd**: Change directory.
  ```bash
  cd /path/to/directory
  ```
- **mkdir**: Create a new directory.
  ```bash
  mkdir new_directory
  ```
- **rmdir**: Remove a directory.
  ```bash
  rmdir directory_name
  ```
- **touch**: Create a new empty file.
  ```bash
  touch filename
  ```
- **rm**: Remove a file.
  ```bash
  rm filename
  ```

### File Permissions

- **chmod**: Change file permissions.
  ```bash
  chmod 755 filename
  ```
  - `7` - Read, write, and execute (rwx)
  - `5` - Read and execute (r-x)
  - `4` - Read only (r--)

### Useful Python Libraries

- **os**: Provides a way of using operating system dependent functionality.
  ```python
  import os
  os.listdir('.')
  ```
- **sys**: Provides access to some variables used or maintained by the interpreter.
  ```python
  import sys
  print(sys.platform)
  ```

### Commonly used Python functions:

- **os.name**: Returns the OS name (e.g., 'posix' for Unix, 'nt' for Windows).

- **os.environ**: Access environment variables.

- **os.getcwd()**: Get the current working directory.

- **os.chdir(path)**: Change the working directory.

- **os.listdir(path)**: List files and directories in a specified path.

- **os.mkdir(path)**: Create a new directory.

- **os.rmdir(path)**: Remove a directory.

- **os.remove(path)**: Remove a file.

### Example Python Script

```python
import os

# Print current working directory
print("Current Working Directory:", os.getcwd())

# List files in the current directory
print("Directory Contents:", os.listdir('.'))

# Create a new directory
os.mkdir('new_directory')

# Change to the new directory
os.chdir('new_directory')
print("Changed Directory:", os.getcwd())
```

### Additional Resources

- [Python Documentation](https://docs.python.org/3/library/os.html)
- [Linux Command Line Basics](https://linuxcommand.org/learning_the_shell.php)

# Using Python to Interact with the Operating System - Module 2

## Managing Files and Directories

### Key Concepts

- **File System**: Organizes and stores files on a storage device.
- **Path**: A string that specifies the location of a file or directory.

### Basic Commands

- **cp**: Copy files or directories.
  ```bash
  cp source_file destination_file
  ```
- **mv**: Move or rename files or directories.
  ```bash
  mv old_name new_name
  ```
- **cat**: Concatenate and display file content.
  ```bash
  cat filename
  ```
- **head**: Display the first part of a file.
  ```bash
  head filename
  ```
- **tail**: Display the last part of a file.
  ```bash
  tail filename
  ```

### File Compression

- **gzip**: Compress files.
  ```bash
  gzip filename
  ```
- **gunzip**: Decompress files.
  ```bash
  gunzip filename.gz
  ```
- **tar**: Archive multiple files into one.
  ```bash
  tar -cvf archive.tar file1 file2
  ```
- **untar**: Extract files from an archive.
  ```bash
  tar -xvf archive.tar
  ```

### Useful Python Libraries

- **shutil**: High-level file operations.
  ```python
  import shutil
  shutil.copy('source_file', 'destination_file')
  ```
- **pathlib**: Object-oriented filesystem paths.

  ```python
  from pathlib import Path
  path = Path('some_directory')
  print(path.exists())
  ```

- **csv**: Provides functionality to read from and write to CSV (Comma Separated Values) files.

  ```python
  import csv

  # Reading from a CSV file
  with open('file.csv', mode='r') as file:
      csv_reader = csv.reader(file)
      for row in csv_reader:
          print(row)

  # Writing to a CSV file
  with open('file.csv', mode='w', newline='') as file:
      csv_writer = csv.writer(file)
      csv_writer.writerow(['Column1', 'Column2'])
      csv_writer.writerow(['Value1', 'Value2'])
  ```

### Commonly used Python functions:

- **[open()](https://docs.python.org/3/library/functions.html#open)**: Used to read or write a file, includes two arguments: the file path and the mode.

  - The mode argument is optional, and it specifies the mode in which the file is opened. If omitted, it defaults to ”r” and that means opening for reading in text mode. The common modes include:

    - `“r”` open for reading (default)

    - `“w”` open for writing, truncating the file first

    - `“x”` open for exclusive creation, failing if the file already exists

    - `“a”` open for writing, appending to the end of the file if it exists

    - `“+”` open for both reading and writing

    Attempting to write to a file opened for read (“r”) will cause a runtime error.

- **close()**: Used to close an open file. When a file is closed, it is no longer available for reading or writing. It is important to close a file after its operations are complete to free up system resources and ensure that all data is properly written to the file.

- **os.path.join(path, filename)**: Combines paths in a platform-independent way.

- **os.path.exists(path)**: Check if a path exists.

- **os.path.isfile(path)**: Check if a path is a file.

- **os.path.isdir(path)**: Check if a path is a directory.

### Example Python Script

```python
import shutil
from pathlib import Path

# Copy a file
shutil.copy('source_file', 'destination_file')

# Check if a directory exists
path = Path('some_directory')
print("Directory exists:", path.exists())

# Create a new directory
path.mkdir(parents=True, exist_ok=True)
print("Created Directory:", path)
```

```python
# Create a directory and move a file from one directory to another
# using low-level OS functions.

import os

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
 os.mkdir(dest_dir)


# Construct source and destination paths:
src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")


# Move the file from its original location to the destination:
os.rename(src_file, dest_file)
```

### Additional Resources

- [Python shutil Documentation](https://docs.python.org/3/library/shutil.html)
- [Python pathlib Documentation](https://docs.python.org/3/library/pathlib.html)
- [Python os Documentation](https://docs.python.org/3/library/os.html)
- [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)

# Using Python to Interact with the Operating System - Module 3

## Regular Expressions

### Key Concepts

- **Regular Expression (regex)**: A sequence of characters that define a search pattern, mainly for use in pattern matching with strings.

### Basic Commands

- **grep**: Search for patterns in files.
  ```bash
  grep 'pattern' filename     # Add -i parameter if match should regardless of case, grep -i 'pattern' filename
  ```

### Useful Python Libraries

- **re**: Provides support for regular expressions.
  ```python
  import re
  pattern = r'\bword\b'
  text = 'This is a word in a sentence.'
  match = re.search(pattern, text)
  if match:
      print("Match found:", match.group())
  ```

### Pattern Matching

| Character | Description                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------- |
| .         | Matches any single character except newline.                                                              |
| ^         | Matches the start of the string.                                                                          |
| $         | Matches the end of the string.                                                                            |
| \*        | Matches 0 or more repetitions of the preceding RE.                                                        |
| \+        | Matches 1 or more repetitions of the preceding RE.                                                        |
| ?         | Matches 0 or 1 repetitions of the preceding RE.                                                           |
| {m}       | Matches exactly m copies of the preceding RE.                                                             |
| {m,n}     | Matches from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible. |
| \         | Escapes special characters or signals a special sequence.                                                 |
| []        | Matches any character in the brackets.                                                                    |
| \|        | Matches the preceding or next RE.                                                                         |

### Regex Examples

`r”\d{3}-\d{3}-\d{4}”` - This line of code matches U.S. phone numbers in the format 111-222-3333.

`r”^-?\d*(\.\d+)?$” ` - This line of code matches any positive or negative number, with or without decimal places.

`r”^(.+)\/([^\/]+)\/”` - This line of code matches any path and filename.

### Example Python Script

```python
import re

# Define a pattern
pattern = r'\bword\b'

# Define a text
text = 'This is a word in a sentence.'

# Search for the pattern in the text
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")
```

### Additional Resources

- [Python re Documentation](https://docs.python.org/3/library/re.html)
- [Regular Expressions 101](https://regex101.com/)

## Process Management

### Key Concepts

- **Process**: An instance of a program in execution.
- **PID (Process ID)**: A unique identifier for each process.

### Basic Commands

- **ps**: Display current processes.
  ```bash
  ps aux
  ```
- **top**: Display and update sorted information about processes.
  ```bash
  top
  ```
- **kill**: Terminate a process by PID.
  ```bash
  kill PID
  ```
- **killall**: Terminate processes by name.
  ```bash
  killall process_name
  ```

### Useful Python Libraries

- **subprocess**: Allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
  ```python
  import subprocess
  result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
  print(result.stdout)
  ```

### Example Python Script

```python
import subprocess

# Run a command and capture the output
result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
print("Current Processes:\n", result.stdout)

# Terminate a process by PID
pid = 1234  # Replace with actual PID
subprocess.run(['kill', str(pid)])
print(f"Terminated process with PID {pid}")
```

### Additional Resources

- [Python subprocess Documentation](https://docs.python.org/3/library/subprocess.html)

# Using Python to Interact with the Operating System - Module 4

## Networking

### Key Concepts

- **IP Address**: A unique string of numbers separated by periods that identifies each computer using the Internet Protocol to communicate over a network.
- **DNS (Domain Name System)**: The system that translates domain names (like www.example.com) into IP addresses.

### Basic Commands

- **ping**: Check the network connection to a server.
  ```bash
  ping www.example.com
  ```
- **ifconfig**: Display or configure network interfaces.
  ```bash
  ifconfig
  ```
- **netstat**: Display network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.
  ```bash
  netstat -a
  ```

### Useful Python Libraries

- **socket**: Provides access to the BSD socket interface.
  ```python
  import socket
  hostname = socket.gethostname()
  ip_address = socket.gethostbyname(hostname)
  print(f"Hostname: {hostname}")
  print(f"IP Address: {ip_address}")
  ```

### Example Python Script

```python
import socket

# Get the hostname
hostname = socket.gethostname()
print("Hostname:", hostname)

# Get the IP address
ip_address = socket.gethostbyname(hostname)
print("IP Address:", ip_address)

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind to the port
s.bind((host, port))

# Queue up to 5 requests
s.listen(5)

print("Server listening...")

while True:
    # Establish a connection
    clientsocket, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    clientsocket.send(b'Thank you for connecting')
    clientsocket.close()
```

### Additional Resources

- [Python socket Documentation](https://docs.python.org/3/library/socket.html)
- [Networking Basics](https://www.comptia.org/content/guides/networking-basics)

# Using Python to Interact with the Operating System - Module 5

## Testing in Python - Test-Driven Development (TDD)

### Key Concepts

- **Test-Driven Development (TDD)**: A software development process where tests are written before the code that needs to be tested.
- **Red-Green-Refactor**: The TDD cycle which involves writing a failing test (Red), writing code to pass the test (Green), and then refactoring the code while ensuring tests still pass.

### TDD Workflow

1. **Write a Test**: Write a test for the next bit of functionality you want to add.
2. **Run the Test**: Run the test and see it fail (Red).
3. **Write Code**: Write the minimum amount of code required to pass the test (Green).
4. **Run the Test Again**: Ensure the test passes.
5. **Refactor**: Refactor the code while keeping the tests passing.
6. **Repeat**: Repeat the cycle for the next bit of functionality.

### Example TDD with pytest

1. **Write a Test**:

   ```python
   # test_math.py
   def test_addition():
       assert add(1, 2) == 3
   ```

2. **Run the Test**:

   ```bash
   pytest test_math.py
   ```

3. **Write Code**:

   ```python
   # math_operations.py
   def add(a, b):
       return a + b
   ```

4. **Run the Test Again**:

   ```bash
   pytest test_math.py
   ```

5. **Refactor**:
   ```python
   # math_operations.py
   def add(a, b):
       return a + b  # No refactoring needed in this simple example
   ```

### Example Python Script

```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
# test_math_operations.py
import pytest
from math_operations import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)
```

### Additional Resources

- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [Test-Driven Development by Example](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530)

## Testing in Python - Unit Tests

### Key Concepts

- **Unit Testing**: Testing individual units or components of a software.
- **Integration Testing**: Testing the integration of different modules or services.
- **Test Coverage**: A measure of how much of the code is tested.

### Basic Commands

- **pytest**: A framework that makes building simple and scalable test cases easy.
  ```bash
  pytest test_module.py
  ```
- **unittest**: A built-in Python module for testing.
  ```bash
  python -m unittest test_module.py
  ```

### Useful Python Libraries

- **unittest**: A built-in library for creating and running tests.

  ```python
  import unittest

  class TestStringMethods(unittest.TestCase):

      def test_upper(self):
          self.assertEqual('foo'.upper(), 'FOO')

      def test_isupper(self):
          self.assertTrue('FOO'.isupper())
          self.assertFalse('Foo'.isupper())

  if __name__ == '__main__':
      unittest.main()
  ```

- **pytest**: A third-party library for more advanced testing.

  ```python
  def test_upper():
      assert 'foo'.upper() == 'FOO'

  def test_isupper():
      assert 'FOO'.isupper()
      assert not 'Foo'.isupper()
  ```

### Example Python Script

```python
import unittest

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def test_multiplication(self):
        self.assertEqual(2 * 3, 6)

    def test_division(self):
        self.assertEqual(10 / 2, 5)

if __name__ == '__main__':
    unittest.main()
```

### Additional Resources

- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [pytest Documentation](https://docs.pytest.org/en/stable/)

# Using Python to Interact with the Operating System - Module 6

## Advanced Shell Commands

### Key Concepts

- **Piping**: Redirecting the output of one command as input to another command.
- **Redirection**: Redirecting the output or input of commands to or from files.

### Basic Commands

- **|**: Pipe the output of one command to another.
  ```bash
  ls | grep 'pattern'
  ```
- **>**: Redirect output to a file.
  ```bash
  echo "Hello, World!" > output.txt
  ```
- **>>**: Append output to a file.
  ```bash
  echo "Hello again!" >> output.txt
  ```
- **<**: Redirect input from a file.
  ```bash
  sort < unsorted_list.txt
  ```

### Useful Python Libraries

- **os**: Execute shell commands from within Python.
  ```python
  import os
  os.system('ls | grep "pattern"')
  ```

### Example Python Script

```python
import os

# Execute a shell command and redirect output to a file
os.system('echo "Hello, World!" > output.txt')

# Append output to the file
os.system('echo "Hello again!" >> output.txt')

# Execute a command with piping
os.system('ls | grep "pattern"')
```

### Additional Resources

- [Python os Documentation](https://docs.python.org/3/library/os.html)
- [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/)

## System Monitoring and Performance

### Key Concepts

- **System Load**: A measure of the amount of computational work that a system performs.
- **Memory Usage**: The amount of memory being used by processes on the system.

### Basic Commands

- **free**: Display memory usage.
  ```bash
  free -h
  ```
- **df**: Display disk space usage.
  ```bash
  df -h
  ```
- **uptime**: Show how long the system has been running.
  ```bash
  uptime
  ```
- **vmstat**: Report virtual memory statistics.
  ```bash
  vmstat
  ```

### Useful Python Libraries

- **psutil**: Provides an interface for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors).
  ```python
  import psutil
  print("CPU Usage:", psutil.cpu_percent(interval=1))
  print("Memory Usage:", psutil.virtual_memory())
  ```

### Example Python Script

```python
import psutil

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print("CPU Usage:", cpu_usage)

# Get memory usage
memory_info = psutil.virtual_memory()
print("Memory Usage:", memory_info)

# Get disk usage
disk_usage = psutil.disk_usage('/')
print("Disk Usage:", disk_usage)

# Get system uptime
uptime = psutil.boot_time()
print("System Uptime:", uptime)
```

### Additional Resources

- [Python psutil Documentation](https://psutil.readthedocs.io/en/latest/)
- [Linux Performance Monitoring Tools](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)

# Using Python to Interact with the Operating System - Module 7

## Scheduling Tasks

### Key Concepts

- **Cron**: A time-based job scheduler in Unix-like operating systems.
- **Crontab**: A file that contains the schedule of cron entries to be run and at specified times.

### Basic Commands

- **crontab -e**: Edit the crontab file.
  ```bash
  crontab -e
  ```
- **crontab -l**: List the crontab file.
  ```bash
  crontab -l
  ```
- **crontab -r**: Remove the crontab file.
  ```bash
  crontab -r
  ```

### Crontab Syntax

- **Minute**: 0-59
- **Hour**: 0-23
- **Day of Month**: 1-31
- **Month**: 1-12
- **Day of Week**: 0-7 (0 and 7 are Sunday)

Example:

```bash
# Run a script every day at 2am
0 2 * * * /path/to/script.sh
```

### Useful Python Libraries

- **schedule**: Job scheduling for humans.

  ```python
  import schedule
  import time

  def job():
      print("Task running...")

  schedule.every().day.at("02:00").do(job)

  while True:
      schedule.run_pending()
      time.sleep(1)
  ```

### Example Python Script

```python
import schedule
import time

# Define a job
def job():
    print("Task running...")

# Schedule the job every day at 2am
schedule.every().day.at("02:00").do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
```

### Additional Resources

- [Python schedule Documentation](https://schedule.readthedocs.io/en/stable/)
- [CronHowto](https://help.ubuntu.com/community/CronHowto)
