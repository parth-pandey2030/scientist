#include <iostream>

/**
 * This file is used to install all neccessary files
 * and tools used in this project.
 * Just run the executable (./installer) followed by the
 * "lib" or "tool" command, followed by the name of the library/tool.
 * Example: ./installer lib numpy
*/

#define INSTALLER_LIB(thing_you_want_to_install) system("pip install " #thing_you_want_to_install) // for python
#define INSTALLER_TOOL(thing_you_want_to_install) system("sudo apt install " #thing_you_want_to_install)

int main(int argc, char *argv[]) {
    if (argc < 3) {
        std::cout << "Usage: ./installer lib <library_name> | tool <tool_name>\n";
        return 1;
    }

    if (std::string(argv[1]) == "lib") {
        std::cout << "Installing library " << argv[2] << "...\n";
        INSTALLER_LIB(argv[2]);
    } else if (std::string(argv[1]) == "tool") {
        std::cout << "Installing tool " << argv[2] << "...\n";
        INSTALLER_TOOL(argv[2]);
    } else {
        std::cout << "Usage: ./installer lib <library_name> | tool <tool_name>\n";
        return 1;
    }
    
    return 0;
}