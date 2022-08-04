#include "SimWindow.h"

SimWindow::SimWindow(Point xy, int w, int h, const string& title):
	Window(xy, w, h, title),
	runButton(
		Point(x_max() - BUTTON_W, 0),
		BUTTON_W,
		BUTTON_H,
		"RUN",
		cb_run),
	stopButton(
		Point(x_max() - BUTTON_W, BUTTON_H),
		BUTTON_W,
		BUTTON_H,
		"STOP",
		cb_stop),
	runPushed(false),
	stopPushed(false),
	sine(sin, SINE_RANGE_BEGIN, SINE_RANGE_END, Point(WINDOW_W/2 - SINE_RANGE_END + HOR_OFFSET/2, WINDOW_H / 2), SINE_GRAIN_COUNT, NUM_OF_NOTCH_X, NUM_OF_NOTCH_Y)
{
	// @TODO - something missing ?
	attach(runButton);
	attach(stopButton);
	sine.set_color(Color::red);
	attach(sine);
}


void SimWindow::simulate()
{
	show();
	int i = 0;

	while(1)
	{
		runPushed = false;
		stopPushed = false;

		while(!runPushed && !stopPushed) Fl::wait();

		// @TODO what will happen if run is pressed
		if (runPushed) {
			Function newSine(sin, SINE_RANGE_BEGIN + M_PI*i, SINE_RANGE_END + M_PI*i, Point(WINDOW_W / 2 - SINE_RANGE_END + HOR_OFFSET / 2 + Y_AXIS_SIZE / NUM_OF_NOTCH_X * M_PI, WINDOW_H / 2), SINE_GRAIN_COUNT, NUM_OF_NOTCH_X, NUM_OF_NOTCH_Y);
			attach(newSine);
			
			flush();
			i++;
		}
		if (stopPushed) {
			break;
		}
	}
	return;
}


void SimWindow::cb_run(Address, Address pw)
{
	reference_to<SimWindow>(pw).run();
}


void SimWindow::cb_stop(Address, Address pw)
{
	reference_to<SimWindow>(pw).stop();
}


void SimWindow::run()
{
	runPushed = true;
}


void SimWindow::stop()
{
	stopPushed = true;
}
