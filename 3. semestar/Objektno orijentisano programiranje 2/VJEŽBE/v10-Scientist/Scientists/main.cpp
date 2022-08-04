#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <fstream>

#include "FullName.h"
#include "Scientist.h"

using namespace std;

// global variables
vector<FullName> scientistsNames;		//vector containing full names of scientists
list<int> scientistsIds;				//list containing ids of scientists
list<Scientist> scientists;				//list containing scientists (objects of class Scientist)


// function declarations
void loadScientists(ifstream& in);

void printNames();						//prints scientists' names
void printIds();						//prints scientists' ids
void printNamesAndIds();				//prints scientists' ids and names
void printNamesAndIdsInReverse();		//prints scientists' in reverse
void addScientist();					//adds new scientist


void fillScientistsList();				//fills scientists with scientists objects (formed of full names and ids)
void removeDuplicatesAndSortById();		//removes duplicates scientists and sorts them based on their id value
void printScientistsList();				//prints the list of scientists

// main
void main()
{
	ifstream in("scientists.txt");
	if (!in)
	{
		cerr << "ERROR: wrong input file name!";
		exit(-1);
	}

	loadScientists(in);

	printNames();
	cout << endl;

	printIds();
	cout << endl;

	printNamesAndIds();
	cout << endl;

	printNamesAndIdsInReverse();
	cout << endl;
	
	addScientist();

	printNamesAndIds();
	cout << endl;

	fillScientistsList();

	printScientistsList();
	cout << endl;

	removeDuplicatesAndSortById();
	
	printScientistsList();
	cout << endl;

	return;
}

void loadScientists(ifstream& in)
{
	while(!in.eof())
	{
		string data;
		int id = 0;
		string name = "";
		string surname = "";
		
		// @TODO: read id, name and surname from input file stream
		getline(in, data);
		string tmp = "";
		for (char c : data) {
			if (c == '\t') {
				if (id == 0) {
					id = stoi(tmp);
				}
				else if (name == "") {
					name = tmp;
				}
				tmp = "";
			}
			else {
				tmp += c;
			}
		}
		surname = tmp;
		
		// @TODO: create Fullname object from name and surname and add object to the proper vector
		FullName fn = FullName(name, surname);
		scientistsNames.push_back(fn);

		// @TODO: add id to the proper list
		scientistsIds.push_back(id);
		 
		Scientist sct = Scientist(fn, id);
		scientists.push_back(sct);
		// NOTE: vector and list are already defined as global variables -> NO NEED TO MAKE NEW ONES ! <-
	}
}

void printNames()
{
	// @TODO: using iterators print the vector of names
	vector<FullName>::iterator sctNamesIt;
	for (sctNamesIt = scientistsNames.begin(); sctNamesIt != scientistsNames.end(); sctNamesIt++)
	{
		cout << (*sctNamesIt).getName() + " " + (*sctNamesIt).getSurname() << endl;
	}
}

void printIds()
{
	// @TODO: using iterators print the list of ids
	list<int>::iterator sctIdsIt;
	for (sctIdsIt = scientistsIds.begin(); sctIdsIt != scientistsIds.end(); sctIdsIt++)
	{
		cout << *sctIdsIt << endl;
	}
}

void printNamesAndIds()
{
	// @TODO: using iterators print scientist id and the its name and surname
	// using list of ids and vector of names
	list<int>::iterator sctIdsIt;
	vector<FullName>::iterator sctNamesIt;
	for (sctIdsIt = scientistsIds.begin(), sctNamesIt = scientistsNames.begin(); sctIdsIt != scientistsIds.end(), sctNamesIt != scientistsNames.end(); sctIdsIt++, sctNamesIt++)
	{
		cout << (*sctIdsIt)<< " " << (*sctNamesIt).getName() << " " << (*sctNamesIt).getSurname() << endl;
	}
}

void printNamesAndIdsInReverse()
{
	// @TODO: using iterators print scientist id and the its name and surname
	// using list of ids and vector of names, in reverse
	list<int>::reverse_iterator sctIdsIt;
	vector<FullName>::reverse_iterator sctNamesIt;
	for (sctIdsIt = scientistsIds.rbegin(), sctNamesIt = scientistsNames.rbegin(); sctIdsIt != scientistsIds.rend(), sctNamesIt != scientistsNames.rend(); sctIdsIt++, sctNamesIt++)
	{
		cout << (*sctIdsIt) << " " << (*sctNamesIt).getName() << " " << (*sctNamesIt).getSurname() << endl;
	}
}

void addScientist()
{
	FullName newScientist("Petar", "Petrovic");
	int newID = 999;
	
	FullName findName("Nikola", "Tesla");
	int findId = 123;
	
	// @TODO: add new scientist "Petar Petrovic" with "999" ID, after
	// "Nikola Tesla" who has "123" as ID
	list<int>::iterator sctIdsIt;
	vector<FullName>::iterator sctNamesIt;
	list<int>::iterator iterID;
	vector<FullName>::iterator iterFN;
	for (sctIdsIt = scientistsIds.begin(), sctNamesIt = scientistsNames.begin(); sctIdsIt != scientistsIds.end(), sctNamesIt != scientistsNames.end(); sctIdsIt++, sctNamesIt++)
	{
		if ((*sctIdsIt) == findId && (*sctNamesIt) == findName) {
			iterID = ++sctIdsIt;
			iterFN = ++sctNamesIt;
			--sctIdsIt;
			--sctNamesIt;
		}
	}
	scientistsIds.insert(iterID, newID);
	scientistsNames.insert(iterFN, newScientist);
}

void fillScientistsList()
{
	// @TODO: fill the list of scientists by creating objects of class Scientist
	// NOTE: use existing vector of names and list of ids to create Scientist objects
	list<int>::iterator sctIdsIt;
	vector<FullName>::iterator sctNamesIt;
	for (sctIdsIt = scientistsIds.begin(), sctNamesIt = scientistsNames.begin(); sctIdsIt != scientistsIds.end(), sctNamesIt != scientistsNames.end(); sctIdsIt++, sctNamesIt++)
	{
		scientists.push_back(Scientist((*sctNamesIt), (*sctIdsIt)));
	}
	cout << scientists.size() << endl;
}

void removeDuplicatesAndSortById()
{
	scientists.sort();
	scientists.unique();
}

void printScientistsList()

{
	// @TODO print the list of scientists
	list<Scientist>::iterator sctIt;
	for (sctIt = scientists.begin(); sctIt != scientists.end(); sctIt++)
	{
		cout << (*sctIt).getId() << " " << (*sctIt).getFullName().getName() << " " << (*sctIt).getFullName().getSurname() << endl;
	}
}
