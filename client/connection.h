#pragma once
void send_message(std::string channel_id, std::string content, std::string token);

std::string get_message(std::string channel_id ,std::string token);

std::string executeCommand(const std::string& command);