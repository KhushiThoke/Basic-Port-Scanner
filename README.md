# 🔍 Basic Port Scanner
A simple Python-based Port Scanner that scans for open ports on a given IP address within a specified range. Useful for basic network diagnostics and learning socket programming.

## 🚀 Features
- Accepts user input for:
  - IP address
  - Start and end ports
- Validates user input and port range
- Scans ports using Python's `socket` module
- Displays open ports

## 🛠️ Requirements
- Python 3.6 or higher
No external libraries are required.

**🖥️ How to Run the scanner** : python scanner.py
**Follow the prompts** : Enter IP address to scan: 127.0.0.1
                         Enter start port (0-65535): 20
                         Enter end port (0-65535): 100


**📦 Output Example** : Scanning 127.0.0.1 from port 20 to 100...
                         Port 22 is OPEN
                         Port 80 is OPEN
                         Open ports: [22, 80]
**Clone the repository** or download the `scanner.py` file:

   ```bash
   git clone https://github.com/KhushiThoke/basic-port-scanner.git
   cd basic-port-scanner
