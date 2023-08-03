
# enum buddy

## Overview

enum buddy is a Python tool that harnesses the power of Nmap for network scanning. The idea behind enum buddy is simple: make network scanning and enumeration more accessible and educational. The tool provides helpful suggestions based on open ports and is designed to grow with the collective knowledge of its users.

## Features

- **Nmap Scanning**: Performs scans with user-specified Nmap flags.
- **Educational Tips**: Provides useful insights for Nmap commands.
- **Scan Logs**: Keeps a record of scan results for future reference.
- **Actionable Suggestions**: Parses scan results to provide actionable suggestions based on open ports.
- **Community Contributions**: enum buddy lets users add their own tips for unrecognized ports, fostering a community of shared knowledge.

## Installation

To install enum buddy, clone this repository:

```
git clone https://github.com/<zgsec>/enumbuddy.git
```

## Usage

Once installed, you can run the tool with your desired Nmap flag and target IP or IP range:

```
cd enumbuddy
python3 enumbuddy.py -c "<NMAP_FLAG>" -t "<IP_OR_RANGE>"
```

For example:

```bash
python3 enumbuddy.py -c "-sS" -t "192.168.x.x"
```

## Contributing

The true strength of enum buddy lies in its users. The tool prompts you to provide a description and suggestions whenever it encounters an unrecognized port. By sharing your knowledge, you help to expand the tool's services dictionary and contribute to a collective understanding of network services. 

If you'd like to contribute:

1. Fork the project.
2. Create a new branch (\`git checkout -b new-feature\`).
3. Commit your changes (\`git commit -am 'Add new feature'\`).
4. Push to the branch (\`git push origin new-feature\`).
5. Create a new Pull Request.

## License

enum buddy is licensed under the MIT License - see the LICENSE file for details.
