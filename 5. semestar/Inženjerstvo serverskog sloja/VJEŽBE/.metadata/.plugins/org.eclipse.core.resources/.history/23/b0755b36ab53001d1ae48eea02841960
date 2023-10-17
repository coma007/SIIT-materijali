package mrezno.programiranje;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {

	public static final int TCP_PORT = 9000;

	public static void main(String[] args) {
		try {
			int clientCounter = 0;
			// slusaj zahteve na datom portu
			@SuppressWarnings("resource")
			ServerSocket ss = new ServerSocket(TCP_PORT);
			System.out.println("Server running...");
			while (true) {
				Socket sock = ss.accept();
				System.out.println("Client accepted: " + (++clientCounter));
				handleReqeust(sock, clientCounter);
			}
		} catch (Exception ex) {
			ex.printStackTrace();
		}
	}
	
	private static void handleReqeust(Socket sock, int value) {
		try {
			BufferedReader in = new BufferedReader(
					new InputStreamReader(sock.getInputStream()));

			// inicijalizuj izlazni stream
			PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(
					sock.getOutputStream())), true);
			// procitaj zahtev
			String request = in.readLine();
			System.out.println(request);

			// odgovori na zahtev
			out.println("(" + value + ")");

			// zatvori konekciju
			in.close();
			out.close();
			sock.close();
		} catch (Exception ex) {
			ex.printStackTrace();
		}
	}

}