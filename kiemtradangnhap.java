import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginForm extends JFrame {

    JTextField txtUser;
    JPasswordField txtPass;
    JButton btnLogin;

    public LoginForm() {
        setTitle("Đăng nhập");
        setSize(300, 180);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(null);

        JLabel lblUser = new JLabel("Username:");
        lblUser.setBounds(20, 20, 80, 25);
        add(lblUser);

        txtUser = new JTextField();
        txtUser.setBounds(100, 20, 150, 25);
        add(txtUser);

        JLabel lblPass = new JLabel("Password:");
        lblPass.setBounds(20, 60, 80, 25);
        add(lblPass);

        txtPass = new JPasswordField();
        txtPass.setBounds(100, 60, 150, 25);
        add(txtPass);

        btnLogin = new JButton("Đăng nhập");
        btnLogin.setBounds(100, 100, 100, 25);
        add(btnLogin);

        btnLogin.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                checkLogin();
            }
        });
    }

    private void checkLogin() {
        String username = txtUser.getText();
        String password = new String(txtPass.getPassword());

        if (username.equals("admin") && password.equals("123")) {
            JOptionPane.showMessageDialog(this, "Đăng nhập thành công!");
        } else {
            JOptionPane.showMessageDialog(this, "Sai tài khoản hoặc mật khẩu!");
        }
    }

    public static void main(String[] args) {
        new LoginForm().setVisible(true);
    }
}
