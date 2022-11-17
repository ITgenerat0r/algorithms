#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <chrono>
#include <windows.h>
#include <locale>

std::string output_file_name = "words";

void chain(std::string bit, const auto& it, const auto& end, std::ofstream& out){
	// if(it == end){
	// 	return;
	// }
	std::vector<char>& subdata = *it;
	if(it + 1 != end){
		for(std::vector<char>::iterator i = subdata.begin(); i != subdata.end(); i++){
			chain(bit + *i, it + 1, end, out);
			// std::cout << bit << *i << std::endl;
		}
	} else {
		for(std::vector<char>::iterator i = subdata.begin(); i != subdata.end(); i++){
			out << bit + *i << std::endl;
			std::cout << bit << *i << std::endl;
		}
	}
}


int main(int argc, char const *argv[])
{
	setlocale(LC_ALL, "Russian");
	auto start = std::chrono::system_clock::now();
	bool rewrite_file = true;
	std::vector<std::vector<char>> data;
	data.clear();

	unsigned int volume = 1;

	for(int i = 1; i < argc; i++){
		std::string st = argv[i];
		std::cout << std::endl;
		if(st[0] != '-'){
			std::vector<char> v;
			v.clear();
			for(std::string::iterator it_str = st.begin(); it_str != st.end(); it_str++){
				std::cout << *it_str << " - " << int(*it_str) << std::endl;
				v.push_back(*it_str);
			}
			volume *= v.size();
			data.push_back(v);
		} else {
			if(st == "-add"){
				rewrite_file = false;
			} else if (st == "-d" && i+1 < argc){
				int p = std::stoi(argv[++i]) - 1;
				// std::cout << "p = " << p << std::endl;
				if(data.size() > p && p >= 0){
					// std::cout << "PUSH\r\n";
					data.push_back(data[p]);
					volume *= data[p].size();
				}
			} else if (st == "-o"){
				if(++i < argc){
					output_file_name = argv[i];
				}
			} else if (st == "-help"){
				std::cout << "-add, don't rewrite file for saving"
						  << "-d [number], use alphabet from other position"
						  << "-o [file name], rename output file"
						  << "-help" << std::endl;
				return 0;
			}
		}
	}

	// std::cout << std::endl;
	// data.push_back({'a', 'b', 'c'});
	// data.push_back({'x', 'y', 'z'});
	// data.push_back({'k', 'l', 'm', 'n'});
	// data.push_back({'o', 'p'});

	// data.push_back({'a', 'b'});
	// data.push_back({'s', 'n'});

	std::cout << "Generating " << volume << " words..." << std::endl;

	std::string word = "";
	if(begin(data) != end(data)){
		std::ofstream fo;
		if(rewrite_file){
			fo.open(output_file_name);
		} else {
			fo.open(output_file_name, std::ios::app);
			fo << std::endl;
		}
		chain(word, begin(data), end(data), fo);
		fo.close();
	}

	auto finish = std::chrono::system_clock::now();
	std::chrono::duration<double> elapsed_seconds = finish-start;
 
    std::cout << std::endl << std::endl 
    		  << "Generated " << volume << " words." << std::endl
              << "elapsed time: " << elapsed_seconds.count() << "s"
              << std::endl;

	return 0;
}