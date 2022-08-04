/*
 * BitmapRawConverter.cpp
 *
 *  Created on: Sep 11, 2011
 *      Author: svetozar
 */


#include "BitmapRawConverter.h"
#include <stdlib.h>

BitmapRawConverter::BitmapRawConverter(char *filename) {
	bitmap.ReadFromFile(filename);
	width = bitmap.TellWidth();
	height = bitmap.TellHeight();

	bitmapToPixels();
}

void BitmapRawConverter::bitmapToPixels() {
	pixels = (int *) malloc(width * height * sizeof(int));  //new int[width * height];

	for (int i = 0; i < width; i++) {
		for (int j = 0; j < height; j++) {
			RGBApixel pxl = bitmap.GetPixel(i,j);
			putPixel(i, j, pxl);
		}
	}
}

void BitmapRawConverter::pixelsToBitmap(char *outFilename) {
	BMP out;
	out.SetSize(width, height);
	out.SetBitDepth(24);

	for (int i = 0; i < width; i++) {
		for (int j = 0; j < height; j++) {
			out.SetPixel(i, j, getPixel(i,j));
		}
	}
	out.WriteToFile(outFilename);
}

RGBApixel BitmapRawConverter::getPixel(int i, int j) {
	RGBApixel pxl;
	int value = pixels[j * width + i];
	pxl.Red = value;
	pxl.Green = value;
	pxl.Blue = value;

	return pxl;
}

void BitmapRawConverter::putPixel(int i, int j, RGBApixel value) {
	pixels[j * width + i] = ((30 * value.Red) + (59 * value.Green) + (11 * value.Blue)) / 100;
}

int *BitmapRawConverter::getBuffer()
{
	return pixels;
}

void BitmapRawConverter::setBuffer(int *buffer)
{
	memcpy((void *)pixels, (void *)buffer, width * height * sizeof(int));
}

int BitmapRawConverter::getHeight() const
{
    return height;
}

int BitmapRawConverter::getWidth() const
{
    return width;
}

void BitmapRawConverter::setHeight(int height)
{
    this->height = height;
}

void BitmapRawConverter::setWidth(int width)
{
    this->width = width;
}

BitmapRawConverter::~BitmapRawConverter() {
	delete pixels;
}

