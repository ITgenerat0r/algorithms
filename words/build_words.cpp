#include <iostream>
#include <vector>
#include <fstream>
#include <string>

std::string output_file_name = "words";

void chain(std::string bit, const auto& it, const auto& end, std::ofstream& out){
	if(it == end){
		return;
	}
	std::vector<char> subdata = *it;
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
	bool rewrite_file = true;
	std::vector<std::vector<char>> data;
	data.clear();

	for(int i = 1; i < argc; i++){
		std::string st = argv[i];
		// std::cout << st << std::endl;
		if(st[0] != '-'){
			std::vector<char> v;
			v.clear();
			for(std::string::iterator it_str = st.begin(); it_str != st.end(); it_str++){
				// std::cout << *it_str << ' ';
				v.push_back(*it_str);
			}
			data.push_back(v);
		} else {
			if(st == "-add"){
				rewrite_file = false;
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

	std::string word = "";
	if(begin(data) != end(data)){
		std::ofstream fo;
		if(rewrite_file){
			fo.open(output_file_name);
		} else {
			fo.open(output_file_name, std::ios::app);
		}
		fo << std::endl;
		chain(word, begin(data), end(data), fo);
		fo.close();
	}

	return 0;
}