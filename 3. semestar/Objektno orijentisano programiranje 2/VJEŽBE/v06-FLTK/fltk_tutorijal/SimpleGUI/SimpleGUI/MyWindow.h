#pragma once

#include "Window.h"
#include "GUI.h"

using namespace Graph_lib;

class MyWindow : public Window
{
public:
	MyWindow(Point xy, int w, int h, const string& title);
	~MyWindow(void);
	bool wait_for_button();

private:
	Button showButton;
	In_box inBox;
	Out_box outBox;
	Menu menu;
	bool showButtonPushed;
	static void cb_showButton(Address, Address);
	void showButtonHandler();
};

