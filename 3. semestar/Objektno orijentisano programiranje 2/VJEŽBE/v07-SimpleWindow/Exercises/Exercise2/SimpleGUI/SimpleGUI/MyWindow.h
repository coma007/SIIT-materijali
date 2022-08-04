#pragma once

#include "Window.h"
#include "GUI.h"

#define IN_BOX_X_ALIGN		100
#define IN_BOX_X_OFFSET		200
#define IN_BOX_Y_ALIGN		25
#define IN_BOX_Y_OFFSET		25
#define IN_BOX_W			100
#define IN_BOX_H			IN_BOX_Y_OFFSET

#define OUT_BOX_X_ALIGN		IN_BOX_X_ALIGN
#define OUT_BOX_X_OFFSET	IN_BOX_X_OFFSET
#define OUT_BOX_Y_ALIGN		150
#define OUT_BOX_Y_OFFSET	IN_BOX_Y_OFFSET
#define OUT_BOX_W			IN_BOX_W
#define OUT_BOX_H			IN_BOX_H

#define BUTTON_W			(IN_BOX_W * 2)
#define BUTTON_H			IN_BOX_H

#define WINDOW_W			450
#define WINDOW_H			300

using namespace Graph_lib;

class MyWindow : public Window
{
public:
	MyWindow(Point xy, int w, int h, const string& title);
	~MyWindow(void);
	bool wait_for_button();

private:
	
	In_box radius;
	In_box rectWidth;
	In_box rectHeight;
	In_box squareWidth;

	Out_box circleArea;
	Out_box rectArea;
	Out_box squareArea;

	Button getAreaButton;
	bool buttonPushed;
	static void cb_getAreaButton(Address, Address);
	void getAreaButtonHandler();
};

