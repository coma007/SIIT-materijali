/* Simulirati rad Operativnog sistema koji ima sledece funkcionalnosti.
 *
 * 1. Pokretanje i zaustavljanje servisa. Programski kod koji servisi izvrsavaju
 * dat je u obliku slobodnih funkcija.
 * Za potrebe testiranja, date su dve funkcije serviceA i serviceB. Svaki servis
 * predstavljen je posebnom klasom, kojoj se pri instanciranju definise
 * programski kod koji ce izvrsavati po startovanju. Proces se izvrsava u
 * posebnoj niti.
 *
 * 2. Rad sa fajlovima. Omoguciti kreiranje, brisanje i preimenovanje fajlova i
 * direktorijuma u operativnom sistemu.
 * (fajlovi i direktorijumi su hijerarhijski organizovani)
 *
 * 3. Rad sa korisnicima. Omoguciti administraciju (unos, izmena, brisanje)
 * korisnika u sistemu. Omoguciti organizovanje korisnika u grupe.
 *
 * 4. Napraviti podrsku za prava pristupa fajlovima. Svaki korisnik nad fajlom
 * ima pravo citanja, pisanja ili i jedno i drugo.
 *
 * Implementirati Shell koji omogucuje koriscenje navedenih funkcionalnosti.
 */
#include <iostream>
#include <map>
#include <thread>

using namespace std;

typedef void (*process_function)(void);

void serviceA() {
  cout << "Process f1 started." << endl;
  for (int i = 0; i < 1000000; i++) {
  }
  cout << "Process f1 finished." << endl;
}

void serviceB() {
  while (true) {
    cout << "f2 hello" << endl;
  }
}

class Process {
  // ProcessDescriptor descriptor;
  process_function f;
  thread process_thread;

public:
  Process(process_function pFunc) {
    f = pFunc;
  }
  void start() {
    process_thread = thread(f);
    process_thread.detach();
  }
};

class Os {
  map<string, process_function> functions;

public:
  Os() {
    register_services();
  }
  void register_services();
  process_function get_service_by_name(string);
  Process create_process(process_function f);
};

void Os::register_services() {
  functions["service_a"] = serviceA;
  functions["service_b"] = serviceB;
}

process_function Os::get_service_by_name(string f_name) {
  return functions[f_name];
}

class Command {
public:
  virtual string execute(Os &) = 0;
};

class Start_service_command : public Command {
private:
  string service_name;

public:
  Start_service_command(string sn) { service_name = sn; }
  string execute(Os &);
};

string Start_service_command::execute(Os &os) {
  process_function f = os.get_service_by_name(service_name);
  f();
  return "Process started.";
}

class Command_factory {
public:
  static Command *create_command(string command_string);
};

Command *Command_factory::create_command(string command_string) {
  // TODO parse string to get command and parameters
  if (command_string.find("start") == 0) { // string starts with "start"
    int pos = command_string.find(" ");
    string service_name = command_string.substr(pos + 1, command_string.size());
    return new Start_service_command(service_name);
  } else
    throw "Invalid command!";
}

class Shell {
private:
  Os os;
  string take_command();
  string execute_command(string command_string);

public:
  Shell(Os &os_param) {
    os = os_param;
  }
  void start();
};

void Shell::start() {
  while (true) {
    string command = take_command();
    string result = execute_command(command);
    cout << result << endl;
  }
}

string Shell::take_command() {
  string command;
  cout << ">>";
  getline(cin, command);
  return command;
}

string Shell::execute_command(string command_string) {
  Command *c = Command_factory::create_command(command_string);
  string result = c->execute(os);
  return result;
}

int main() {
  Os os;
  Shell s(os);

  s.start();

  return 0;
}
