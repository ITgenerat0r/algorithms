#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <chrono>
#include <windows.h>
#include <locale>
#include <set>

#include "percent_windows.cpp"

#define VERSION "v2.3"

std::string output_file_name = "words";


void chain(std::string bit, const auto& it, const auto& end, std::ofstream& out, Percent p){
	// if(it == end){
	// 	return;
	// }
	std::vector<char>& subdata = *it;
	if(it + 1 != end){
		for(std::vector<char>::iterator i = subdata.begin(); i != subdata.end(); i++){
			chain(bit + *i, it + 1, end, out, p);
			// std::cout << bit << *i << std::endl;
		}
	} else {
		for(std::vector<char>::iterator i = subdata.begin(); i != subdata.end(); i++){
			out << bit + *i << std::endl;
			p.clear_current_line();
			std::cout << bit << *i << std::endl;
			p.increase();
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

	std::string alphabet = "";
	int min_len = 1, max_len = 0;
	unsigned int volume = 1;
	std::string mask = "";
	std::cout << "Version " << VERSION << std::endl;


	// Считываем переданные данные из ARGV
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
			} else if (st == "-permutations" && i+1 < argc){
				alphabet = argv[++i];
			} else if (st == "-min" && i+1 < argc){
				min_len = std::stoi(argv[++i]);
			} else if (st == "-max" && i+1 < argc){
				max_len = std::stoi(argv[++i]) + 1;
			} else if (st == "-mask" && i+1 < argc){
				mask = argv[++i];
			} else if (st == "-o"){
				if(++i < argc){
					output_file_name = argv[i];
				}
			} else if (st == "-help"){
				std::cout << "-add, don't rewrite file for saving"
						  << "-d [number], use alphabet from other position"
						  << "-o [file name], rename output file"
						  << "permutation [alphabet]"
						  << "-min [number], minimum lenght for output words"
						  << "-max [number], maximum lenght for output words"
						  << "-mask [mask], not developed"
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

	// если перестановки, то определяем количество перестановок
	if(alphabet != ""){
		volume = 1;
		int count_factorial = 1;
		for(std::string::iterator it_str = alphabet.begin(); it_str != alphabet.end(); it_str++){
			volume *= count_factorial++;
		}

		// check
		if(mask.size() > 0){
			min_len = mask.size();
			max_len = mask.size();
		} else if (max_len != 0 && max_len < min_len){
			max_len = 0;
		}
	}
	std::cout << "Generating " << volume << " words..." << std::endl;

	Percent bar(0, volume);

	// если только перестановки
	if(alphabet != ""){
		std::set<std::string> res;
		res.clear();
		int len_alphabet = alphabet.size();
		if(max_len == 0 || max_len > alphabet.size()){
			max_len = alphabet.size();
		}

		std::sort(alphabet.begin(), alphabet.end());
	    do {
	        // std::cout << alphabet << '\n';
	        for(int i = min_len; i < max_len; i++){
	        	res.insert(alphabet.substr(0, i));
	        	// std::cout << ":" << alphabet.substr(0, i) << std::endl;
	        }
	        // res.insert(alphabet);
	    } while(std::next_permutation(alphabet.begin(), alphabet.end()));


	    // запись результата в файл
	    std::cout << "Writing data in file..." << std::endl;
	    std::ofstream fo;
	    if(rewrite_file){
			fo.open(output_file_name);
		} else {
			fo.open(output_file_name, std::ios::app);
			fo << std::endl;
		}
	    for(const auto& it : res){
	    	// std::cout << it << std::endl;
	    	fo << it << std::endl;
	    }
	    fo.close();

	} else {
		// если для полного перебора для словарей по позициям
		std::string word = "";
		if(begin(data) != end(data)){
			std::ofstream fo;
			if(rewrite_file){
				fo.open(output_file_name);
			} else {
				fo.open(output_file_name, std::ios::app);
				fo << std::endl;
			}
			chain(word, begin(data), end(data), fo, bar);
			fo.close();
		}
	}

	auto finish = std::chrono::system_clock::now();
	std::chrono::duration<double> elapsed_seconds = finish-start;
 
    std::cout << std::endl << std::endl 
    		  << "Generated " << volume << " words." << std::endl
              << "elapsed time: " << elapsed_seconds.count() << "s"
              << std::endl;
	return 0;
}