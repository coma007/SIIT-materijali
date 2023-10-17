package rs.ac.uns.testing.user;

public class UserService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public boolean isValidUser(String id, String password) {
        User user = userRepository.findById(id);
        return isEnabledUser(user) && isValidPassword(user, password);
    }

    private boolean isEnabledUser(User user) {
        return user != null && user.isEnabled();
    }

    private boolean isValidPassword(User user, String password) {
        String encodedPassword = passwordEncoder.encode(password);
        return encodedPassword.equals(user.getPasswordHash());
    }
}
