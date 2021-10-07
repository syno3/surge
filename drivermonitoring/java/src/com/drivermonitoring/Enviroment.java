// we convert environment.py file to java

package com.drivermonitoring;

import org.opencv.core.Core;

public class Enviroment {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		System.out.println("loaded succesfully");


	}
	// Brightness level methods we return string
	public static int Brightness_level(){
		return 0;
	}
	// Saturation level method we return string
	public static int staturation_level(){
		return 0;
	}
	// we calculate frames per second, we return integer
	public static int frames_per_second(){
		return 0;
	}


}
