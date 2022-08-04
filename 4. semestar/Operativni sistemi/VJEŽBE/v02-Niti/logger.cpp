/* Napraviti konkurentni program za proveru znanja tablice mnozenja. Od
 * korisnika se trazi da unese proizvod dva slucajno izabrana cela broja
 * (izmedju 1 i 10). Nakon unosa, na ekranu se ispisuje da li je odgovor tacan.
 * Postupak se ponavlja dok god korisnik ne napusti program unosom slova "q".
 *
 * Osim ispisa na ekranu, tacnost svakog odgovora se nakon unosa loguje i u
 * posebnom fajlu. Logovanje u fajl se vrsi u posebnoj niti da glavna nit ne bi
 * cekala da se zavrsi rad sa fajl sistemom.
 */
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <thread>
#include <vector>

using namespace std;

ofstream logfile;

void log(string message) {
  logfile << message << "\n";
}

int main() {
  srand(time(NULL)); // da se dobijaju razliciti pseudoslucajni brojevi pri svakom pokretanju
  vector<thread *> log_threads;

  logfile.open("os.log");
  string input;
  do {
    int first_operand = rand() % 10 + 1;
    int second_operand = rand() % 10 + 1;
    cout << first_operand << "*" << second_operand << "=";
    getline(cin, input);
    if (input == "q")
      break;
    int result = atoi(input.c_str());
    string message;
    if (first_operand * second_operand == result) {
      message = (string) "TACAN ODGOVOR: " +
                to_string(first_operand) + "*" + to_string(second_operand) + "=" + input;
    } else {
      message = (string) "NETACAN ODGOVOR: " + to_string(first_operand) + "*" + to_string(second_operand) + "=" + input;
    }
    thread *t = new thread(log, message);
    log_threads.push_back(t);
  } while (true);

  for (vector<thread *>::iterator it = log_threads.begin(); it != log_threads.end(); it++)
    (*it)->join();

  logfile.close();

  return 0;
}
