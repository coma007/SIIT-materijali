#include <iostream>
#include "Picture.h"
#include "Person.h"
#include "GmailUser.h"
#include "GooglePlusUser.h"

using namespace std;

int main(int argc, char **argv)
{
	Picture pic;
	pic.setPicture("./../profilna.jpg");

	GooglePlusUser gpu;
	gpu.setName("Milojica");
	gpu.setAge(11);
	gpu.setUsername("milojica12@gmail.com");
	gpu.setPassword("IV-2zakon");
	gpu.setProfilePicture(pic);

	cout << "********************************************" << endl;
	cout << "Name: " << gpu.getName() << endl;
	cout << "Age: " << gpu.getAge() << endl;
	cout << "Username: " << gpu.getUsername() << endl;
	cout << "Password: " << gpu.getPassword() << endl;
	cout << "Profile picture: " << gpu.getProfilePicture().getPicture() << endl;
	cout << "********************************************" << endl;

	return 0;
}

