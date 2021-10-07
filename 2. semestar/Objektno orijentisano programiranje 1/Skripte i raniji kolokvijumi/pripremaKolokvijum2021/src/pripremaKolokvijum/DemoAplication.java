package pripremaKolokvijum;

import java.awt.BorderLayout;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;


public class DemoAplication extends JFrame{

	
	/**
	 * 
	 */
	private static final long serialVersionUID = 3627433207069620118L;


	public DemoAplication() {
		
		this.setSize(300, 200);
		this.setTitle("Demo application");
//		this.setResizable(false);
		
		
		JPanel panel1 = new JPanel();
		panel1.setLayout(new GridBagLayout());
		
		
		
		JLabel user = new JLabel("User: ");
		GridBagConstraints gbc_user = new GridBagConstraints();
		gbc_user.gridx = 0;
		gbc_user.gridy = 0;
		gbc_user.anchor = GridBagConstraints.WEST;
		gbc_user.ipadx = 15;
		panel1.add(user, gbc_user);
		
		JTextField userText = new JTextField(15);
		GridBagConstraints gbc_userText = new GridBagConstraints();
		gbc_userText.gridx = 1;
		gbc_userText.gridy = 0;
		gbc_userText.gridwidth = 2;
		panel1.add(userText, gbc_userText);

		
		JLabel password = new JLabel("Password: ");
		GridBagConstraints gbc_password = new GridBagConstraints();
		gbc_password.gridx = 0;
		gbc_password.gridy = 1;
		gbc_password.anchor = GridBagConstraints.WEST;
		gbc_password.ipady = 30;
		gbc_password.ipadx = 15;
		panel1.add(password, gbc_password);
		
		JTextField passwordText = new JTextField(15);
		GridBagConstraints gbc_passwordText = new GridBagConstraints();
		gbc_passwordText.gridx = 1;
		gbc_passwordText.gridy = 1;
		panel1.add(passwordText, gbc_passwordText);
		
		JButton button1 = new JButton("login");
		GridBagConstraints gbc_button1 = new GridBagConstraints();
		gbc_button1.gridx = 0;
		gbc_button1.gridy = 2;

		gbc_button1.anchor = GridBagConstraints.WEST;
		
		JButton button2 = new JButton("register");
		GridBagConstraints gbc_button2 = new GridBagConstraints();
		gbc_button2.gridx = 1;
		gbc_button2.gridy = 2;

		gbc_button2.anchor = GridBagConstraints.EAST;
		
		panel1.add(button1, gbc_button1);
		panel1.add(button2, gbc_button2);
		
		
		button1.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				String user = "Welcome " + userText.getText();
				System.out.println(user);
				
				JOptionPane.showMessageDialog(DemoAplication.this, user);
				
				
			}
		});
		
button2.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				
				JOptionPane.showMessageDialog(DemoAplication.this, "Proceed to registration");
				
				
			}
		});
		
		
		
				
		
		this.add(panel1, BorderLayout.CENTER);
//		this.add(buttons, BorderLayout.SOUTH);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setVisible(true);
		
	}
	
	

	public static void main(String[] args) {
			
		DemoAplication d = new DemoAplication();
	}
}
