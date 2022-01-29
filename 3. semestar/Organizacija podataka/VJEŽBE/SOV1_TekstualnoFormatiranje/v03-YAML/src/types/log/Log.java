package types.log;

import java.util.List;

public class Log {
	
	public String Time;
	public String User;
	public String Warning;
	public String Fatal;
	public List<Stack> Stack;
	
	public String getTime() {
		return Time;
	}
	public void setTime(String time) {
		Time = time;
	}
	public String getUser() {
		return User;
	}
	public void setUser(String user) {
		User = user;
	}
	public String getWarning() {
		return Warning;
	}
	public void setWarning(String warning) {
		Warning = warning;
	}
	public String getFatal() {
		return Fatal;
	}
	public void setFatal(String fatal) {
		Fatal = fatal;
	}
	public List<Stack> getStack() {
		return Stack;
	}
	public void setStack(List<Stack> stack) {
		Stack = stack;
	}
	@Override
	public String toString() {
		return "Log [Time=" + Time + ", User=" + User + ", Warning=" + Warning + ", Fatal=" + Fatal + ", Stack=" + Stack
				+ "]";
	}
	
	
	

}
