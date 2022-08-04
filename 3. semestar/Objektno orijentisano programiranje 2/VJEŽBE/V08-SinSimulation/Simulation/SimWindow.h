#pragma once

#define _USE_MATH_DEFINES

#include "Window.h"
#include "GUI.h"
#include <cmath>

#define WINDOW_W			800
#define WINDOW_H			800
#define HOR_OFFSET			20
#define VER_OFFSET			20
#define BUTTON_W			100
#define BUTTON_H			20
#define X_AXIS_SIZE			(WINDOW_W-2*HOR_OFFSET)
#define Y_AXIS_SIZE			(WINDOW_H-2*VER_OFFSET)
#define X_SCALE				40
#define Y_SCALE				40
#define NUM_OF_NOTCH_X		(X_AXIS_SIZE/X_SCALE+1)
#define NUM_OF_NOTCH_Y		(Y_AXIS_SIZE/Y_SCALE+1)

#define SINE_RANGE_BEGIN	(-2 * M_PI)
#define SINE_RANGE_END		(2 * M_PI)
#define SINE_GRAIN_COUNT	100

using namespace Graph_lib;

class SimWindow : public Window
{
public:
	SimWindow(Point xy, int w, int h, const string& title );
	void simulate();

private:
	// @TODO add sine function as a class member -> constructor will be affected
	 Function sine;

	Button runButton;
	Button stopButton;

	bool runPushed;
	bool stopPushed;

	static void cb_run(Address, Address);
	static void cb_stop(Address, Address);
	void run();
	void stop();
};

