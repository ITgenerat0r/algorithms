#include <iostream>
#include <windows.h>
#include <string>

COORD getpos()
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

void setpos(COORD position){
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleCursorPosition(hConsole, position);
}


void gotoxy(int y, int x)
{
    COORD position;
    position.X = x;
    position.Y = y;
    setpos(position);
}




int main(int argc, char const *argv[])
{
	std::string x = "";
	
	while(x != "exit") {
	    std::cin >> x;
	    COORD s = getpos();
		gotoxy(2,0);
		std::cout << x;
		setpos(s);
	}
	
	return 0;
}