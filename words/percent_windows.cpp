#include "percent_windows.h"


Percent::Percent(const long int& b, const long int& e):begin_range(b), end_range(e), md(e-b){
	current = begin_range;
	// md = end_range - begin_range;
	position.Y = 0;
	position.X = 1;
	active_position = position;
    outspace_size = std::to_string(md).size();

    // set bar_size
    bar_size = 0;
    HANDLE hWndConsole;
    if (hWndConsole = GetStdHandle(-12))
    {
        CONSOLE_SCREEN_BUFFER_INFO consoleInfo;
        if (GetConsoleScreenBufferInfo(hWndConsole, &consoleInfo))
        {
            int width = consoleInfo.srWindow.Right - consoleInfo.srWindow.Left + 1;
            // int height = consoleInfo.srWindow.Bottom - consoleInfo.srWindow.Top + 1;
            // std::cout << "width = " << width << std::endl;
            bar_size = width - 10 - outspace_size * 3;
            std::string cs(width, ' ');
            clear_string = cs;
        }
    }
    if(bar_size < 1){
        bar_size = 10;
    }

    // set bar -
    std::string filled(bar_size, '#');
    std::string empted(bar_size, '-');
    bar = filled + empted;
}


COORD Percent::getpos()
{
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    COORD coord;
 
    if (GetConsoleScreenBufferInfo(
        GetStdHandle(STD_OUTPUT_HANDLE), &csbi))
    {
        coord.X = csbi.dwCursorPosition.X;
        coord.Y = csbi.dwCursorPosition.Y;
    }
    else
    {
        coord.X = 0;
        coord.Y = 0;
    }
    return coord;
}

void Percent::setpos(COORD pos){
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleCursorPosition(hConsole, pos);
}

void Percent::movepos(int y, int x){
    COORD position = this->getpos();
    // std::cout << " Current position (" << position.Y << ", " << position.X << ")" << std::endl;
    position.X += x;
    position.Y += y;
    this->setpos(position);
}


void Percent::changepos(int y, int x)
{
    position.X = x;
    position.Y = y;
    
}

void Percent::update(long int cur){
	current = cur - begin_range;
	pc = double(current)/double(md)*100;
    int bar_pc = int(bar_size*pc/100);
    // std::cout << "bar_pc = " << bar_pc << std::endl;
    this->clear_current_line();
    this->movepos(1, 0);
	std::cout << std::setw(outspace_size) << current << '/' << md << ", " 
			  << std::setw(outspace_size) << pc << "% " 
			  << '[' << bar.substr(bar_size - bar_pc, bar_size) << ']';
    active_position = getpos();
    active_position.Y--;
    active_position.X = 0;
    this->setpos(active_position);
}

void Percent::increase(){
    this->update(++current);
}

void Percent::erase_line(int y){
    active_position = getpos();
    COORD pos;
    pos.X = 0;
    pos.Y = y;
    this->setpos(pos);
    std::cout << clear_string;
    this->setpos(active_position);
}

void Percent::clear_current_line(){
    active_position = getpos();
    erase_line(active_position.Y);
}

Percent::~Percent(){
	// setpos(active_position);
    movepos(2, 0);
    // std::cout << "Destructor();" << std::endl;
}
