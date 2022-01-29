package pripremaKolokvijum;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Hello extends JFrame{

	
	/**
	 * 
	 */
	private static final long serialVersionUID = 3627433207069620118L;
	DemoAplication frame = new DemoAplication();


	public Hello() {
		
		this.setSize(500, 500);
		this.setTitle("Hello");
		this.frame.setVisible(false);
		
		JLabel hello = new JLabel("Hello World !");
		this.add(hello, BorderLayout.CENTER);
		hello.setVisible(false);
		hello.setHorizontalAlignment(0);
		
		JButton button = new JButton("Button");
		this.add(button, BorderLayout.SOUTH);
		button.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				hello.setVisible(true);
				frame.setVisible(true);
				
				
			}
		});
				
		
		
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setVisible(true);
		
	}
	
	

	public static void main(String[] args) {
			
		Hello h = new Hello();
	}
}
